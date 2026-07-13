# *Madracis auretenra* — jaMadAure2 / GCA_964059495.1

## Overview

| | |
|---|---|
| **Species** | *Madracis auretenra* |
| **Family** | Pocilloporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964059495.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964059495.1) |
| **ToLID** | jaMadAure2 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [999287](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=999287) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 521681634 bp |
| Scaffolds | 390 |
| N50 | 37320567 bp |
| GC content | 38.51% |
| Soft-masked | 50.48% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 28418 |
| Average gene length | 6245 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1368 bp |
| Exons per transcript | 6.21 |
| Average exon length | 220 bp |
| Average intron length | 1036.7 bp |
| Single-exon transcripts | 9992 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 8.99% |
| DNA transposons | 4.37% |
| Rolling circles | 0.16% |
| Unclassified | 34.12% |
| Simple repeats | 2.22% |
| **Total interspersed** | **47.52%** |
| Soft-masked total | 50.48% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:95.5% [S:82.5%, D:13.0%] F:0.7% M:3.8% (n=3203) |
| OMARK completeness | 85.01% single, 10.35% duplicated, 4.64% missing |
| OMARK consistency | 68.19% consistent, 6.83% inconsistent, 24.99% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 50.80% of proteins |
| KEGG KO | 57.06% of proteins |
| COG categories | 90.08% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964059495.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964059495.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964059495.1/) |

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
