#!/bin/bash
# bsub -o busco.log -n 8 -q normal -M8G -R'select[mem > 8G] rusage[mem=8G]'


INPUT=$1
OUTPUT="${2}"

CPUS=8
ORTHODB=$3

module load busco/5.8.2--pyhdfd78af_0

busco -f -i $INPUT -o $OUTPUT -l $ORTHODB -m protein -c 8

