# *Meandrina meandrites* — jaMeaMean2 / GCA_963693305.1

## Overview

| | |
|---|---|
| **Species** | *Meandrina meandrites* |
| **Family** | Meandrinidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_963693305.1](https://www.ebi.ac.uk/ena/browser/view/GCA_963693305.1) |
| **ToLID** | jaMeaMean2 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [51056](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=51056) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 551172847 bp |
| Scaffolds | 57 |
| N50 | 39932128 bp |
| GC content | 39.27% |
| Soft-masked | 52.88% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 33155 |
| Average gene length | 6172 bp |
| Transcripts per gene | 1.14 |
| Average transcript length | 1391 bp |
| Exons per transcript | 6.10 |
| Average exon length | 227 bp |
| Average intron length | 1032.0 bp |
| Single-exon transcripts | 12427 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 10.01% |
| DNA transposons | 5.91% |
| Rolling circles | 0.25% |
| Unclassified | 34.78% |
| Simple repeats | 1.54% |
| **Total interspersed** | **50.75%** |
| Soft-masked total | 52.88% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.3% [S:84.6%, D:13.8%] F:0.6% M:1.1% (n=3203) |
| OMARK completeness | 88.07% single, 9.47% duplicated, 2.45% missing |
| OMARK consistency | 65.15% consistent, 8.36% inconsistent, 26.48% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 47.78% of proteins |
| KEGG KO | 55.65% of proteins |
| COG categories | 89.51% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_963693305.1](https://www.ebi.ac.uk/ena/browser/view/GCA_963693305.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_963693305.1/) |

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
