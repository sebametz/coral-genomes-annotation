# Protein sets
## Scleractinia.fasta.xz | Scleractinia_braker.fasta.xz (Apr 2025)
Collection of NCBI, Uniprot and Ensembl Scleractinia proteins

## Complexa_braker.fasta.xz (Jul 2025)
Added: 
	* jaAcrPala1.3
	* jaMonSpea1 

## Robusta_braker.fasta.xz (Jul 2025)
Added:
	* jaCauFurc1
	* jaDipLaby1

## Complexa_braker.fasta.xz (June 2025)
Collection of Complex corals predicted proteomes:

* jaAcrAuse1
* jaAcrCerv1
* jaAcrGlau1
* jaAcrHyac4
* jaAcrLori1
* jaAcrMuri1
* jaAcrPala1
* jaAcrPulc1
* jaAcrSpat14
* jaAcrSpic1
* jaIsoPali11
* jaMonCapi2
* jaMonCapr1
* jaMonPala3
* jaDunAxif1
* jaTurReni1
* jaGalFasc40
* jaPorCyli1
* jaPorDiva4
* jaPorLute2
* jaPorRusx1
* jaSidRadi1
* jaSidSide1

## Robusta_braker.fasta.xz (30 June 2025)
Collection of Robust corals predicted proteomes:

* jaSteInte3
* jaMicLord3
* jaDenCyli1
* jaMeaMean2
* jaCypSala7
* jaEchHorr1
* jaOrbFran1
* jaBlaWell11
* jaOcuArbu1
* jaMadAure2
* jaMadSena2
* jaPocDami1
* jaPocGran1
* jaStyPist1 

## cnidaria_uniprot_25_08_2023_without_A0A6S7FRV1_PARCT.fa.xz
Unprot cnidaria proteins (with isoforms) with A0A6S7FRV1_PARCT, a centrosomal protein, that will align to too many regions for SPALN to deal with removed.

## uniprotkb_hexacorallia_2023_11_20.fasta.xz
UniProt hexacorallia proteins with isoforms.

### NOTE: 

To reassemble and decompress:

```bash

cat file.fasta_part_*.xz | xz -d > file.fasta

```
