# *Dendrogyra cylindrus* — jaDenCyli1 / GCA_964187815.1

## Overview

| | |
|---|---|
| **Species** | *Dendrogyra cylindrus* |
| **Family** | Meandrinidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964187815.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964187815.1) |
| **ToLID** | jaDenCyli1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [214965](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=214965) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 560023380 bp |
| Scaffolds | 363 |
| N50 | 40517759 bp |
| GC content | 39.42% |
| Soft-masked | 54.59% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 29967 |
| Average gene length | 6906 bp |
| Transcripts per gene | 1.14 |
| Average transcript length | 1488 bp |
| Exons per transcript | 6.82 |
| Average exon length | 218 bp |
| Average intron length | 1048.4 bp |
| Single-exon transcripts | 10289 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 9.59% |
| DNA transposons | 9.20% |
| Rolling circles | 0.14% |
| Unclassified | 33.45% |
| Simple repeats | 1.00% |
| **Total interspersed** | **52.31%** |
| Soft-masked total | 54.59% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.6% [S:85.0%, D:13.6%] F:0.5% M:0.9% (n=3203) |
| OMARK completeness | 88.95% single, 8.91% duplicated, 2.14% missing |
| OMARK consistency | 66.88% consistent, 7.75% inconsistent, 25.37% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 50.39% of proteins |
| KEGG KO | 57.48% of proteins |
| COG categories | 90.55% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964187815.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964187815.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964187815.1/) |

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
