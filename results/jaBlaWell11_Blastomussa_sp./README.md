# *Blastomussa sp.* — jaBlaWell11 / GCA_947652115.1

## Overview

| | |
|---|---|
| **Species** | *Blastomussa sp.* |
| **Family** | Plerogyridae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_947652115.1](https://www.ebi.ac.uk/ena/browser/view/GCA_947652115.1) |
| **ToLID** | jaBlaWell11 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [419443](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=419443) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 368009085 bp |
| Scaffolds | 135 |
| N50 | 27335774 bp |
| GC content | 39.73% |
| Soft-masked | 48.74% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 31382 |
| Average gene length | 5508 bp |
| Transcripts per gene | 1.11 |
| Average transcript length | 1396 bp |
| Exons per transcript | 6.02 |
| Average exon length | 231 bp |
| Average intron length | 863.7 bp |
| Single-exon transcripts | 10363 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 11.39% |
| DNA transposons | 5.88% |
| Rolling circles | 0.48% |
| Unclassified | 29.55% |
| Simple repeats | 1.00% |
| **Total interspersed** | **46.99%** |
| Soft-masked total | 48.74% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:89.6% [S:83.0%, D:6.6%] F:6.0% M:4.3% (n=3203) |
| OMARK completeness | 83.65% single, 11.95% duplicated, 4.40% missing |
| OMARK consistency | 61.27% consistent, 9.35% inconsistent, 29.38% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 46.07% of proteins |
| KEGG KO | 51.65% of proteins |
| COG categories | 85.51% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_947652115.1](https://www.ebi.ac.uk/ena/browser/view/GCA_947652115.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_947652115.1/) |

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
