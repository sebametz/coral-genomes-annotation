#!/usr/bin/env python3
"""
compile_summary_table.py
-------------------------
Parses all per-genome result files and compiles one wide summary TSV.
Reads the project folder structure — no manifest required at this stage.

Expects this structure under results/{genome_id_safe}/:
    annotation_stats/coding_region_stats.txt
    annotation_stats/intron_stats.txt
    assembly_stats/seqkit_stats.txt
    assembly_stats/masked_percentage.txt
    repeats/repeats.tsv
    functional/eggnog.annotations
    busco/short_summary*.txt
    omark/summary.sum

Usage:
    python compile_summary_table.py \\
        --project /path/to/coral-genomes-annotation \\
        --out tables/genome_traits_summary.tsv

    # single genome (for testing)
    python compile_summary_table.py \\
        --project /path/to/coral-genomes-annotation \\
        --genome GCA_964261235_1 \\
        --out tables/genome_traits_summary.tsv
"""

import argparse
import csv
import glob
import os
import re
import sys

NA = "NA"


# ═════════════════════════════════════════════════════════════════════════════
# PARSERS — one function per file type, returns a flat dict
# ═════════════════════════════════════════════════════════════════════════════

def parse_coding_region_stats(path):
    """
    coding_region_stats.txt format:
    ---
    genes: 27072
    average_gene_length: 6384
    ...
    """
    out = {
        "genes":                    NA,
        "average_gene_length":      NA,
        "transcripts_per_gene":     NA,
        "average_transcript_length":NA,
        "exons_per_transcript":     NA,
        "average_exon_length":      NA,
    }
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line == "---":
                    continue
                if ":" in line:
                    key, _, val = line.partition(":")
                    key = key.strip()
                    val = val.strip()
                    if key in out:
                        out[key] = val
    except FileNotFoundError:
        pass
    return out


def parse_intron_stats(path):
    """
    intron_stats.txt format:
    transcripts_total: 32783
    single_exon_transcripts: 8218
    ...
    """
    out = {
        "transcripts_total":        NA,
        "single_exon_transcripts":  NA,
        "multi_exon_transcripts":   NA,
        "introns_total":            NA,
        "avg_introns_per_transcript":NA,
        "avg_intron_length":        NA,
        "median_intron_length":     NA,
        "min_intron_length":        NA,
        "max_intron_length":        NA,
    }
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    key, _, val = line.partition(":")
                    key = key.strip()
                    val = val.strip()
                    if key in out:
                        out[key] = val
    except FileNotFoundError:
        pass
    return out


def parse_masked_percentage(path):
    """
    masked_percentage.txt format:
    GCA_942486025.1/GCA_942486025.1.fa.masked\t46.1824
    """
    out = {"soft_masked_pct": NA}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                if len(parts) >= 2:
                    out["soft_masked_pct"] = parts[-1].strip()
                    break
                # fallback: single value on line
                try:
                    float(line)
                    out["soft_masked_pct"] = line
                    break
                except ValueError:
                    pass
    except FileNotFoundError:
        pass
    return out


def parse_seqkit_stats(path):
    """
    seqkit_stats.txt format: TSV with header
    file format type num_seqs sum_len ... N50 ... GC(%)
    """
    out = {
        "scaffold_count":   NA,
        "total_bp":         NA,
        "min_scaffold_len": NA,
        "avg_scaffold_len": NA,
        "max_scaffold_len": NA,
        "N50":              NA,
        "gc_pct":           NA,
    }
    try:
        with open(path) as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                out["scaffold_count"]   = row.get("num_seqs", NA).strip()
                out["total_bp"]         = row.get("sum_len",  NA).strip()
                out["min_scaffold_len"] = row.get("min_len",  NA).strip()
                out["avg_scaffold_len"] = row.get("avg_len",  NA).strip()
                out["max_scaffold_len"] = row.get("max_len",  NA).strip()
                out["N50"]              = row.get("N50",      NA).strip()
                out["gc_pct"]           = row.get("GC(%)",    NA).strip()
                break  # only one data row expected
    except FileNotFoundError:
        pass
    return out


