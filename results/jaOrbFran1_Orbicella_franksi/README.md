# *Orbicella franksi* — jaOrbFran1 / GCA_964199315.1

## Overview

| | |
|---|---|
| **Species** | *Orbicella franksi* |
| **Family** | Merulinidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964199315.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964199315.1) |
| **ToLID** | jaOrbFran1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [48499](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=48499) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 496989174 bp |
| Scaffolds | 805 |
| N50 | 32264924 bp |
| GC content | 39.75% |
| Soft-masked | 50.50% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 27199 |
| Average gene length | 6636 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1458 bp |
| Exons per transcript | 7.00 |
| Average exon length | 208 bp |
| Average intron length | 972.3 bp |
| Single-exon transcripts | 9009 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 8.96% |
| DNA transposons | 4.20% |
| Rolling circles | 0.26% |
| Unclassified | 33.45% |
| Simple repeats | 1.01% |
| **Total interspersed** | **46.67%** |
| Soft-masked total | 50.50% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.7% [S:83.3%, D:15.4%] F:0.6% M:0.7% (n=3203) |
| OMARK completeness | 89.07% single, 8.57% duplicated, 2.36% missing |
| OMARK consistency | 67.58% consistent, 7.37% inconsistent, 25.05% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 52.97% of proteins |
| KEGG KO | 58.99% of proteins |
| COG categories | 91.28% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964199315.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964199315.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964199315.1/) |

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
