# *Diploria labyrinthiformis* — jaDipLaby1 / GCA_965282425.1

## Overview

| | |
|---|---|
| **Species** | *Diploria labyrinthiformis* |
| **Family** | Faviidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_965282425.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965282425.1) |
| **ToLID** | jaDipLaby1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [242715](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=242715) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 388238899 bp |
| Scaffolds | 1112 |
| N50 | 5893000 bp |
| GC content | 38.93% |
| Soft-masked | 43.97% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 25278 |
| Average gene length | 6521 bp |
| Transcripts per gene | 1.16 |
| Average transcript length | 1561 bp |
| Exons per transcript | 7.54 |
| Average exon length | 207 bp |
| Average intron length | 876.6 bp |
| Single-exon transcripts | 7788 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 10.13% |
| DNA transposons | 5.70% |
| Rolling circles | 0.55% |
| Unclassified | 25.76% |
| Simple repeats | 0.81% |
| **Total interspersed** | **41.59%** |
| Soft-masked total | 43.97% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:97.2% [S:83.1%, D:14.0%] F:1.1% M:1.7% (n=3203) |
| OMARK completeness | 88.97% single, 8.45% duplicated, 2.57% missing |
| OMARK consistency | 69.09% consistent, 7.33% inconsistent, 23.58% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 54.10% of proteins |
| KEGG KO | 59.57% of proteins |
| COG categories | 91.82% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_965282425.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965282425.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965282425.1/) |

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
