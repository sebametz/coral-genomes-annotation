# *Montipora indentata* — jaMonSpea1 / GCA_964205245.1

## Overview

| | |
|---|---|
| **Species** | *Montipora indentata* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964205245.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964205245.1) |
| **ToLID** | jaMonSpea1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [3154093](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3154093) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 818668351 bp |
| Scaffolds | 1076 |
| N50 | 49604136 bp |
| GC content | 39.74% |
| Soft-masked | 56.23% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 63391 |
| Average gene length | 4462 bp |
| Transcripts per gene | 1.12 |
| Average transcript length | 1081 bp |
| Exons per transcript | 4.13 |
| Average exon length | 261 bp |
| Average intron length | 1141.0 bp |
| Single-exon transcripts | 25720 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 19.85% |
| DNA transposons | 3.92% |
| Rolling circles | 0.33% |
| Unclassified | 30.48% |
| Simple repeats | 1.14% |
| **Total interspersed** | **54.25%** |
| Soft-masked total | 56.23% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:86.5% [S:77.9%, D:8.6%] F:7.4% M:6.1% (n=3203) |
| OMARK completeness | 80.25% single, 13.19% duplicated, 6.56% missing |
| OMARK consistency | 41.30% consistent, 11.95% inconsistent, 46.75% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 33.57% of proteins |
| KEGG KO | 40.39% of proteins |
| COG categories | 77.84% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964205245.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964205245.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964205245.1/) |

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
