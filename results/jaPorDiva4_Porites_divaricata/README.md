# *Porites divaricata* — jaPorDiva4 / GCA_964035745.1

## Overview

| | |
|---|---|
| **Species** | *Porites divaricata* |
| **Family** | Poritidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964035745.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964035745.1) |
| **ToLID** | jaPorDiva4 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [262287](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=262287) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 527108013 bp |
| Scaffolds | 90 |
| N50 | 47881226 bp |
| GC content | 38.96% |
| Soft-masked | 53.94% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 26471 |
| Average gene length | 8475 bp |
| Transcripts per gene | 1.16 |
| Average transcript length | 1535 bp |
| Exons per transcript | 7.29 |
| Average exon length | 210 bp |
| Average intron length | 1244.2 bp |
| Single-exon transcripts | 8419 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 11.29% |
| DNA transposons | 5.01% |
| Rolling circles | 0.14% |
| Unclassified | 36.17% |
| Simple repeats | 0.91% |
| **Total interspersed** | **52.77%** |
| Soft-masked total | 53.94% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:99.2% [S:84.3%, D:14.9%] F:0.5% M:0.3% (n=3203) |
| OMARK completeness | 89.48% single, 8.02% duplicated, 2.50% missing |
| OMARK consistency | 66.21% consistent, 7.84% inconsistent, 25.95% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 53.50% of proteins |
| KEGG KO | 58.96% of proteins |
| COG categories | 91.52% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964035745.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964035745.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964035745.1/) |

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