def parse_busco(path):
    """
    BUSCO short_summary format:
    C:88.9%[S:64.5%,D:24.4%],F:3.4%,M:7.6%,n:3203
    Also extract lineage from header comment.
    """
    out = {
        "busco_lineage":        NA,
        "busco_complete_pct":   NA,
        "busco_single_pct":     NA,
        "busco_duplicated_pct": NA,
        "busco_fragmented_pct": NA,
        "busco_missing_pct":    NA,
        "busco_n":              NA,
        "busco_mode":           NA,
    }

    re_scores = re.compile(
        r"C:([\d.]+)%\[S:([\d.]+)%,D:([\d.]+)%\],F:([\d.]+)%,M:([\d.]+)%,n:(\d+)"
    )
    re_lineage = re.compile(r"lineage dataset is:\s+(\S+)")
    re_mode    = re.compile(r"BUSCO was run in mode:\s+(\S+)")

    try:
        # resolve glob if directory given
        if os.path.isdir(path):
            matches = glob.glob(os.path.join(path, "short_summary*.txt"))
            if not matches:
                return out
            path = matches[0]

        with open(path) as f:
            for line in f:
                m = re_lineage.search(line)
                if m:
                    # extract just the lineage name e.g. cnidaria_odb12
                    out["busco_lineage"] = m.group(1).split("(")[0].strip()

                m = re_mode.search(line)
                if m:
                    out["busco_mode"] = m.group(1)

                m = re_scores.search(line)
                if m:
                    out["busco_complete_pct"]   = m.group(1)
                    out["busco_single_pct"]     = m.group(2)
                    out["busco_duplicated_pct"] = m.group(3)
                    out["busco_fragmented_pct"] = m.group(4)
                    out["busco_missing_pct"]    = m.group(5)
                    out["busco_n"]              = m.group(6)
    except FileNotFoundError:
        pass
    return out


def parse_omark(path):
    """
    OMARK summary.sum format — see uploaded example.
    Extracts HOG-level and proteome-level statistics.
    """
    out = {
        "omark_clade":              NA,
        "omark_conserved_hogs":     NA,
        "omark_single_pct":         NA,
        "omark_duplicated_pct":     NA,
        "omark_dup_unexpected_pct": NA,
        "omark_dup_expected_pct":   NA,
        "omark_missing_pct":        NA,
        "omark_consistent_pct":     NA,
        "omark_inconsistent_pct":   NA,
        "omark_contamination_pct":  NA,
        "omark_unknown_pct":        NA,
    }

    re_clade     = re.compile(r"selected clade was (.+)")
    re_hogs      = re.compile(r"Number of conserved HOGs is:\s+(\d+)")
    re_hog_pct   = re.compile(
        r"S:([\d.]+)%,D:([\d.]+)%\[U:([\d.]+)%,E:([\d.]+)%\],M:([\d.]+)%"
    )
    re_prot_pct  = re.compile(
        r"A:([\d.]+)%.*?I:([\d.]+)%.*?C:([\d.]+)%.*?U:([\d.]+)%"
    )

    try:
        with open(path) as f:
            for line in f:
                line = line.strip()

                m = re_clade.search(line)
                if m:
                    out["omark_clade"] = m.group(1).strip()

                m = re_hogs.search(line)
                if m:
                    out["omark_conserved_hogs"] = m.group(1)

                m = re_hog_pct.search(line)
                if m:
                    out["omark_single_pct"]         = m.group(1)
                    out["omark_duplicated_pct"]      = m.group(2)
                    out["omark_dup_unexpected_pct"]  = m.group(3)
                    out["omark_dup_expected_pct"]    = m.group(4)
                    out["omark_missing_pct"]         = m.group(5)

                m = re_prot_pct.search(line)
                if m:
                    out["omark_consistent_pct"]     = m.group(1)
                    out["omark_inconsistent_pct"]   = m.group(2)
                    out["omark_contamination_pct"]  = m.group(3)
                    out["omark_unknown_pct"]         = m.group(4)
    except FileNotFoundError:
        pass
    return out


