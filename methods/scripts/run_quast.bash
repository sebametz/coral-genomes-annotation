#!/bin/bash
# bsub -o quast.log -n 16 -q normal -M8G -R'select[mem > 8G] rusage[mem=8G]'


CPUS=16
source ~/quast/bin/activate

for i in ~/coral-genomes-annotation/results/ja*; do
	echo "Processing $i"

	INPUT=$i
	base=$(basename $i)
	tolid=${base%%_*}
	OUTPUT="stats/quast/${tolid}"
 
	mkdir -p $OUTPUT
	cd $OUTPUT
	wget "https://asg_hubs.cog.sanger.ac.uk/${tolid}/${tolid}.fa.masked"
 
	quast.py --threads $CPUS  "${tolid}.fa.masked" 
 
	echo "${tolid} done!"
 
	cd /lustre/scratch124/tol/teams/tolengine_guest/projects/coral_annotation
done

deactivate
