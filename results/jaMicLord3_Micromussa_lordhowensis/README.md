# *Micromussa lordhowensis* — jaMicLord3 / GCA_964020085.1

## Overview

| | |
|---|---|
| **Species** | *Micromussa lordhowensis* |
| **Family** | Lobophylliidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964020085.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964020085.1) |
| **ToLID** | jaMicLord3 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [1216036](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1216036) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 582095087 bp |
| Scaffolds | 1615 |
| N50 | 37782130 bp |
| GC content | 39.95% |
| Soft-masked | 52.28% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 34954 |
| Average gene length | 5780 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1284 bp |
| Exons per transcript | 5.72 |
| Average exon length | 224 bp |
| Average intron length | 1070.4 bp |
| Single-exon transcripts | 14277 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 12.21% |
| DNA transposons | 6.18% |
| Rolling circles | 0.37% |
| Unclassified | 32.25% |
| Simple repeats | 0.74% |
| **Total interspersed** | **50.66%** |
| Soft-masked total | 52.28% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:96.8% [S:81.2%, D:15.6%] F:1.5% M:1.8% (n=3203) |
| OMARK completeness | 87.42% single, 9.55% duplicated, 3.04% missing |
| OMARK consistency | 59.03% consistent, 9.10% inconsistent, 31.87% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 45.05% of proteins |
| KEGG KO | 51.86% of proteins |
| COG categories | 84.21% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964020085.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964020085.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964020085.1/) |

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
