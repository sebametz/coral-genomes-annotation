# *Porites haddoni* — jaPorLute2 / GCA_958299795.1

## Overview

| | |
|---|---|
| **Species** | *Porites haddoni* |
| **Family** | Poritidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_958299795.1](https://www.ebi.ac.uk/ena/browser/view/GCA_958299795.1) |
| **ToLID** | jaPorLute2 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [51062](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=51062) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2];  RNA: ERR12708749 — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 541663525 bp |
| Scaffolds | 107 |
| N50 | 35980406 bp |
| GC content | 39.14% |
| Soft-masked | 50.40% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 31988 |
| Average gene length | 6172 bp |
| Transcripts per gene | 1.15 |
| Average transcript length | 1387 bp |
| Exons per transcript | 6.08 |
| Average exon length | 228 bp |
| Average intron length | 1055.1 bp |
| Single-exon transcripts | 11786 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 8.99% |
| DNA transposons | 3.50% |
| Rolling circles | 0.18% |
| Unclassified | 35.89% |
| Simple repeats | 1.49% |
| **Total interspersed** | **48.52%** |
| Soft-masked total | 50.40% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:96.9% [S:82.4%, D:14.5%] F:1.0% M:2.2% (n=3203) |
| OMARK completeness | 87.37% single, 8.23% duplicated, 4.40% missing |
| OMARK consistency | 62.48% consistent, 8.43% inconsistent, 29.09% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 48.15% of proteins |
| KEGG KO | 54.39% of proteins |
| COG categories | 88.82% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_958299795.1](https://www.ebi.ac.uk/ena/browser/view/GCA_958299795.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_958299795.1/) |

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
