#!/bin/bash

use_proxy=yes
http_proxy=http://wwwcache.sanger.ac.uk:3128
https_proxy=http://wwwcache.sanger.ac.uk:3128
export PATH=/data/tol/users/mh6/lustre/VARUS/Implementation:$PATH

# bsub -o rat.lsf -n 8 -q basement -M12000 -R'select[mem > 12000] rusage[mem=12000] span[hosts=1]'



module load bamtools/2.5.2--hdcf5f25_3

module load cellgen/sratoolkit/3.2.0
module load cellgen/samtools/1.21

module load hisat2/2.2.1--hdbdd923_6


/data/tol/users/mh6/lustre/VARUS/runVARUS.pl --readFromTable=1 --createindex=1  --aligner=HISAT
