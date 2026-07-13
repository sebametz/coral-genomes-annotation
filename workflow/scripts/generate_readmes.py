#!/usr/bin/env python3
"""
generate_readmes.py
--------------------
Auto-generates a README.md for each genome in results/{tolid}_{species}/
from genomes.tsv + genome_traits_summary.tsv.

Re-run this script whenever annotations are updated — all 95 READMEs
regenerate in seconds. No manual editing needed.

Usage:
    python generate_readmes.py \\
        --project /path/to/coral-genomes-annotation \\
        --mapping config/tolid_mapping.tsv \\
        --summary tables/genome_traits_summary.tsv \\
        --manifest config/genomes.tsv

    # single genome (for testing)
    python generate_readmes.py \\
        --project /path/to/coral-genomes-annotation \\
        --mapping config/tolid_mapping.tsv \\
        --summary tables/genome_traits_summary.tsv \\
        --manifest config/genomes.tsv \\
        --genome GCA_964261235_1
"""

import argparse
import csv
import os
import sys
from datetime import date

NA = "NA"


# ── Changelog ─────────────────────────────────────────────────────────────────
# Edit this dict to add/update version entries.
# Keys are version strings, values are lists of change descriptions.
# The script detects whether a genome was in v1 automatically.

CHANGELOG = {
    "v2.0": [
        " Extended dataset from 40 to 95 genomes",
        " Two-pass BRAKER3 gene prediction pipeline (with RNA-seq, when available, and protein evidence)",
        " New proteome database for first annotation including OrthoDB v12 Cnidaria, plus predicted proteins from V1 genome annotations",
        " Genomes without RNA-seq data, BRAKER3 in protein-only mode for those",
        " Added InterProScan protein domain annotation",
        " Added intron statistics",
        " Re-ran BUSCO quality assessment with cnidaria_odb12 lineage",
        " Re-ran OMARK annotation quality assessment",
        " Re-ran EggNOG-mapper with updated database",
        " Standardised file naming and folder structure",
    ],
    "v1.0": [
        " Initial release: 40 genomes, 22 genera, 13 families",
        " BRAKER3 gene prediction pipeline",
        " BUSCO quality assessment",
        " EggNOG-mapper functional annotation",
        " RepeatModeler/RepeatMasker repeat annotation",
    ],
}

# ToLIDs that were in v1 (from the original 36 + 4 more from v1 Zenodo)
V1_TOLIDS = {
    "jaBlaWell11","jaGalFasc40","jaMonCapi2","jaPorLute2","jaMeaMean2",
    "jaSidRadi1","jaAcrSpat14","jaMicLord3","jaSidSide1","jaAcrCerv1",
    "jaPorCyli1","jaPorRusx1","jaPorDiva4","jaMadAure2","jaDenCyli1",
    "jaCypSala7","jaOrbFran1","jaPocDami1","jaTurReni1","jaMonSpea1",
    "jaIsoPali11","jaDunAxif1","jaAcrSpic1","jaAcrAuse1","jaAcrGlau1",
    "jaAcrHyac4","jaMonPala3","jaAcrMuri1","jaMadSena2","jaOcuArbu1",
    "jaMonCapr1","jaSteInte3","jaAcrPulc1","jaAcrLori1","jaDipLaby1",
    "jaCauFurc1","jaAcrPala1","jaPocGran1","jaStyPist1","jaEchHorr1",
}


# ── Loaders ───────────────────────────────────────────────────────────────────

def load_tsv(path, key_col):
    """Load a TSV into a dict keyed by key_col."""
    with open(path, newline="") as f:
        return {row[key_col]: row for row in csv.DictReader(f, delimiter="\t")}


# ── Formatting helpers ────────────────────────────────────────────────────────