def parse_eggnog(path):
    """
    EggNOG .annotations format: TSV, comment lines start with ##, header with #.
    Columns: query seed_ortholog evalue score eggNOG_OGs max_annot_lvl
             COG_category Description Preferred_name GOs EC KEGG_ko
             KEGG_Pathway KEGG_Module KEGG_Reaction KEGG_rclass BRITE
             KEGG_TC CAZy BiGG_Reaction PFAMs
    """
    out = {
        "eggnog_total_queries":    NA,
        "eggnog_annotated":        NA,
        "eggnog_annotated_pct":    NA,
        "eggnog_with_go":          NA,
        "eggnog_with_go_pct":      NA,
        "eggnog_with_kegg_ko":     NA,
        "eggnog_with_kegg_ko_pct": NA,
        "eggnog_with_cog":         NA,
        "eggnog_with_cog_pct":     NA,
        "eggnog_with_pfam":        NA,
        "eggnog_with_pfam_pct":    NA,
    }

    re_total = re.compile(r"##\s+(\d+)\s+queries scanned")

    total_queries = None
    annotated     = 0
    with_go       = 0
    with_kegg_ko  = 0
    with_cog      = 0
    with_pfam     = 0

    fieldnames = None

    try:
        with open(path) as f:
            for line in f:
                # total queries from footer comment
                m = re_total.search(line)
                if m:
                    total_queries = int(m.group(1))
                    continue

                # skip metadata comments
                if line.startswith("##"):
                    continue

                # header line
                if line.startswith("#query"):
                    fieldnames = [c.strip() for c in line.lstrip("#").split("\t")]
                    continue

                if fieldnames is None:
                    continue

                parts = line.rstrip("\n").split("\t")
                if len(parts) < 2:
                    continue

                row = dict(zip(fieldnames, parts))
                annotated += 1

                if row.get("GOs",      "-").strip() not in ("-", ""):
                    with_go      += 1
                if row.get("KEGG_ko",  "-").strip() not in ("-", ""):
                    with_kegg_ko += 1
                if row.get("COG_category", "-").strip() not in ("-", ""):
                    with_cog     += 1
                if row.get("PFAMs",    "-").strip() not in ("-", ""):
                    with_pfam    += 1

    except FileNotFoundError:
        return out

    total = total_queries if total_queries else annotated

    def pct(n, d):
        return f"{round(n / d * 100, 2)}" if d > 0 else NA

    out["eggnog_total_queries"]    = str(total)
    out["eggnog_annotated"]        = str(annotated)
    out["eggnog_annotated_pct"]    = pct(annotated,    total)
    out["eggnog_with_go"]          = str(with_go)
    out["eggnog_with_go_pct"]      = pct(with_go,      total)
    out["eggnog_with_kegg_ko"]     = str(with_kegg_ko)
    out["eggnog_with_kegg_ko_pct"] = pct(with_kegg_ko, total)
    out["eggnog_with_cog"]         = str(with_cog)
    out["eggnog_with_cog_pct"]     = pct(with_cog,     total)
    out["eggnog_with_pfam"]        = str(with_pfam)
    out["eggnog_with_pfam_pct"]    = pct(with_pfam,    total)
    return out


def parse_interproscan(path):
    """
    InterProScan TSV format (12 columns):
    protein_id  md5  length  analysis  sig_acc  sig_desc
    start  end  score  status  date  ipr_acc  [ipr_desc  go_terms]
    """
    out = {
        "iprscan_proteins_with_domain":     NA,
        "iprscan_proteins_with_domain_pct": NA,
        "iprscan_proteins_with_go":         NA,
        "iprscan_proteins_with_go_pct":     NA,
        "iprscan_total_proteins":           NA,
    }
    try:
        proteins_with_domain = set()
        proteins_with_go     = set()
        all_proteins         = set()

        with open(path) as f:
            for line in f:
                if line.startswith("#") or not line.strip():
                    continue
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 11:
                    continue
                pid = parts[0].strip()
                all_proteins.add(pid)
                proteins_with_domain.add(pid)
                # GO terms in column 13 (0-indexed 12) if present
                if len(parts) > 13:
                    go = parts[13].strip()
                    if go and go != "-":
                        proteins_with_go.add(pid)

        total = len(all_proteins)
        def pct(n, d):
            return f"{round(n / d * 100, 2)}" if d > 0 else NA

        out["iprscan_total_proteins"]           = str(total)
        out["iprscan_proteins_with_domain"]     = str(len(proteins_with_domain))
        out["iprscan_proteins_with_domain_pct"] = pct(len(proteins_with_domain), total)
        out["iprscan_proteins_with_go"]         = str(len(proteins_with_go))
        out["iprscan_proteins_with_go_pct"]     = pct(len(proteins_with_go), total)
    except FileNotFoundError:
        pass
    return out


