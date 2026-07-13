#!/usr/bin/env python3
"""
populate_metadata.py
---------------------
Auto-populates provenance, specimen, and taxonomy columns in genomes.tsv
by querying NCBI Datasets API (assembly + biosample metadata) and the
Open Tree of Life API (OTT IDs).

Never overwrites an existing non-NA value — safe to re-run.

Sources:
  NCBI Datasets v2  → prov_bioproject, prov_biosample, tax_*, spec_*
  NCBI Taxonomy     → tax_class, tax_order, tax_family (parent ranks)
  Open Tree of Life → tax_ott_id
  Constants         → prov_publication_doi, prov_data_usage_policy,
                      prov_insdc_note

Usage:
    # dry-run — show what would change without writing
    python populate_metadata.py --manifest config/genomes.tsv --dry-run

    # populate all columns
    python populate_metadata.py --manifest config/genomes.tsv

    # single genome
    python populate_metadata.py --manifest config/genomes.tsv \\
        --genome GCA_964261235.1

    # skip OTT lookup (faster, use if OTT API is slow)
    python populate_metadata.py --manifest config/genomes.tsv --no-ott

Requirements:
    pip install requests pandas
"""

import argparse
import sys
import time
import pandas as pd
import requests

# ── Constants ─────────────────────────────────────────────────────────────────
# Values that are the same for every genome in this dataset.
# Edit before running if your dataset differs.

CONSTANTS = {
    "prov_publication_doi":  "10.1038/s41597-026-07499-3",
    "prov_data_usage_policy": "CC-BY-4.0",
    "prov_insdc_note":        "ENA primary",
    "prov_bioproject_parent": "PRJEB40665",   # ASG umbrella BioProject — verify
    "prov_annotation_pipeline": "BRAKER3",
}

NA_VALUES = {"NA", "nan", "", None}

NCBI_BASE = "https://api.ncbi.nlm.nih.gov/datasets/v2"
OTT_BASE  = "https://api.opentreeoflife.org/v3"

# Polite delay between API requests (seconds)
DELAY = 0.4


# ── Helpers ───────────────────────────────────────────────────────────────────

def is_na(v):
    return str(v).strip() in NA_VALUES or pd.isna(v)


def set_if_empty(row, col, value):
    """Set column value only if currently NA."""
    if col in row.index and not is_na(row[col]):
        return row   # already has a value — do not overwrite
    row[col] = str(value).strip() if value is not None else "NA"
    return row


def ncbi_get(endpoint, params=None, retries=3):
    url = f"{NCBI_BASE}{endpoint}"
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, timeout=15)
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 429:
                print(f"    Rate-limited — waiting 10s...")
                time.sleep(10)
        except requests.RequestException as e:
            print(f"    Network error: {e}")
        time.sleep(DELAY * (attempt + 1))
    return None


def ott_match(species_name):
    """Return OTT ID for a species name, or None."""
    try:
        r = requests.post(
            f"{OTT_BASE}/tnrs/match_names",
            json={"names": [species_name], "do_approximate_matching": False},
            timeout=10,
        )
        if r.status_code != 200:
            return None
        data = r.json()
        results = data.get("results", [])
        if not results:
            return None
        matches = results[0].get("matches", [])
        if not matches:
            return None
        # Return OTT ID of the best match
        return str(matches[0]["taxon"]["ott_id"])
    except Exception:
        return None


# ── NCBI Datasets: assembly report ───────────────────────────────────────────

def fetch_assembly_report(accession):
    """
    Fetch assembly metadata from NCBI Datasets v2.
    Returns dict with keys: bioproject, biosample, taxid, species_name,
                             collection_date, lat_lon, geo_loc, collected_by
    """
    clean_acc = accession.split(".")[0] + "." + accession.split(".")[1] \
        if "." in accession else accession

    data = ncbi_get(f"/genome/accession/{clean_acc}/dataset_report")
    if not data:
        return {}

    reports = data.get("reports", [])
    if not reports:
        return {}

    r = reports[0]
    info    = r.get("assembly_info", {})
    organism = r.get("organism", {})

    result = {
        "bioproject": info.get("bioproject_accession"),
        "biosample":  info.get("biosample_accession"),
        "taxid":      organism.get("tax_id"),
        "species_name": organism.get("organism_name"),
    }

    # BioSample attributes are sometimes embedded in the assembly report
    biosample_attrs = info.get("biosample", {}).get("attributes", [])
    attrs = {a["name"]: a["value"] for a in biosample_attrs}

    result.update({
        "collection_date": attrs.get("collection_date"),
        "lat_lon":         attrs.get("lat_lon"),
        "geo_loc":         attrs.get("geo_loc_name"),
        "collected_by":    attrs.get("collected_by"),
        "specimen_id":     attrs.get("specimen_voucher") or attrs.get("sample_name"),
    })

    return result


# ── NCBI Taxonomy: parent ranks ───────────────────────────────────────────────

RANK_COLS = {
    "class":  "tax_class",
    "order":  "tax_order",
    "family": "tax_family",
    "genus":  "tax_genus",
}

def fetch_taxonomy(taxid):
    """Return dict of rank→name for the given taxid."""
    data = ncbi_get(f"/taxonomy/taxon/{taxid}/dataset_report")
    if not data:
        return {}

    reports = data.get("reports", [])
    if not reports:
        return {}

    lineage = reports[0].get("taxonomy", {}).get("classification", {})
    result  = {}
    for rank, col in RANK_COLS.items():
        node = lineage.get(rank)
        if node:
            result[col] = node.get("name")
    return result


# ── Coordinate parser ─────────────────────────────────────────────────────────

