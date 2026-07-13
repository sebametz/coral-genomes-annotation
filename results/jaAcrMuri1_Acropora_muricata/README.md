# *Acropora muricata* — jaAcrMuri1 / GCA_964332325.1

## Overview

| | |
|---|---|
| **Species** | *Acropora muricata* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964332325.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964332325.1) |
| **ToLID** | jaAcrMuri1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [159855](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=159855) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 468464808 bp |
| Scaffolds | 709 |
| N50 | 32304366 bp |
| GC content | 39.07% |
| Soft-masked | 53.58% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 25903 |
| Average gene length | 6336 bp |
| Transcripts per gene | 1.18 |
| Average transcript length | 1436 bp |
| Exons per transcript | 7.13 |
| Average exon length | 201 bp |
| Average intron length | 940.1 bp |
| Single-exon transcripts | 8661 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 13.21% |
| DNA transposons | 4.95% |
| Rolling circles | 0.35% |
| Unclassified | 33.00% |
| Simple repeats | 0.67% |
| **Total interspersed** | **51.51%** |
| Soft-masked total | 53.58% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.7% [S:80.6%, D:18.0%] F:0.5% M:0.8% (n=3203) |
| OMARK completeness | 89.00% single, 6.95% duplicated, 4.06% missing |
| OMARK consistency | 61.66% consistent, 8.28% inconsistent, 30.06% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 52.23% of proteins |
| KEGG KO | 56.19% of proteins |
| COG categories | 88.65% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964332325.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964332325.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964332325.1/) |

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
