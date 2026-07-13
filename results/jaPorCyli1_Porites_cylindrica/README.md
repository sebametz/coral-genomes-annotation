# *Porites cylindrica* — jaPorCyli1 / GCA_964035525.1

## Overview

| | |
|---|---|
| **Species** | *Porites cylindrica* |
| **Family** | Poritidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964035525.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964035525.1) |
| **ToLID** | jaPorCyli1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [126659](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=126659) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 589292816 bp |
| Scaffolds | 109 |
| N50 | 37871096 bp |
| GC content | 39.22% |
| Soft-masked | 51.63% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 30988 |
| Average gene length | 6162 bp |
| Transcripts per gene | 1.14 |
| Average transcript length | 1420 bp |
| Exons per transcript | 6.19 |
| Average exon length | 229 bp |
| Average intron length | 1022.7 bp |
| Single-exon transcripts | 11829 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 9.34% |
| DNA transposons | 3.44% |
| Rolling circles | 0.29% |
| Unclassified | 36.65% |
| Simple repeats | 1.49% |
| **Total interspersed** | **49.57%** |
| Soft-masked total | 51.63% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:97.4% [S:84.0%, D:13.4%] F:1.1% M:1.4% (n=3203) |
| OMARK completeness | 87.52% single, 8.89% duplicated, 3.59% missing |
| OMARK consistency | 62.67% consistent, 8.39% inconsistent, 28.93% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 49.18% of proteins |
| KEGG KO | 55.50% of proteins |
| COG categories | 88.84% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964035525.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964035525.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964035525.1/) |

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