def parse_lat_lon(lat_lon_str):
    """
    Parse NCBI lat_lon string e.g. '18.2871 S 147.6992 E'
    into (lat_float, lon_float) with correct signs.
    Returns (None, None) on failure.
    """
    if not lat_lon_str:
        return None, None
    try:
        parts = lat_lon_str.strip().split()
        if len(parts) >= 4:
            lat = float(parts[0]) * (-1 if parts[1].upper() == "S" else 1)
            lon = float(parts[2]) * (-1 if parts[3].upper() == "W" else 1)
            return lat, lon
        elif len(parts) == 2:   # already decimal degrees
            return float(parts[0]), float(parts[1])
    except (ValueError, IndexError):
        pass
    return None, None


# ── Main per-genome update ────────────────────────────────────────────────────

def update_genome(row, use_ott=True, dry_run=False):
    gid = row["genome_id"]

    if gid.startswith("TEMP_"):
        print(f"  [SKIP]  {gid} — temporary ID, no NCBI accession")
        return row, {}

    changes = {}

    # ── 1. Fill constants ──────────────────────────────────────────────────
    for col, val in CONSTANTS.items():
        if col in row.index and is_na(row[col]):
            changes[col] = val

    # ── 2. NCBI assembly report ────────────────────────────────────────────
    print(f"  [NCBI]  {gid}")
    assembly = fetch_assembly_report(gid)
    time.sleep(DELAY)

    if assembly.get("bioproject") and is_na(row.get("prov_bioproject")):
        changes["prov_bioproject"] = assembly["bioproject"]

    if assembly.get("biosample") and is_na(row.get("prov_biosample")):
        changes["prov_biosample"] = assembly["biosample"]

    if assembly.get("taxid") and is_na(row.get("tax_ncbi_taxid")):
        changes["tax_ncbi_taxid"] = str(assembly["taxid"])

    if assembly.get("species_name") and is_na(row.get("tax_species")):
        parts = assembly["species_name"].split()
        if len(parts) >= 2:
            changes["tax_species"] = " ".join(parts[:2])
            if is_na(row.get("tax_genus")):
                changes["tax_genus"] = parts[0]

    # Specimen from BioSample attributes
    if assembly.get("collection_date") and is_na(row.get("spec_collection_date")):
        changes["spec_collection_date"] = assembly["collection_date"]

    if assembly.get("geo_loc") and is_na(row.get("spec_site_name")):
        changes["spec_site_name"] = assembly["geo_loc"]

    if assembly.get("lat_lon"):
        lat, lon = parse_lat_lon(assembly["lat_lon"])
        if lat is not None and is_na(row.get("spec_lat")):
            changes["spec_lat"] = str(lat)
        if lon is not None and is_na(row.get("spec_lon")):
            changes["spec_lon"] = str(lon)

    if assembly.get("collected_by") and is_na(row.get("spec_collector")):
        changes["spec_collector"] = assembly["collected_by"]

    if assembly.get("specimen_id") and is_na(row.get("spec_specimen_id")):
        changes["spec_specimen_id"] = assembly["specimen_id"]

    # ── 3. NCBI Taxonomy for parent ranks ─────────────────────────────────
    taxid = changes.get("tax_ncbi_taxid") or str(row.get("tax_ncbi_taxid", ""))
    if taxid and taxid not in NA_VALUES:
        tax = fetch_taxonomy(taxid)
        time.sleep(DELAY)
        for col, val in tax.items():
            if val and is_na(row.get(col)):
                changes[col] = val

    # ── 4. Open Tree of Life OTT ID ───────────────────────────────────────
    if use_ott and is_na(row.get("tax_ott_id")):
        species = changes.get("tax_species") or str(row.get("tax_species", ""))
        if species and species not in NA_VALUES:
            print(f"    [OTT]   {species}")
            ott = ott_match(species)
            time.sleep(DELAY)
            if ott:
                changes["tax_ott_id"] = ott

    return row, changes


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Auto-populate genomes.tsv from NCBI and OTT APIs"
    )
    parser.add_argument("--manifest", required=True, help="Path to config/genomes.tsv")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Show changes without writing to file")
    parser.add_argument("--no-ott",   action="store_true",
                        help="Skip Open Tree of Life OTT ID lookup")
    parser.add_argument("--genome",   default=None,
                        help="Process only this genome_id")
    args = parser.parse_args()

    df = pd.read_csv(args.manifest, sep="\t", dtype=str)
    df = df.loc[:, ~df.columns.duplicated()]   # remove duplicate columns
    df = df.fillna("NA")

    if args.genome:
        rows = df[df["genome_id"] == args.genome]
        if rows.empty:
            sys.exit(f"ERROR: genome_id '{args.genome}' not found")
        indices = rows.index.tolist()
    else:
        indices = df.index.tolist()

    print(f"\nProcessing {len(indices)} genome(s) "
          f"{'[DRY-RUN]' if args.dry_run else ''}\n")

    total_changes = 0

    for idx in indices:
        row, changes = update_genome(
            df.loc[idx].copy(),
            use_ott=not args.no_ott,
            dry_run=args.dry_run,
        )

        if changes:
            for col, val in changes.items():
                print(f"    {col}: NA → {val}")
            if not args.dry_run:
                for col, val in changes.items():
                    df.at[idx, col] = val
            total_changes += len(changes)
        else:
            print(f"    (no changes)")

    if not args.dry_run:
        df.to_csv(args.manifest, sep="\t", index=False)
        print(f"\nWritten → {args.manifest}")

    print(f"\nTotal changes: {total_changes}")
    if args.dry_run:
        print("Re-run without --dry-run to apply.")


if __name__ == "__main__":
    main()
