# *Siderastrea siderea* — jaSidSide1 / GCA_964030785.1

## Overview

| | |
|---|---|
| **Species** | *Siderastrea siderea* |
| **Family** | Rhizangiidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964030785.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964030785.1) |
| **ToLID** | jaSidSide1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [130672](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=130672) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 831122133 bp |
| Scaffolds | 450 |
| N50 | 56755662 bp |
| GC content | 39.80% |
| Soft-masked | 54.76% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 41798 |
| Average gene length | 6003 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1266 bp |
| Exons per transcript | 5.34 |
| Average exon length | 236 bp |
| Average intron length | 1236.4 bp |
| Single-exon transcripts | 18689 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 10.07% |
| DNA transposons | 8.90% |
| Rolling circles | 0.07% |
| Unclassified | 34.29% |
| Simple repeats | 1.12% |
| **Total interspersed** | **53.35%** |
| Soft-masked total | 54.76% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.0% [S:82.1%, D:15.9%] F:1.0% M:1.0% (n=3203) |
| OMARK completeness | 87.25% single, 9.81% duplicated, 2.94% missing |
| OMARK consistency | 56.05% consistent, 9.03% inconsistent, 34.92% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 44.45% of proteins |
| KEGG KO | 51.39% of proteins |
| COG categories | 85.09% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964030785.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964030785.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964030785.1/) |

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
