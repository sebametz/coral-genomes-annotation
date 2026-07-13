# *Caulastraea furcata* — jaCauFurc1 / GCA_965607595.1

## Overview

| | |
|---|---|
| **Species** | *Caulastraea furcata* |
| **Family** | Merulinidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_965607595.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965607595.1) |
| **ToLID** | jaCauFurc1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [46696](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=46696) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 830821469 bp |
| Scaffolds | 1860 |
| N50 | 31854290 bp |
| GC content | 39.24% |
| Soft-masked | 61.21% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 35783 |
| Average gene length | 7132 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1287 bp |
| Exons per transcript | 5.39 |
| Average exon length | 238 bp |
| Average intron length | 1484.6 bp |
| Single-exon transcripts | 14762 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 15.20% |
| DNA transposons | 7.10% |
| Rolling circles | 0.21% |
| Unclassified | 37.17% |
| Simple repeats | 1.06% |
| **Total interspersed** | **59.48%** |
| Soft-masked total | 61.21% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:95.2% [S:79.8%, D:15.5%] F:1.8% M:3.0% (n=3203) |
| OMARK completeness | 84.96% single, 10.86% duplicated, 4.18% missing |
| OMARK consistency | 59.79% consistent, 8.89% inconsistent, 31.32% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 45.28% of proteins |
| KEGG KO | 52.34% of proteins |
| COG categories | 85.37% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_965607595.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965607595.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965607595.1/) |

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
