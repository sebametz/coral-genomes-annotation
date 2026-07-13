# *Stephanocoenia intersepta* — jaSteInte3 / GCA_965112835.1

## Overview

| | |
|---|---|
| **Species** | *Stephanocoenia intersepta* |
| **Family** | Astrocoeniidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_965112835.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965112835.1) |
| **ToLID** | jaSteInte3 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [504342](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=504342) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 656234329 bp |
| Scaffolds | 1151 |
| N50 | 53335361 bp |
| GC content | 39.90% |
| Soft-masked | 59.85% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 30461 |
| Average gene length | 5994 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1199 bp |
| Exons per transcript | 5.29 |
| Average exon length | 227 bp |
| Average intron length | 1175.5 bp |
| Single-exon transcripts | 13840 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 9.42% |
| DNA transposons | 7.38% |
| Rolling circles | 0.12% |
| Unclassified | 41.22% |
| Simple repeats | 1.20% |
| **Total interspersed** | **58.04%** |
| Soft-masked total | 59.85% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:61.6% [S:52.8%, D:8.8%] F:15.6% M:22.8% (n=3203) |
| OMARK completeness | 74.28% single, 10.95% duplicated, 14.77% missing |
| OMARK consistency | 58.93% consistent, 10.10% inconsistent, 30.97% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 49.02% of proteins |
| KEGG KO | 55.67% of proteins |
| COG categories | 87.03% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_965112835.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965112835.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965112835.1/) |

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
