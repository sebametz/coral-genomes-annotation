# *Duncanopsammia axifuga* — jaDunAxif1 / GCA_964258685.1

## Overview

| | |
|---|---|
| **Species** | *Duncanopsammia axifuga* |
| **Family** | Dendrophylliidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964258685.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964258685.1) |
| **ToLID** | jaDunAxif1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [1479653](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1479653) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 673605476 bp |
| Scaffolds | 700 |
| N50 | 49606253 bp |
| GC content | 39.21% |
| Soft-masked | 60.35% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 30003 |
| Average gene length | 7414 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1431 bp |
| Exons per transcript | 6.57 |
| Average exon length | 217 bp |
| Average intron length | 1218.2 bp |
| Single-exon transcripts | 10953 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 8.86% |
| DNA transposons | 14.82% |
| Rolling circles | 0.91% |
| Unclassified | 34.48% |
| Simple repeats | 0.93% |
| **Total interspersed** | **58.31%** |
| Soft-masked total | 60.35% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.3% [S:83.5%, D:14.7%] F:0.7% M:1.1% (n=3203) |
| OMARK completeness | 88.12% single, 8.96% duplicated, 2.91% missing |
| OMARK consistency | 63.15% consistent, 9.08% inconsistent, 27.77% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 50.21% of proteins |
| KEGG KO | 56.43% of proteins |
| COG categories | 89.41% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964258685.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964258685.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964258685.1/) |

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