def val(d, key, suffix="", digits=None):
    """Safely get a value from a dict, format it, return '—' if NA."""
    v = d.get(key, NA)
    if v in (NA, "", None):
        return "—"
    if digits is not None:
        try:
            v = f"{float(v):.{digits}f}"
        except (ValueError, TypeError):
            pass
    return f"{v}{suffix}"


def pct(d, key):
    return val(d, key, suffix="%", digits=2)


def busco_line(s):
    """Format BUSCO as: C:88.9% [S:64.5%, D:24.4%] F:3.4% M:7.6%"""
    c = s.get("busco_complete_pct", NA)
    sc = s.get("busco_single_pct", NA)
    d = s.get("busco_duplicated_pct", NA)
    f = s.get("busco_fragmented_pct", NA)
    m = s.get("busco_missing_pct", NA)
    n = s.get("busco_n", NA)
    if c == NA:
        return "—"
    return f"C:{c}% [S:{sc}%, D:{d}%] F:{f}% M:{m}% (n={n})"


def ena_url(genome_id):
    return f"https://www.ebi.ac.uk/ena/browser/view/{genome_id}"


def ncbi_url(genome_id):
    return f"https://www.ncbi.nlm.nih.gov/datasets/genome/{genome_id}/"


# ── README template ───────────────────────────────────────────────────────────

