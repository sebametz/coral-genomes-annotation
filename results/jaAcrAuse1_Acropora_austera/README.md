# *Acropora austera* — jaAcrAuse1 / GCA_964273435.1

## Overview

| | |
|---|---|
| **Species** | *Acropora austera* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964273435.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964273435.1) |
| **ToLID** | jaAcrAuse1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [117779](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=117779) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 482207919 bp |
| Scaffolds | 1142 |
| N50 | 28705890 bp |
| GC content | 39.12% |
| Soft-masked | 52.31% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 29008 |
| Average gene length | 5977 bp |
| Transcripts per gene | 1.16 |
| Average transcript length | 1437 bp |
| Exons per transcript | 6.81 |
| Average exon length | 211 bp |
| Average intron length | 917.5 bp |
| Single-exon transcripts | 10362 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 14.30% |
| DNA transposons | 5.50% |
| Rolling circles | 0.58% |
| Unclassified | 30.53% |
| Simple repeats | 0.79% |
| **Total interspersed** | **50.56%** |
| Soft-masked total | 52.31% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:97.6% [S:81.4%, D:16.3%] F:0.9% M:1.5% (n=3203) |
| OMARK completeness | 88.37% single, 7.65% duplicated, 3.98% missing |
| OMARK consistency | 59.92% consistent, 9.24% inconsistent, 30.84% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 48.94% of proteins |
| KEGG KO | 53.38% of proteins |
| COG categories | 87.25% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964273435.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964273435.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964273435.1/) |

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
