# *Madracis senaria* — jaMadSena2 / GCA_964656595.1

## Overview

| | |
|---|---|
| **Species** | *Madracis senaria* |
| **Family** | Pocilloporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964656595.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964656595.1) |
| **ToLID** | jaMadSena2 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [123773](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=123773) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 541754393 bp |
| Scaffolds | 403 |
| N50 | 38906063 bp |
| GC content | 37.97% |
| Soft-masked | 52.28% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 29082 |
| Average gene length | 6151 bp |
| Transcripts per gene | 1.13 |
| Average transcript length | 1326 bp |
| Exons per transcript | 5.96 |
| Average exon length | 222 bp |
| Average intron length | 1063.0 bp |
| Single-exon transcripts | 10598 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 10.22% |
| DNA transposons | 5.23% |
| Rolling circles | 0.26% |
| Unclassified | 31.80% |
| Simple repeats | 4.32% |
| **Total interspersed** | **47.32%** |
| Soft-masked total | 52.28% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:95.7% [S:82.6%, D:13.0%] F:1.2% M:3.2% (n=3203) |
| OMARK completeness | 85.52% single, 10.20% duplicated, 4.27% missing |
| OMARK consistency | 66.99% consistent, 7.45% inconsistent, 25.56% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 49.38% of proteins |
| KEGG KO | 55.77% of proteins |
| COG categories | 88.95% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964656595.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964656595.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964656595.1/) |

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
