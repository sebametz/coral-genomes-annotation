# *Galaxea sp.* — jaGalFasc40 / GCA_948470475.1

## Overview

| | |
|---|---|
| **Species** | *Galaxea sp.* |
| **Family** | Euphylliidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_948470475.1](https://www.ebi.ac.uk/ena/browser/view/GCA_948470475.1) |
| **ToLID** | jaGalFasc40 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [46745](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=46745) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2];  RNA: ERR10378011 — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 416866986 bp |
| Scaffolds | 178 |
| N50 | 33853504 bp |
| GC content | 39.80% |
| Soft-masked | 48.09% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 26121 |
| Average gene length | 6465 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1378 bp |
| Exons per transcript | 6.48 |
| Average exon length | 212 bp |
| Average intron length | 1053.9 bp |
| Single-exon transcripts | 9365 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 11.97% |
| DNA transposons | 4.86% |
| Rolling circles | 0.35% |
| Unclassified | 29.54% |
| Simple repeats | 0.87% |
| **Total interspersed** | **46.51%** |
| Soft-masked total | 48.09% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:93.7% [S:78.4%, D:15.3%] F:0.9% M:5.4% (n=3203) |
| OMARK completeness | 86.64% single, 6.51% duplicated, 6.85% missing |
| OMARK consistency | 61.61% consistent, 8.21% inconsistent, 30.18% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 50.48% of proteins |
| KEGG KO | 55.32% of proteins |
| COG categories | 88.36% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_948470475.1](https://www.ebi.ac.uk/ena/browser/view/GCA_948470475.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_948470475.1/) |

### Files in this folder

| File | Description |
|---|---|
| `annotation.gff3.gz` | Gene models (GFF3 format) |
| `proteins.fa.gz` | Protein sequences (BRAKER3) |
| `transcripts.fa.gz` | Coding sequences (BRAKER3) |
| `eggnog.annotations.gz` | EggNOG-mapper functional annotation |
| `interproscan.tsv.gz` | InterProScan protein domain annotation |
| `repeatmasker.tbl` | RepeatMasker summary table |
| `coding_region_stats.txt` | Gene / transcript statistics |
| `busco_short_summary.txt` | BUSCO completeness summary |

## Changelog

**v2.0**
*  Extended dataset from 40 to 95 genomes
*  Two-pass BRAKER3 gene prediction pipeline (with RNA-seq, when available, and protein evidence)
*  New proteome database for first annotation including OrthoDB v12 Cnidaria, plus predicted proteins from V1 genome annotations
*  Genomes without RNA-seq data, BRAKER3 in protein-only mode for those
*  Added InterProScan protein domain annotation
*  Added intron statistics
*  Re-ran BUSCO quality assessment with cnidaria_odb12 lineage
*  Re-ran OMARK annotation quality assessment
*  Re-ran EggNOG-mapper with updated database
*  Standardised file naming and folder structure

**v1.0**
*  Initial release: 40 genomes, 22 genera, 13 families
*  BRAKER3 gene prediction pipeline
*  BUSCO quality assessment
*  EggNOG-mapper functional annotation
*  RepeatModeler/RepeatMasker repeat annotation

## Citation

If you use these annotations, please cite:

> Metz, S., Paulini, M., Rising, K. et al. Chromosome-level genomes of scleractinian corals: gene prediction and functional annotation. Sci Data (2026).

>https://doi.org/10.1038/s41597-026-07499-3

> Zenodo: [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096)

---
*README auto-generated on 2026-07-13 by generate_readmes.py*
