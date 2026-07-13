# *Cyphastrea salae* — jaCypSala7 / GCA_964194085.1

## Overview

| | |
|---|---|
| **Species** | *Cyphastrea salae* |
| **Family** | Merulinidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964194085.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964194085.1) |
| **ToLID** | jaCypSala7 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [1967629](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1967629) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 536305725 bp |
| Scaffolds | 37 |
| N50 | 38477971 bp |
| GC content | 39.19% |
| Soft-masked | 52.58% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 30980 |
| Average gene length | 5519 bp |
| Transcripts per gene | 1.14 |
| Average transcript length | 1298 bp |
| Exons per transcript | 5.74 |
| Average exon length | 226 bp |
| Average intron length | 981.8 bp |
| Single-exon transcripts | 12361 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 10.84% |
| DNA transposons | 5.36% |
| Rolling circles | 0.41% |
| Unclassified | 34.50% |
| Simple repeats | 1.06% |
| **Total interspersed** | **50.85%** |
| Soft-masked total | 52.58% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:95.2% [S:80.9%, D:14.3%] F:1.8% M:3.0% (n=3203) |
| OMARK completeness | 86.20% single, 9.84% duplicated, 3.96% missing |
| OMARK consistency | 62.59% consistent, 8.43% inconsistent, 28.97% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 48.61% of proteins |
| KEGG KO | 54.69% of proteins |
| COG categories | 87.66% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964194085.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964194085.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964194085.1/) |

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
