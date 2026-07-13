#!/usr/bin/env python3
"""
calc_intron_stats.py
--------------------
Derives intron statistics from a GFF3 annotation file.
Introns = gaps between consecutive exons within the same transcript.

Output format matches stats.txt so both can be parsed by the same script.

Usage:
    python calc_intron_stats.py annotation.gff3
    python calc_intron_stats.py annotation.gff3 --out intron_stats.txt
    python calc_intron_stats.py annotation.gff  # .gff works too
"""

import argparse
import statistics
import sys
from collections import defaultdict


def parse_gff(path):
    """
    Returns a dict: transcript_id -> sorted list of (start, end) exon tuples.
    Coordinates are kept 1-based as in the GFF.
    """
    exons = defaultdict(list)

    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue

            parts = line.rstrip("\n").split("\t")
            if len(parts) < 9:
                continue

            feature = parts[2]
            if feature != "exon":
                continue

            start  = int(parts[3])
            end    = int(parts[4])
            attrs  = parts[8]

            # Parse Parent= from attributes
            parent = None
            for field in attrs.split(";"):
                field = field.strip()
                if field.lower().startswith("parent="):
                    parent = field.split("=", 1)[1].strip()
                    # take first parent if comma-separated
                    parent = parent.split(",")[0]
                    break

            if parent:
                exons[parent].append((start, end))

    # Sort each transcript's exons by start position
    for tx in exons:
        exons[tx].sort()

    return exons


def calc_introns(exons_by_tx):
    """
    Given exons per transcript, derive intron lengths.
    Returns per-transcript intron lists and flat list of all intron lengths.
    """
    all_intron_lengths = []
    introns_per_tx     = []   # number of introns per transcript
    single_exon        = 0

    for tx_id, exon_list in exons_by_tx.items():
        if len(exon_list) < 2:
            single_exon += 1
            introns_per_tx.append(0)
            continue

        tx_introns = []
        for i in range(1, len(exon_list)):
            # intron = gap between end of exon[i-1] and start of exon[i]
            intron_start = exon_list[i - 1][1] + 1
            intron_end   = exon_list[i][0] - 1
            length       = intron_end - intron_start + 1
            if length > 0:
                tx_introns.append(length)

        introns_per_tx.append(len(tx_introns))
        all_intron_lengths.extend(tx_introns)

    return all_intron_lengths, introns_per_tx, single_exon


def main():
    parser = argparse.ArgumentParser(
        description="Calculate intron statistics from a GFF3 file"
    )
    parser.add_argument("gff", help="Path to GFF3 annotation file")
    parser.add_argument("--out", help="Output file (default: print to stdout)")
    args = parser.parse_args()

    print(f"Parsing {args.gff}...", file=sys.stderr)
    exons_by_tx = parse_gff(args.gff)

    if not exons_by_tx:
        sys.exit("ERROR: no exon features found. Check GFF feature type is 'exon'.")

    n_transcripts = len(exons_by_tx)
    print(f"Transcripts with exons: {n_transcripts}", file=sys.stderr)

    all_introns, introns_per_tx, single_exon = calc_introns(exons_by_tx)

    if not all_introns:
        sys.exit("ERROR: no introns found. All transcripts appear to be single-exon.")

    lines = [
        f"transcripts_total: {n_transcripts}",
        f"single_exon_transcripts: {single_exon}",
        f"multi_exon_transcripts: {n_transcripts - single_exon}",
        f"introns_total: {len(all_introns)}",
        f"avg_introns_per_transcript: {round(statistics.mean(introns_per_tx), 4)}",
        f"avg_intron_length: {round(statistics.mean(all_introns), 4)}",
        f"median_intron_length: {round(statistics.median(all_introns), 4)}",
        f"min_intron_length: {min(all_introns)}",
        f"max_intron_length: {max(all_introns)}",
        f"stdev_intron_length: {round(statistics.stdev(all_introns), 4)}",
    ]

    output = "\n".join(lines) + "\n"

    if args.out:
        with open(args.out, "w") as f:
            f.write(output)
        print(f"Written → {args.out}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
