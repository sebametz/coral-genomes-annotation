#!/usr/bin/env python3
"""
parse_repeatmasker_tbl.py  v2
------------------------------
Parses a RepeatMasker .tbl file into a flat TSV preserving the full
classification hierarchy.

Output columns:
  genome_id | section | level | parent | name |
  element_count | length_bp | pct_of_genome | is_total

section  : RETROELEMENTS | DNA_TRANSPOSONS | TANDEM_SIMPLE | SUMMARY
level    : 0 (top) 1 (subcategory) 2 (sub-sub) 3 (deepest)
parent   : name of parent element, or NA for top-level
is_total : true for summary lines

Indentation → level mapping (RepeatMasker uses inconsistent spaces at level 2):
  0 spaces  → level 0   top-level categories
  1-3 spaces → level 1   direct subcategories
  4-6 spaces → level 2   sub-subcategories (4 OR 5 spaces, treated as siblings)
  7+ spaces  → level 3   deepest (e.g. Retroviral under Gypsy/DIRS1)
"""

import argparse
import csv
import os
import re
import sys

# ── Patterns ─────────────────────────────────────────────────────────────────

# Data line: spaces + name + 2+spaces + count + bp + pct
# Key: (.+?) non-greedy, stops at first 2+ space gap → handles names with digits/symbols
RE_DATA = re.compile(
    r"^(\s*)"
    r"(.+?)"
    r"\s{2,}"
    r"([\d,]+)\s+"
    r"([\d,]+)\s+bp\s+"
    r"([\d.]+)\s+%"
)

RE_INTERSPERSED = re.compile(
    r"Total interspersed repeats:\s+([\d,]+)\s+bp\s+([\d.]+)\s+%"
)
RE_MASKED  = re.compile(r"bases masked:\s+([\d,]+)\s+bp\s+\(\s*([\d.]+)\s+%\)")
RE_TOTAL   = re.compile(r"total length:\s+([\d,]+)\s+bp\s+\(([\d,]+)\s+bp\s+excl")
RE_GC      = re.compile(r"GC level:\s+([\d.]+)\s+%")
RE_SEQS    = re.compile(r"sequences:\s+([\d,]+)")

# Bottom section names (no indent but NOT top-level repeat categories)
BOTTOM_NAMES = {"small rna", "satellites", "simple repeats", "low complexity"}

# ── Helpers ───────────────────────────────────────────────────────────────────

def clean_int(s):  return int(s.replace(",", ""))
def clean_name(s): return s.strip().rstrip(":")

def spaces_to_level(n):
    """Bin raw space count to a normalised level 0-3."""
    if n == 0:   return 0
    if n <= 3:   return 1
    if n <= 6:   return 2
    return 3

# ── Parser ───────────────────────────────────────────────────────────────────