def render_readme(manifest_row, stats_row, tolid, version="v2"):
    gid      = manifest_row.get("genome_id", NA)
    species  = manifest_row.get("tax_species", NA)
    genus    = manifest_row.get("tax_genus", NA)
    family   = manifest_row.get("tax_family", NA)
    order    = manifest_row.get("tax_order", NA)
    ncbi_tax = manifest_row.get("tax_ncbi_taxid", NA)
    pipeline = manifest_row.get("prov_annotation_pipeline", NA)
    pip_ver  = manifest_row.get("prov_annotation_pipeline_version", NA)
    ref_db   = manifest_row.get("prov_ref_db", NA)
    ref_ver  = manifest_row.get("prov_ref_db_version", NA)
    zen_doi  = manifest_row.get("prov_genome_doi", NA)
    haplotype = manifest_row.get("haplotype", NA)
    busco_lin = stats_row.get("busco_lineage", NA) if stats_row else NA

    zen_link = (f"[{zen_doi}](https://doi.org/{zen_doi.replace('https://doi.org/','')})"
                if zen_doi not in (NA, "—", "") else "— (not yet deposited)")
    
    # Changelog
    changelog_lines = []
    if tolid in V1_TOLIDS:
        for ver, changes in CHANGELOG.items():
            changelog_lines.append(f"**{ver}**")
            for c in changes:
                changelog_lines.append(f"* {c}")
            changelog_lines.append("")
    else:
        changelog_lines.append(f"**{version}**")
        for c in CHANGELOG.get(version, []):
            changelog_lines.append(f"* {c}")
        changelog_lines.append("")

    # Stats section
    s = stats_row if stats_row else {}

    lines = [
        f"# *{species}* — {tolid} / {gid}",
        "",
        "## Overview",
        "",
        "| | |",
        "|---|---|",
        f"| **Species** | *{species}* |",
        f"| **Family** | {family} |",
        f"| **Order** | {order} |",
        f"| **Assembly accession** | [{gid}]({ena_url(gid)}) |",
        f"| **ToLID** | {tolid} |",
        f"| **Haplotype** | {haplotype} |",
        f"| **NCBI Taxonomy ID** | [{ncbi_tax}](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={ncbi_tax}) |" if ncbi_tax != NA else f"| **NCBI Taxonomy ID** | — |",
        f"| **Annotation version** | {version} |",
        f"| **Annotation pipeline** | {pipeline} — {pip_ver} |",
        f"| **Protein database** | {ref_db} — {ref_ver} |",
        f"| **BUSCO lineage** | {busco_lin} |",
        "",
        "## Assembly statistics",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Total length | {val(s, 'total_bp')} bp |",
        f"| Scaffolds | {val(s, 'scaffold_count')} |",
        f"| N50 | {val(s, 'N50')} bp |",
        f"| GC content | {pct(s, 'gc_pct')} |",
        f"| Soft-masked | {pct(s, 'soft_masked_pct')} |",
        "",
        "## Gene annotation statistics",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Genes | {val(s, 'genes')} |",
        f"| Average gene length | {val(s, 'average_gene_length')} bp |",
        f"| Transcripts per gene | {val(s, 'transcripts_per_gene', digits=2)} |",
        f"| Average transcript length | {val(s, 'average_transcript_length')} bp |",
        f"| Exons per transcript | {val(s, 'exons_per_transcript', digits=2)} |",
        f"| Average exon length | {val(s, 'average_exon_length')} bp |",
        f"| Average intron length | {val(s, 'avg_intron_length', digits=1)} bp |",
        f"| Single-exon transcripts | {val(s, 'single_exon_transcripts')} |",
        "",
        "## Repeat content",
        "",
        "| Class | % genome |",
        "|---|---|",
        f"| Retroelements | {pct(s, 'repeat_retroelements_pct')} |",
        f"| DNA transposons | {pct(s, 'repeat_dna_transposons_pct')} |",
        f"| Rolling circles | {pct(s, 'repeat_rolling_circles_pct')} |",
        f"| Unclassified | {pct(s, 'repeat_unclassified_pct')} |",
        f"| Simple repeats | {pct(s, 'repeat_simple_repeats_pct')} |",
        f"| **Total interspersed** | **{pct(s, 'repeat_total_interspersed_pct')}** |",
        f"| Soft-masked total | {pct(s, 'soft_masked_pct')} |",
        "",
        "## Annotation quality",
        "",
        "| Tool | Result |",
        "|---|---|",
        f"| BUSCO | {busco_line(s)} |",
        f"| OMARK completeness | {pct(s, 'omark_single_pct')} single, {pct(s, 'omark_duplicated_pct')} duplicated, {pct(s, 'omark_missing_pct')} missing |",
        f"| OMARK consistency | {pct(s, 'omark_consistent_pct')} consistent, {pct(s, 'omark_inconsistent_pct')} inconsistent, {pct(s, 'omark_unknown_pct')} unknown |",
        "",
        "## Functional annotation",
        "",
        "| Database | Coverage |",
        "|---|---|",
        f"| EggNOG-mapper | {pct(s, 'eggnog_annotated_pct')} annotated |",
        f"| GO terms (EggNOG) | {pct(s, 'eggnog_with_go_pct')} of proteins |",
        f"| KEGG KO | {pct(s, 'eggnog_with_kegg_ko_pct')} of proteins |",
        f"| COG categories | {pct(s, 'eggnog_with_cog_pct')} of proteins |",
        f"| InterProScan domains | {pct(s, 'iprscan_proteins_with_domain_pct')} of proteins |",
        "",
        "## Downloads",
        "",
        f"| Resource | Link |",
        "|---|---|",
        f"| Annotation files (this version, Zenodo) | {zen_link} |",
        f"| Assembly (ENA) | [{gid}]({ena_url(gid)}) |",
        f"| Assembly (NCBI) | [NCBI Datasets]({ncbi_url(gid)}) |",
        "",
        "### Files in this folder",
        "",
        "| File | Description |",
        "|---|---|",
        "| `annotation.gff3.gz` | Gene models (GFF3 format) |",
        "| `proteins.fa.gz` | Protein sequences (BRAKER3) |",
        "| `transcripts.fa.gz` | Coding sequences (BRAKER3) |",
        "| `eggnog.annotations.gz` | EggNOG-mapper functional annotation |",
        "| `interproscan.tsv.gz` | InterProScan protein domain annotation |",
        "| `repeatmasker.tbl` | RepeatMasker summary table |",
        "| `coding_region_stats.txt` | Gene / transcript statistics |",
        "| `busco_short_summary.txt` | BUSCO completeness summary |",
        "",
        "## Changelog",
        "",
        *changelog_lines,
        "## Citation",
        "",
        "If you use these annotations, please cite:",
        "",
        f"> Metz, S., Paulini, M., Rising, K. et al. Chromosome-level genomes of scleractinian corals: gene prediction and functional annotation. Sci Data (2026).",
        "",
        f">https://doi.org/10.1038/s41597-026-07499-3",
        "",
        f"> Zenodo: {zen_link}",
        "",
        "---",
        f"*README auto-generated on {date.today()} by generate_readmes.py*",
        "",
    ]

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Auto-generate per-genome README files for GitHub results/"
    )
    parser.add_argument("--project",  required=True,
                        help="Project root")
    parser.add_argument("--mapping",  required=True,
                        help="config/tolid_mapping.tsv")
    parser.add_argument("--summary",  required=True,
                        help="tables/genome_traits_summary.tsv")
    parser.add_argument("--manifest", required=True,
                        help="config/genomes.tsv")
    parser.add_argument("--version",  default="v2",
                        help="Annotation version label (default: v2)")
    parser.add_argument("--genome",   default=None,
                        help="Process only this genome_id_safe")
    args = parser.parse_args()

    mapping  = load_tsv(args.mapping,  "genome_id_safe")   # key: genome_id_safe
    summary  = load_tsv(args.summary,  "genome_id")        # key: genome_id_safe
    manifest = load_tsv(args.manifest, "genome_id")        # key: genome_id (with dot)

    # Build genome_id_safe → genome_id mapping from manifest
    safe_to_id = {}
    with open(args.manifest, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            safe_to_id[row["genome_id_safe"]] = row["genome_id"]

    results_base = os.path.join(args.project, "results")

    if args.genome:
        # Accept both dot format (GCA_964261235.1) and safe format (GCA_964261235_1)
        normalised = args.genome.replace(".", "_")
        if normalised not in mapping:
            sys.exit(f"ERROR: '{args.genome}' not found in tolid mapping "
                     f"(tried key '{normalised}')")
        genomes = [normalised]
    else:
        # Iterate over mapping keys (genome_id_safe, underscore format)
        # This avoids the mismatch with results/ directory names which use dots
        genomes = sorted(mapping.keys())

    ok = skipped = 0

    for gid_safe in genomes:

        tolid    = mapping[gid_safe]["tolid"]
        gid_dot  = safe_to_id.get(gid_safe)

        manifest_row = manifest.get(gid_dot, {}) if gid_dot else {}

        # summary is keyed by dot format (from compile_summary_table.py)
        # fall back to underscore format in case summary was generated differently
        stats_row = (summary.get(gid_dot)
                     or summary.get(gid_safe)
                     or {})

        if not manifest_row:
            print(f"  [WARN]  {gid_safe} — not in genomes.tsv, README will have gaps")

        # Get species name for folder naming
        species = manifest_row.get("tax_species", "unknown_species")
        species_folder = species.replace(" ", "_") if species != NA else "unknown_species"
        folder_name    = f"{tolid}_{species_folder}"
        folder_path    = os.path.join(args.project, "results", folder_name)

        # Also write to the genome_id_safe folder if it differs
        readme_dirs = [results_base]  # write to results/{tolid}_{species}/
        target_dir  = os.path.join(results_base, folder_name)
        os.makedirs(target_dir, exist_ok=True)

        readme_content = render_readme(manifest_row, stats_row, tolid, args.version)
        readme_path    = os.path.join(target_dir, "README.md")

        with open(readme_path, "w") as f:
            f.write(readme_content)

        print(f"  [OK]  {folder_name}")
        ok += 1

    print(f"\n  Generated: {ok}  |  Skipped: {skipped}")
    print(f"  Location : {results_base}/{{tolid}}_{{species}}/README.md")


if __name__ == "__main__":
    main()
