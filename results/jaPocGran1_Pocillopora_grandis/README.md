# *Pocillopora grandis* — jaPocGran1 / GCA_964027065.2

## Overview

| | |
|---|---|
| **Species** | *Pocillopora grandis* |
| **Family** | Pocilloporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964027065.2](https://www.ebi.ac.uk/ena/browser/view/GCA_964027065.2) |
| **ToLID** | jaPocGran1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [2759717](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2759717) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 361425095 bp |
| Scaffolds | 300 |
| N50 | 23862603 bp |
| GC content | 37.98% |
| Soft-masked | 40.17% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 27776 |
| Average gene length | 4834 bp |
| Transcripts per gene | 1.16 |
| Average transcript length | 1444 bp |
| Exons per transcript | 7.03 |
| Average exon length | 205 bp |
| Average intron length | 626.0 bp |
| Single-exon transcripts | 8691 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 7.31% |
| DNA transposons | 3.15% |
| Rolling circles | 0.43% |
| Unclassified | 28.18% |
| Simple repeats | 0.77% |
| **Total interspersed** | **38.65%** |
| Soft-masked total | 40.17% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:97.9% [S:84.0%, D:13.9%] F:1.0% M:1.2% (n=3203) |
| OMARK completeness | 87.01% single, 11.29% duplicated, 1.70% missing |
| OMARK consistency | 71.78% consistent, 5.58% inconsistent, 22.64% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 52.69% of proteins |
| KEGG KO | 58.52% of proteins |
| COG categories | 92.19% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964027065.2](https://www.ebi.ac.uk/ena/browser/view/GCA_964027065.2) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964027065.2/) |

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