def parse_tbl(path, genome_id):
    header = {}
    rows   = []

    parent_stack = []   # list of (level, name) — tracks ancestry
    section      = "RETROELEMENTS"
    skip_next    = False   # for multi-line name continuations

    with open(path) as f:
        lines = f.readlines()

    for i, raw in enumerate(lines):

        # Skip the continuation line of multi-line entries (e.g. "P-element, Transib)")
        if skip_next:
            skip_next = False
            continue

        line = raw.rstrip()

        # ── Header ──────────────────────────────────────────────────────────
        m = RE_SEQS.search(line)
        if m: header["sequences"] = clean_int(m.group(1)); continue

        m = RE_TOTAL.search(line)
        if m:
            header["total_bp"] = clean_int(m.group(1))
            header["total_bp_excl_n"] = clean_int(m.group(2)); continue

        m = RE_GC.search(line)
        if m: header["gc_pct"] = float(m.group(1)); continue

        m = RE_MASKED.search(line)
        if m:
            header["masked_bp"]  = clean_int(m.group(1))
            header["masked_pct"] = float(m.group(2)); continue

        # ── Summary line (no element count column) ────────────────────────
        m = RE_INTERSPERSED.search(line)
        if m:
            rows.append({
                "genome_id":     genome_id,
                "section":       "SUMMARY",
                "level":         0,
                "parent":        "NA",
                "name":          "Total interspersed repeats",
                "element_count": "NA",
                "length_bp":     clean_int(m.group(1)),
                "pct_of_genome": float(m.group(2)),
                "is_total":      "true",
            })
            continue

        # ── Skip non-data lines ───────────────────────────────────────────
        stripped = line.strip()
        if not stripped: continue
        if re.match(r"^[=\-\*]", stripped): continue
        if re.match(r"(number|file name|RepeatMasker|run with|The query|FamDB|most repeat)",
                    stripped, re.I): continue

        # ── Parse data line ───────────────────────────────────────────────
        m = RE_DATA.match(line)
        if not m:
            continue

        spaces = len(m.group(1))
        name   = clean_name(m.group(2))
        count  = clean_int(m.group(3))
        bp     = clean_int(m.group(4))
        pct    = float(m.group(5))

        # Handle multi-line names: "Other (Mirage," → peek at next line
        if name.endswith(",") or name.endswith("("):
            if i + 1 < len(lines):
                cont = lines[i + 1].strip().rstrip(")")
                name = name + " " + cont + ")"
                skip_next = True
            name = clean_name(name)

        # ── Level and parent ──────────────────────────────────────────────
        lvl = spaces_to_level(spaces)

        # Pop stack until top is strictly shallower than current level
        while parent_stack and parent_stack[-1][0] >= lvl:
            parent_stack.pop()
        parent = parent_stack[-1][1] if parent_stack else "NA"
        parent_stack.append((lvl, name))

        # ── Section detection ─────────────────────────────────────────────
        name_lower = name.lower().rstrip(":")
        if lvl == 0:
            if "dna transposon" in name_lower:
                section = "DNA_TRANSPOSONS"
            elif "rolling" in name_lower or "unclassified" in name_lower:
                section = "RETROELEMENTS"   # keep in main section
            elif name_lower in BOTTOM_NAMES or "small rna" in name_lower:
                section = "TANDEM_SIMPLE"

        rows.append({
            "genome_id":     genome_id,
            "section":       section,
            "level":         lvl,
            "parent":        parent,
            "name":          name,
            "element_count": count,
            "length_bp":     bp,
            "pct_of_genome": pct,
            "is_total":      "false",
        })

    return header, rows

# ── Output ────────────────────────────────────────────────────────────────────

FIELDNAMES = [
    "genome_id", "section", "level", "parent", "name",
    "element_count", "length_bp", "pct_of_genome", "is_total",
]

def write_tsv(rows, path):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Parse RepeatMasker .tbl to TSV")
    group  = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--tbl",      help="Single .tbl file")
    group.add_argument("--manifest", help="config/genomes.tsv (batch mode)")
    parser.add_argument("--genome-id", help="genome_id for single mode")
    parser.add_argument("--out",       help="Output TSV path")
    args = parser.parse_args()

    if args.tbl:
        gid = args.genome_id or os.path.basename(args.tbl).replace(".tbl", "")
        header, rows = parse_tbl(args.tbl, gid)
        out = args.out or f"{gid}_repeats.tsv"
        write_tsv(rows, out)

        print(f"\nHeader stats for {gid}:")
        for k, v in header.items():
            print(f"  {k:<22} {v}")

        print(f"\nHierarchy ({len(rows)} rows):")
        for r in rows:
            indent = "  " * r["level"]
            tag = "[TOTAL]" if r["is_total"] == "true" else ""
            print(f"  {indent}[{r['section']:<16}] L{r['level']} "
                  f"parent={r['parent']:<22} {r['name']} "
                  f"  n={r['element_count']}  {r['pct_of_genome']}% {tag}")
        print(f"\nWritten → {out}")
        return

    # ── Batch ────────────────────────────────────────────────────────────
    if not args.out:
        sys.exit("ERROR: --out required in batch mode")
    if not os.path.isfile(args.manifest):
        sys.exit(f"ERROR: manifest not found: {args.manifest}")

    with open(args.manifest, newline="") as f:
        manifest_rows = list(csv.DictReader(f, delimiter="\t"))

    all_rows = []
    ok = skipped = errors = 0

    for row in manifest_rows:
        gid  = row["genome_id"]
        path = row.get("path_repeatmasker_tbl", "NA").strip()
        if path in ("NA", ""):
            print(f"  [SKIP]  {gid}")
            skipped += 1; continue
        try:
            _, rows = parse_tbl(path, gid)
            all_rows.extend(rows)
            print(f"  [OK]    {gid}  ({len(rows)} elements)")
            ok += 1
        except Exception as e:
            print(f"  [ERROR] {gid}: {e}")
            errors += 1

    write_tsv(all_rows, args.out)
    print(f"\n{len(all_rows)} rows written → {args.out}")
    print(f"  OK: {ok}  Skipped: {skipped}  Errors: {errors}")

if __name__ == "__main__":
    main()

