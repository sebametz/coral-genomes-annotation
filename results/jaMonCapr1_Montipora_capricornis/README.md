# *Montipora capricornis* — jaMonCapr1 / GCA_965112405.1

## Overview

| | |
|---|---|
| **Species** | *Montipora capricornis* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_965112405.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965112405.1) |
| **ToLID** | jaMonCapr1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [246305](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=246305) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 716402913 bp |
| Scaffolds | 864 |
| N50 | 48485938 bp |
| GC content | 39.60% |
| Soft-masked | 57.57% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 33322 |
| Average gene length | 7748 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1287 bp |
| Exons per transcript | 5.87 |
| Average exon length | 219 bp |
| Average intron length | 1514.8 bp |
| Single-exon transcripts | 14045 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 19.59% |
| DNA transposons | 4.92% |
| Rolling circles | 0.25% |
| Unclassified | 31.47% |
| Simple repeats | 0.82% |
| **Total interspersed** | **56.12%** |
| Soft-masked total | 57.57% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.0% [S:81.4%, D:16.6%] F:0.5% M:1.5% (n=3203) |
| OMARK completeness | 88.49% single, 7.75% duplicated, 3.76% missing |
| OMARK consistency | 54.77% consistent, 9.22% inconsistent, 36.01% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 46.64% of proteins |
| KEGG KO | 51.88% of proteins |
| COG categories | 85.86% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_965112405.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965112405.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965112405.1/) |

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
