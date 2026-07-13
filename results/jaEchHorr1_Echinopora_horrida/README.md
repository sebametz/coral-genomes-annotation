# *Echinopora horrida* — jaEchHorr1 / GCA_964199735.2

## Overview

| | |
|---|---|
| **Species** | *Echinopora horrida* |
| **Family** | Merulinidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964199735.2](https://www.ebi.ac.uk/ena/browser/view/GCA_964199735.2) |
| **ToLID** | jaEchHorr1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [983564](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=983564) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 658382683 bp |
| Scaffolds | 884 |
| N50 | 42565161 bp |
| GC content | 39.25% |
| Soft-masked | 54.44% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 49293 |
| Average gene length | 4805 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1251 bp |
| Exons per transcript | 5.25 |
| Average exon length | 238 bp |
| Average intron length | 886.1 bp |
| Single-exon transcripts | 16278 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 13.61% |
| DNA transposons | 7.13% |
| Rolling circles | 0.40% |
| Unclassified | 31.98% |
| Simple repeats | 1.04% |
| **Total interspersed** | **52.72%** |
| Soft-masked total | 54.44% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:92.7% [S:82.9%, D:9.8%] F:4.3% M:3.0% (n=3203) |
| OMARK completeness | 81.54% single, 15.33% duplicated, 3.13% missing |
| OMARK consistency | 53.41% consistent, 9.99% inconsistent, 36.59% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 39.20% of proteins |
| KEGG KO | 46.91% of proteins |
| COG categories | 81.00% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964199735.2](https://www.ebi.ac.uk/ena/browser/view/GCA_964199735.2) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964199735.2/) |

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
