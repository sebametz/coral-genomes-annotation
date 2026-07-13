# *Acropora spicifera* — jaAcrSpic1 / GCA_964261235.1

## Overview

| | |
|---|---|
| **Species** | *Acropora spicifera* |
| **Family** | Acroporidae |
| **Order** | Scleractinia |
| **Assembly accession** | [GCA_964261235.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964261235.1) |
| **ToLID** | jaAcrSpic1 |
| **Haplotype** | hap1 |
| **NCBI Taxonomy ID** | [191023](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=191023) |
| **Annotation version** | v2 |
| **Annotation pipeline** | RepeatModeller;BRAKER3;Egg-NOG mapper;InterProScan — v2 |
| **Protein database** | R1: VARUS + db [Cnidaria + Scleractinia]; R2: VARUS + db [Scleractinia v2] — v2 |
| **BUSCO lineage** | cnidaria_odb12 |

## Assembly statistics

| Metric | Value |
|---|---|
| Total length | 478509595 bp |
| Scaffolds | 89 |
| N50 | 31359961 bp |
| GC content | 39.05% |
| Soft-masked | 54.90% |

## Gene annotation statistics

| Metric | Value |
|---|---|
| Genes | 27928 |
| Average gene length | 5808 bp |
| Transcripts per gene | 1.17 |
| Average transcript length | 1404 bp |
| Exons per transcript | 6.73 |
| Average exon length | 208 bp |
| Average intron length | 884.1 bp |
| Single-exon transcripts | 9833 |

## Repeat content

| Class | % genome |
|---|---|
| Retroelements | 16.84% |
| DNA transposons | 4.70% |
| Rolling circles | 0.31% |
| Unclassified | 31.56% |
| Simple repeats | 0.74% |
| **Total interspersed** | **53.34%** |
| Soft-masked total | 54.90% |

## Annotation quality

| Tool | Result |
|---|---|
| BUSCO | C:99.0% [S:81.8%, D:17.2%] F:0.3% M:0.7% (n=3203) |
| OMARK completeness | 89.43% single, 6.85% duplicated, 3.72% missing |
| OMARK consistency | 59.75% consistent, 9.09% inconsistent, 31.15% unknown |

## Functional annotation

| Database | Coverage |
|---|---|
| EggNOG-mapper | 100.00% annotated |
| GO terms (EggNOG) | 50.11% of proteins |
| KEGG KO | 53.67% of proteins |
| COG categories | 87.71% of proteins |
| InterProScan domains | 100.00% of proteins |

## Downloads

| Resource | Link |
|---|---|
| Annotation files (this version, Zenodo) | [10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096) |
| Assembly (ENA) | [GCA_964261235.1](https://www.ebi.ac.uk/ena/browser/view/GCA_964261235.1) |
| Assembly (NCBI) | [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_964261235.1/) |

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
