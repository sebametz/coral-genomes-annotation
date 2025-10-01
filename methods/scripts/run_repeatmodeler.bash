#!/bin/bash
# 34 threads
# 96G memory
# bsub -o runrm.log -q week -M96000 -R'select[mem>96000 && tmp>32G] rusage[mem=96000,tmp=32G] span[hosts=1]' -n 32

INFILE=$1
SPECIES=$2
DIR=`pwd`
THREADS=32

module load ISG/singularity/

[ -d /tmp/$INFILE ] && rm -rf /tmp/$INFILE

mkdir -p /tmp/$INFILE/out

cp $INFILE /tmp/$INFILE/out/

cd /tmp/$INFILE/out/

IMG=/data/tol/users/mh6/nfs/singularity/tetools_1.92.sif


singularity exec --bind `pwd`:$HOME $IMG BuildDatabase -name $SPECIES $INFILE
# singularity exec --bind `pwd`:$HOME $IMG RepeatModeler -database $SPECIES -threads $THREADS
singularity exec --bind `pwd`:$HOME $IMG RepeatModeler -database $SPECIES -LTRStruct -threads $THREADS
singularity exec --bind `pwd`:$HOME $IMG RepeatMasker -lib ${SPECIES}-families.fa $INFILE -xsmall -pa $THREADS

cd ..
echo "creating $DIR/$SPECIES.tar"
tar cvf $DIR/$SPECIES.tar out/
xz -9 -e -T $THREADS $DIR/$SPECIES.tar

rm -rf /tmp/$INFILE
