# *Montipora palawanensis* — jaMonPala3 / GCA_964330385.1

## Overview

| | |
|---|---|
| **Species** | *Montipora palawanensis* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964330385.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964330385.1) |
| **ToLID** | jaMonPala3 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [3109268](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3109268) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 774819882 bp |
| Scaffolds | 145 |
| N50 | 51362878 bp |
| GC content | 39.59% |
| Soft-masked | 59.61% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 38841 |
| Average gene length | 6850 bp |
| Transcripts per gene | 1.14 |
| Average transcript length | 1236 bp |
| Exons per transcript | 5.37 |
| Average exon length | 230 bp |
| Average intron length | 1467.6 bp |
| Single-exon transcripts | 15158 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 20.17% |
| DNA transposons | 4.86% |
| Rolling circles | 0.26% |
| Unclassified | 33.03% |
| Simple repeats | 0.85% |
| **Total interspersed** | **58.16%** |
| Soft-masked total | 59.61% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:96.5% [S:80.0%, D:16.6%] F:1.2% M:2.3% (n=3203) |
| OMARK completeness | 80.79% single, 12.97% duplicated, 6.24% missing |
| OMARK consistency | 44.37% consistent, 12.49% inconsistent, 43.15% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 33.59% of proteins |
| KEGG KO | 39.99% of proteins |
| COG categories | 77.64% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964330385.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964330385.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964330385.1/) |

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
