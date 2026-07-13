# *Pocillopora damicornis* — jaPocDami1 / GCA_964200805.1

## Overview

| | |
|---|---|
| **Species** | *Pocillopora damicornis* |
| **Family** | Pocilloporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964200805.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964200805.1) |
| **ToLID** | jaPocDami1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [46731](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=46731) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 380694473 bp |
| Scaffolds | 115 |
| N50 | 25611475 bp |
| GC content | 38.06% |
| Soft-masked | 43.42% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 26477 |
| Average gene length | 5487 bp |
| Transcripts per gene | 1.17 |
| Average transcript length | 1540 bp |
| Exons per transcript | 7.59 |
| Average exon length | 202 bp |
| Average intron length | 685.7 bp |
| Single-exon transcripts | 7830 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 6.94% |
| DNA transposons | 3.87% |
| Rolling circles | 0.48% |
| Unclassified | 30.78% |
| Simple repeats | 0.88% |
| **Total interspersed** | **41.82%** |
| Soft-masked total | 43.42% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:99.2% [S:83.5%, D:15.7%] F:0.4% M:0.4% (n=3203) |
| OMARK completeness | 87.95% single, 10.76% duplicated, 1.29% missing |
| OMARK consistency | 72.14% consistent, 5.39% inconsistent, 22.47% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 53.83% of proteins |
| KEGG KO | 59.13% of proteins |
| COG categories | 92.68% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964200805.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964200805.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964200805.1/) |

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
