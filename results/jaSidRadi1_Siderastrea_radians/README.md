# *Siderastrea radians* — jaSidRadi1 / GCA_964017195.1

## Overview

| | |
|---|---|
| **Species** | *Siderastrea radians* |
| **Family** | Rhizangiidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964017195.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964017195.1) |
| **ToLID** | jaSidRadi1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [214988](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=214988) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 807211382 bp |
| Scaffolds | 539 |
| N50 | 56751969 bp |
| GC content | 39.98% |
| Soft-masked | 54.93% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 40765 |
| Average gene length | 5610 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1214 bp |
| Exons per transcript | 5.00 |
| Average exon length | 242 bp |
| Average intron length | 1207.1 bp |
| Single-exon transcripts | 17979 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 9.02% |
| DNA transposons | 8.47% |
| Rolling circles | 0.04% |
| Unclassified | 33.39% |
| Simple repeats | 1.10% |
| **Total interspersed** | **51.11%** |
| Soft-masked total | 54.93% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:95.5% [S:80.1%, D:15.4%] F:1.4% M:3.0% (n=3203) |
| OMARK completeness | 84.82% single, 10.49% duplicated, 4.69% missing |
| OMARK consistency | 56.60% consistent, 8.98% inconsistent, 34.41% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 43.88% of proteins |
| KEGG KO | 50.63% of proteins |
| COG categories | 84.24% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964017195.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964017195.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964017195.1/) |

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