def parse_repeats_tsv(path):
    """
    repeats.tsv — already in our parsed format from parse_repeatmasker_tbl.py.
    Extract level-0 rows and the SUMMARY total for the wide table.
    """
    out = {
        "repeat_retroelements_pct":       NA,
        "repeat_dna_transposons_pct":     NA,
        "repeat_rolling_circles_pct":     NA,
        "repeat_unclassified_pct":        NA,
        "repeat_total_interspersed_pct":  NA,
        "repeat_small_rna_pct":           NA,
        "repeat_satellites_pct":          NA,
        "repeat_simple_repeats_pct":      NA,
        "repeat_low_complexity_pct":      NA,
    }

    # name fragment → output key
    NAME_MAP = {
        "retroelement":       "repeat_retroelements_pct",
        "dna transposon":     "repeat_dna_transposons_pct",
        "rolling-circle":     "repeat_rolling_circles_pct",
        "unclassified":       "repeat_unclassified_pct",
        "small rna":          "repeat_small_rna_pct",
        "satellite":          "repeat_satellites_pct",
        "simple repeat":      "repeat_simple_repeats_pct",
        "low complexity":     "repeat_low_complexity_pct",
    }

    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                name      = row.get("name", "").strip().lower()
                is_total  = row.get("is_total", "false").strip().lower()
                level     = row.get("level", "").strip()
                pct       = row.get("pct_of_genome", NA).strip()

                if is_total == "true" and "interspersed" in name:
                    out["repeat_total_interspersed_pct"] = pct
                    continue

                if level != "0":
                    continue

                for fragment, key in NAME_MAP.items():
                    if fragment in name:
                        out[key] = pct
                        break
    except FileNotFoundError:
        pass
    return out


# ═════════════════════════════════════════════════════════════════════════════
# OUTPUT COLUMNS — order defines column order in the final table
# ═════════════════════════════════════════════════════════════════════════════

OUTPUT_COLS = [
    # Identity
    "genome_id",
    # Assembly
    "total_bp", "scaffold_count", "N50",
    "min_scaffold_len", "avg_scaffold_len", "max_scaffold_len", "gc_pct",
    "soft_masked_pct",
    # Repeats
    "repeat_retroelements_pct", "repeat_dna_transposons_pct",
    "repeat_rolling_circles_pct", "repeat_unclassified_pct",
    "repeat_total_interspersed_pct",
    "repeat_small_rna_pct", "repeat_satellites_pct",
    "repeat_simple_repeats_pct", "repeat_low_complexity_pct",
    # Annotation: genes
    "genes", "average_gene_length",
    "transcripts_per_gene", "average_transcript_length",
    "exons_per_transcript", "average_exon_length",
    # Annotation: introns
    "transcripts_total", "single_exon_transcripts", "multi_exon_transcripts",
    "introns_total", "avg_introns_per_transcript",
    "avg_intron_length", "median_intron_length",
    "min_intron_length", "max_intron_length",
    # BUSCO
    "busco_lineage", "busco_mode", "busco_n",
    "busco_complete_pct", "busco_single_pct", "busco_duplicated_pct",
    "busco_fragmented_pct", "busco_missing_pct",
    # OMARK
    "omark_clade", "omark_conserved_hogs",
    "omark_single_pct", "omark_duplicated_pct",
    "omark_dup_unexpected_pct", "omark_dup_expected_pct",
    "omark_missing_pct",
    "omark_consistent_pct", "omark_inconsistent_pct",
    "omark_contamination_pct", "omark_unknown_pct",
    # EggNOG
    "eggnog_total_queries", "eggnog_annotated", "eggnog_annotated_pct",
    "eggnog_with_go", "eggnog_with_go_pct",
    "eggnog_with_kegg_ko", "eggnog_with_kegg_ko_pct",
    "eggnog_with_cog", "eggnog_with_cog_pct",
    "eggnog_with_pfam", "eggnog_with_pfam_pct",
    # InterProScan
    "iprscan_total_proteins",
    "iprscan_proteins_with_domain", "iprscan_proteins_with_domain_pct",
    "iprscan_proteins_with_go", "iprscan_proteins_with_go_pct",
]


