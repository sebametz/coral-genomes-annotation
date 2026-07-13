# *Acropora loripes* — jaAcrLori1 / GCA_965214385.1

## Overview

| | |
|---|---|
| **Species** | *Acropora loripes* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_965214385.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965214385.1) |
| **ToLID** | jaAcrLori1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [154029](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=154029) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 547230792 bp |
| Scaffolds | 1579 |
| N50 | 28738798 bp |
| GC content | 39.11% |
| Soft-masked | 56.93% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 28743 |
| Average gene length | 5143 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1300 bp |
| Exons per transcript | 6.11 |
| Average exon length | 212 bp |
| Average intron length | 842.6 bp |
| Single-exon transcripts | 10438 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 18.46% |
| DNA transposons | 4.70% |
| Rolling circles | 0.36% |
| Unclassified | 32.27% |
| Simple repeats | 0.66% |
| **Total interspersed** | **55.43%** |
| Soft-masked total | 56.93% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:96.8% [S:79.2%, D:17.6%] F:1.1% M:2.1% (n=3203) |
| OMARK completeness | 85.81% single, 9.16% duplicated, 5.03% missing |
| OMARK consistency | 58.62% consistent, 8.73% inconsistent, 32.65% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 49.19% of proteins |
| KEGG KO | 53.05% of proteins |
| COG categories | 86.98% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_965214385.1](https://www.ebi.ac.uk/ena/browser/view/GCA_965214385.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965214385.1/) |

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
