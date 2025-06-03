# Coral annotations
Collected annotations of the ASG Scleractinia

Currently created using [TE Tools](https://github.com/Dfam-consortium/TETools) => [VARUS](https://github.com/Gaius-Augustus/VARUS) => [BRAKER3](https://github.com/Gaius-Augustus/BRAKER) / [GALBA](https://github.com/Gaius-Augustus/GALBA) => [OMArk](https://github.com/DessimozLab/OMArk) => [MakeHub](https://github.com/Gaius-Augustus/MakeHub)

# Folder structure
## results/
### tolID_species_name/
* protein fasta file (braker.aa or galba.aa)
* coding sequences fasta file (braker.codingseq or galba.codingseq)
* GTF file (braker.gtf or galba.tpf)
* GFF file decorated (itol.emapper.decorated.gff)
* emapper annotation file (itol.emapper.annotations)
* Stats file with number of genes, avg transcripts per gene, avg transcript length, avg exons number and avg exon length (itol.stats)
* description of additional files of interest (RNASeq libraries / genome sequences / repeat libraries)
## protein_sets/
* description of the origin of the sequences used to train BRAKER3/GALBA
## methods/
* process used to create the annotations
