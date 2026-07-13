# *Isopora aff. cuneata* — jaIsoPali11 / GCA_964212065.1

## Overview

| | |
|---|---|
| **Species** | *Isopora aff. cuneata* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964212065.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964212065.1) |
| **ToLID** | jaIsoPali11 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [105615](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=105615) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2];  RNA: ERR16828706 — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 482731129 bp |
| Scaffolds | 270 |
| N50 | 36807548 bp |
| GC content | 38.97% |
| Soft-masked | 53.41% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 24065 |
| Average gene length | 5341 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1297 bp |
| Exons per transcript | 6.22 |
| Average exon length | 208 bp |
| Average intron length | 847.4 bp |
| Single-exon transcripts | 8803 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 11.16% |
| DNA transposons | 5.15% |
| Rolling circles | 0.23% |
| Unclassified | 35.35% |
| Simple repeats | 0.80% |
| **Total interspersed** | **51.95%** |
| Soft-masked total | 53.41% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:92.5% [S:78.5%, D:14.0%] F:1.7% M:5.7% (n=3203) |
| OMARK completeness | 83.75% single, 8.23% duplicated, 8.02% missing |
| OMARK consistency | 62.71% consistent, 8.13% inconsistent, 29.17% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 53.70% of proteins |
| KEGG KO | 57.15% of proteins |
| COG categories | 89.75% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964212065.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964212065.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964212065.1/) |

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
