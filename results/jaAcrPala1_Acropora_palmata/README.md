# *Acropora palmata* — jaAcrPala1 / GCA_964030605.3

## Overview

| | |
|---|---|
| **Species** | *Acropora palmata* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964030605.3](https://www.ebi.ac.uk/ena/browser/view/GCA_964030605.3) |
| **ToLID** | jaAcrPala1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [6131](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=6131) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 333964842 bp |
| Scaffolds | 245 |
| N50 | 22572888 bp |
| GC content | 39.11% |
| Soft-masked | 41.61% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 23791 |
| Average gene length | 6402 bp |
| Transcripts per gene | 1.18 |
| Average transcript length | 1506 bp |
| Exons per transcript | 7.61 |
| Average exon length | 197 bp |
| Average intron length | 852.9 bp |
| Single-exon transcripts | 7663 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 10.54% |
| DNA transposons | 4.09% |
| Rolling circles | 0.21% |
| Unclassified | 25.28% |
| Simple repeats | 0.89% |
| **Total interspersed** | **39.92%** |
| Soft-masked total | 41.61% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:99.1% [S:82.2%, D:16.9%] F:0.4% M:0.5% (n=3203) |
| OMARK completeness | 89.90% single, 6.46% duplicated, 3.64% missing |
| OMARK consistency | 63.84% consistent, 8.18% inconsistent, 27.98% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 54.06% of proteins |
| KEGG KO | 57.53% of proteins |
| COG categories | 91.05% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964030605.3](https://www.ebi.ac.uk/ena/browser/view/GCA_964030605.3) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964030605.3/) |

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
