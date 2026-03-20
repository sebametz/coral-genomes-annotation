# Coral annotations
Collected annotations of the ASG Scleractinia (& other)

Currently created using [TE Tools](https://github.com/Dfam-consortium/TETools) => [VARUS](https://github.com/Gaius-Augustus/VARUS) => [BRAKER3](https://github.com/Gaius-Augustus/BRAKER) / [GALBA](https://github.com/Gaius-Augustus/GALBA) => [BUSCO](https://busco.ezlab.org/) / [OMArk](https://github.com/DessimozLab/OMArk)

# Folder structure
## results/
### [tolid]_species_name/
* protein fasta file (braker.aa or galba.aa)
* coding sequences fasta file (braker.codingseq or galba.codingseq)
* GTF file (braker.gtf or galba.gtf)
* GFF file decorated ([tolid].emapper.decorated.gff)
* emapper annotation file ([tolid].emapper.annotations)
* stats file with number of genes, avg transcripts per gene, avg transcript length, avg exons number and avg exon length ([tolid].stats)
* RepeatModeler output: Masked genome (masked.fa); families fasta file; summary table (.tbl); coordinates in tsv format (.out) and log file.

## protein_sets/
* description of the origin of the sequences used to train BRAKER3/GALBA

## methods/
* process used to create the annotations

## Citation
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17713987.svg)](https://doi.org/10.5281/zenodo.17713987)


