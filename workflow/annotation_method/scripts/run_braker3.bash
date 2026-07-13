#!/bin/bash
# run_braker.bash tolid Bla_blub proteins
# bsub -o /dev/null -n 22 -q long -M48G -R'select[mem > 48G, tmp>50G] rusage[mem=48G, tmp=50G] span[hosts=1]'


WDIR=$1
TOLID=${WDIR%%_*}
DB=$2

CPUS=22
WORK_DIR=/tmp/BRAKER3/$WDIR
ORIGINAL=/PATH/$WDIR
ORTHODB=metazoa_odb10

module load ISG/singularity/

export SINGULARITY_TMPDIR=/tmp/$USER/$BASHPID
export SINGULARITY_CACHEDIR=$SINGULARITY_TMPDIR/$USER

rm -rf $ORIGINAL/BRAKER3

mkdir -p $WORK_DIR

cp $ORIGINAL/$TOLID.fa.masked $WORK_DIR/
cp $ORIGINAL/VARUS_modified.bam $WORK_DIR/VARUS.bam

singularity exec --bind $WORK_DIR:$HOME,/PATH/db:/protdbs docker://teambraker/braker3:latest braker.pl --genome=$TOLID.fa.masked --prot_seq=/protdbs/$DB --threads=$CPUS --bam=VARUS.bam --workingdir=BRAKER3 --species=$TOLID --busco_lineage=$ORTHODB --crf

mv $WORK_DIR/BRAKER3 $ORIGINAL
rm -rf $WORK_DIR
rm -rf $SINGULARITY_TMPDIR
