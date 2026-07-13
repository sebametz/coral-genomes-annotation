# *Montipora capitata* — jaMonCapi2 / GCA_949126865.1

## Overview

| | |
|---|---|
| **Species** | *Montipora capitata* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_949126865.1](https://www.ebi.ac.uk/ena/browser/view/GCA_949126865.1) |
| **ToLID** | jaMonCapi2 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [46704](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=46704) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 689329058 bp |
| Scaffolds | 133 |
| N50 | 47608193 bp |
| GC content | 39.62% |
| Soft-masked | 57.61% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 33201 |
| Average gene length | 8344 bp |
| Transcripts per gene | 1.14 |
| Average transcript length | 1344 bp |
| Exons per transcript | 6.10 |
| Average exon length | 220 bp |
| Average intron length | 1586.2 bp |
| Single-exon transcripts | 13460 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 18.20% |
| DNA transposons | 4.51% |
| Rolling circles | 0.26% |
| Unclassified | 33.21% |
| Simple repeats | 0.90% |
| **Total interspersed** | **56.06%** |
| Soft-masked total | 57.61% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:98.1% [S:82.0%, D:16.1%] F:0.9% M:1.0% (n=3203) |
| OMARK completeness | 89.46% single, 6.97% duplicated, 3.57% missing |
| OMARK consistency | 54.20% consistent, 9.52% inconsistent, 36.28% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 46.01% of proteins |
| KEGG KO | 51.56% of proteins |
| COG categories | 84.90% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_949126865.1](https://www.ebi.ac.uk/ena/browser/view/GCA_949126865.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_949126865.1/) |

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
