# *Acropora cf. manni* — jaAcrPulc1 / GCA_965118205.1

## Overview

| | |
|---|---|
| **Species** | *Acropora cf. manni* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_965118205.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965118205.1) |
| **ToLID** | jaAcrPulc1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [3471590](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3471590) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2]; RNA: ERR15140919 — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 459279821 bp |
| Scaffolds | 1340 |
| N50 | 30835548 bp |
| GC content | 39.05% |
| Soft-masked | 50.05% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 28136 |
| Average gene length | 5876 bp |
| Transcripts per gene | 1.17 |
| Average transcript length | 1438 bp |
| Exons per transcript | 6.77 |
| Average exon length | 212 bp |
| Average intron length | 894.1 bp |
| Single-exon transcripts | 10308 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 13.22% |
| DNA transposons | 4.41% |
| Rolling circles | 0.55% |
| Unclassified | 29.56% |
| Simple repeats | 0.73% |
| **Total interspersed** | **47.88%** |
| Soft-masked total | 50.05% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:97.8% [S:81.1%, D:16.6%] F:0.5% M:1.7% (n=3203) |
| OMARK completeness | 88.51% single, 7.38% duplicated, 4.10% missing |
| OMARK consistency | 60.87% consistent, 9.22% inconsistent, 29.91% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 49.10% of proteins |
| KEGG KO | 53.13% of proteins |
| COG categories | 88.32% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_965118205.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965118205.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965118205.1/) |

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
