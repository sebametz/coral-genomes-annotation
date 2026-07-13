# *Turbinaria lichenoides* — jaTurReni1 / GCA_964204835.1

## Overview

| | |
|---|---|
| **Species** | *Turbinaria lichenoides* |
| **Family** | Dendrophylliidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964204835.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964204835.1) |
| **ToLID** | jaTurReni1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [1381352](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1381352) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2]; RNA: ERR13148262 — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 802319975 bp |
| Scaffolds | 748 |
| N50 | 53019679 bp |
| GC content | 39.17% |
| Soft-masked | 59.37% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 35354 |
| Average gene length | 4857 bp |
| Transcripts per gene | 1.12 |
| Average transcript length | 1293 bp |
| Exons per transcript | 5.18 |
| Average exon length | 249 bp |
| Average intron length | 947.8 bp |
| Single-exon transcripts | 15539 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 9.71% |
| DNA transposons | 8.36% |
| Rolling circles | 0.58% |
| Unclassified | 38.71% |
| Simple repeats | 0.80% |
| **Total interspersed** | **57.72%** |
| Soft-masked total | 59.37% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:92.9% [S:79.4%, D:13.5%] F:2.3% M:4.8% (n=3203) |
| OMARK completeness | 83.56% single, 10.54% duplicated, 5.90% missing |
| OMARK consistency | 60.28% consistent, 9.48% inconsistent, 30.23% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 44.23% of proteins |
| KEGG KO | 50.55% of proteins |
| COG categories | 84.08% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964204835.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964204835.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964204835.1/) |

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