# ═════════════════════════════════════════════════════════════════════════════
# GENOME RUNNER
# ═════════════════════════════════════════════════════════════════════════════

def process_genome(genome_id, results_dir):
    """Run all parsers for one genome. Returns a flat dict of all columns."""

    def p(*parts):
        return os.path.join(results_dir, *parts)

    # Resolve BUSCO short_summary — could be in busco/ directly or busco/run_*/
    busco_candidates = (
        glob.glob(p("busco", "short_summary*.txt")) +
        glob.glob(p("busco", "run_*", "short_summary*.txt"))
    )
    busco_path = busco_candidates[0] if busco_candidates else p("busco", "short_summary.txt")

    row = {"genome_id": genome_id}
    row.update(parse_coding_region_stats(p("annotation_stats", "coding_region_stats.txt")))
    row.update(parse_intron_stats(        p("annotation_stats", "intron_stats.txt")))
    row.update(parse_masked_percentage(   p("assembly_stats",   "masked_percentage.txt")))
    row.update(parse_seqkit_stats(        p("assembly_stats",   "seqkit_stats.txt")))
    row.update(parse_busco(               busco_path))
    row.update(parse_omark(               p("omark",            "summary.sum")))
    row.update(parse_eggnog(              p("functional",        "eggnog.annotations")))
    row.update(parse_interproscan(        p("functional",        "interproscan.tsv")))
    row.update(parse_repeats_tsv(         p("repeats",          "repeats.tsv")))

    return row


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Compile genome summary table from all per-genome result files"
    )
    parser.add_argument("--project", required=True,
                        help="Project root (coral-genomes-annotation/)")
    parser.add_argument("--out",     required=True,
                        help="Output TSV path e.g. tables/genome_traits_summary.tsv")
    parser.add_argument("--genome",  default=None,
                        help="Process only this genome_id_safe (for testing)")
    args = parser.parse_args()

    results_base = os.path.join(args.project, "results")
    if not os.path.isdir(results_base):
        sys.exit(f"ERROR: results/ not found under {args.project}")

    # Discover genomes
    if args.genome:
        genome_dirs = [args.genome]
    else:
        genome_dirs = sorted(
            d for d in os.listdir(results_base)
            if os.path.isdir(os.path.join(results_base, d))
        )

    if not genome_dirs:
        sys.exit("ERROR: no genome directories found in results/")

    print(f"Processing {len(genome_dirs)} genome(s)...\n")

    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else ".", exist_ok=True)

    ok = errors = 0
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLS, delimiter="\t",
                                extrasaction="ignore")
        writer.writeheader()

        for gid in genome_dirs:
            results_dir = os.path.join(results_base, gid)
            try:
                row = process_genome(gid, results_dir)

                # Fill any missing columns with NA
                for col in OUTPUT_COLS:
                    row.setdefault(col, NA)

                writer.writerow(row)

                # Status line
                genes   = row.get("genes", NA)
                busco_c = row.get("busco_complete_pct", NA)
                masked  = row.get("soft_masked_pct", NA)
                iprscan = row.get("iprscan_proteins_with_domain_pct", NA)
                iprtag  = "" if iprscan != NA else " [no iprscan]"
                print(f"  ✓  {gid:<30}  genes={genes:<7}  "
                      f"BUSCO={busco_c}%  masked={masked}%{iprtag}")
                ok += 1

            except Exception as e:
                print(f"  ✗  {gid}: {e}")
                errors += 1

    print(f"\nWritten → {args.out}")
    print(f"  OK: {ok}  |  Errors: {errors}")
    print(f"  Columns: {len(OUTPUT_COLS)}  |  Rows: {ok}")
    if errors:
        print("  Fix errors above and re-run — the table will be overwritten cleanly.")


if __name__ == "__main__":
    main()

