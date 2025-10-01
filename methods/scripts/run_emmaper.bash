#!/bin/bash
# bsub -o /dev/null -n 22 -q normal -M60G -R'select[mem > 60G] rusage[mem=60G]'


input=$1
round=$2
base=$(basename $input) 
tolid=${base%%_*}

#CDS="${input}/${2}/braker.codingseq"

GTF="${input}/${round}/braker.gtf"
GFF="${input}/${tolid}.gff"
OUTPUT="${input}/${tolid}_annotation"
PROT="${input}/${round}/braker.aa"

CPUS=22

cat $GTF | /lustre/scratch124/tol/teams/tolengine_guest/projects/coral_annotation/scripts/annotation/gtf2gff.pl --gff3 --out=$GFF

module load eggnog-mapper/2.1.12--pyhdfd78af_2

emapper.py --override --data_dir /lustre/scratch122/tol/resources/eggnog --cpu $CPUS --itype proteins -i $PROT -o $OUTPUT --decorate_gff $GFF --decorate_gff_ID_field ID

#emapper.py --override --data_dir /lustre/scratch123/tol/resources/eggnog --cpu $CPUS --itype CDS --translate -i $CDS -o $OUTPUT --decorate_gff $GFF --decorate_gff_ID_field ID
