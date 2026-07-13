# *Stylophora pistillata* — jaStyPist1 / GCA_964205215.1

## Overview

| | |
|---|---|
| **Species** | *Stylophora pistillata* |
| **Family** | Pocilloporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964205215.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964205215.1) |
| **ToLID** | jaStyPist1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [50429](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=50429) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 560638484 bp |
| Scaffolds | 227 |
| N50 | 37068110 bp |
| GC content | 39.62% |
| Soft-masked | 52.07% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 33431 |
| Average gene length | 5605 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1420 bp |
| Exons per transcript | 6.65 |
| Average exon length | 213 bp |
| Average intron length | 848.8 bp |
| Single-exon transcripts | 11803 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 14.82% |
| DNA transposons | 5.09% |
| Rolling circles | 0.19% |
| Unclassified | 30.90% |
| Simple repeats | 0.82% |
| **Total interspersed** | **50.81%** |
| Soft-masked total | 52.07% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:99.0% [S:83.5%, D:15.5%] F:0.3% M:0.7% (n=3203) |
| OMARK completeness | 86.54% single, 12.22% duplicated, 1.24% missing |
| OMARK consistency | 66.83% consistent, 6.86% inconsistent, 26.30% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 47.63% of proteins |
| KEGG KO | 53.80% of proteins |
| COG categories | 90.54% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964205215.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964205215.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964205215.1/) |

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
