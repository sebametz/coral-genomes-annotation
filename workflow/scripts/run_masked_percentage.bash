#!/bin/bash

awk '/^>/{next} {
  for(i=1;i<=length($0);i++){
    c=substr($0,i,1)
    if(c~/[acgt]/) lc++
    if(c~/[acgtACGT]/) tot++
  }
} END {
  if (tot > 0)
    printf "%s\t%.4f\n", FILENAME, lc/tot*100
  else
    printf "%s\t%.4f\n", FILENAME, 0.0
}' ${1}/${1}.fa.masked > ${1}/masked_percentage.txt


