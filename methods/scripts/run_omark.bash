#!/bin/bash
# bsub -o omark.log -q normal -M16G -R'select[mem>16G] rusage[mem=16G]' -n 1


module load omamer/2.1.0--pyhdfd78af_0

#export http_proxy=http://wwwcache.sanger.ac.uk:3128

itol=$1
round=$2

input="${itol}/${round}/braker.aa"

db=/data/tol/resources/omark/LUCA.h5 #/lustre/scratch123/tol/resources/omark/LUCA.h5

# get genelist
perl -nE 'if(/>(g\d+)(\.t\d+)/){$h{$1}||=();push @{$h{$1}},"$1$2"}END{while(($k,$v)=each %h){say join ";",@{$v}}}' $input > "${itol}/${itol}_${round}.splice"

omamer search --db $db --query $input --out "${itol}/${itol}_${round}.omamer"

mkdir -p "${itol}/omark_${round}"

source /nfs/users/nfs_s/sm70/omark/bin/activate

omark -f "${itol}/${itol}_${round}.omamer" -i "${itol}/${itol}_${round}.splice" -r phylum -d $db -o "${itol}/omark_${round}"

echo "${s} DONE!"
