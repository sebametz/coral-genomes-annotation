# *Acropora spathulata* — jaAcrSpat14 / GCA_964019555.1

## Overview

| | |
|---|---|
| **Species** | *Acropora spathulata* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964019555.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964019555.1) |
| **ToLID** | jaAcrSpat14 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [141011](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=141011) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 486213471 bp |
| Scaffolds | 464 |
| N50 | 32720690 bp |
| GC content | 39.05% |
| Soft-masked | 55.33% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 29094 |
| Average gene length | 5716 bp |
| Transcripts per gene | 1.17 |
| Average transcript length | 1404 bp |
| Exons per transcript | 6.64 |
| Average exon length | 211 bp |
| Average intron length | 889.5 bp |
| Single-exon transcripts | 10825 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 16.69% |
| DNA transposons | 4.04% |
| Rolling circles | 0.36% |
| Unclassified | 32.86% |
| Simple repeats | 0.71% |
| **Total interspersed** | **54.01%** |
| Soft-masked total | 55.33% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.4% [S:81.0%, D:17.5%] F:0.8% M:0.8% (n=3203) |
| OMARK completeness | 88.37% single, 7.82% duplicated, 3.81% missing |
| OMARK consistency | 59.64% consistent, 8.86% inconsistent, 31.49% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 49.10% of proteins |
| KEGG KO | 53.42% of proteins |
| COG categories | 87.50% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964019555.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964019555.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964019555.1/) |

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
