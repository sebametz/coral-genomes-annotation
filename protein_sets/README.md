# Protein sets
## Scleractinia.fasta (Apr 2025)
Collection of NCBI, Uniprot and Ensembl Scleractinia proteins

## Complex_Aug_2025.faa.xz (Aug 2025)
Collection of 734,275 proteins, including BRAKER3 first round prediction of:
* jaAcrCerv1_Acropora_cervicornis
* jaAcrAuse1_Acropora_austera
* jaAcrGlau1_Acropora_glauca
* jaAcrHyac4_Acropora_hyacinthus
* jaAcrLori1_Acropora_loripes
* jaAcrMuri1_Acropora_muricata
* jaAcrPala1.3_Acropora_palmata
* jaAcrPulc1_Acropora_pulchra
* jaAcrSpat14_Acropora_spathulata
* jaAcrSpic1_Acropora_spicifera
* jaDunAxif1_Duncanopsammia_axifuga
* jaGalFasc40_Galaxea_fascicularis
* jaIsoPali11_Isopora_palifera
* jaMonCapi2_Montipora_capitata
* jaMonCapr1_Montipora_capricornis
* jaMonPala3_Montipora_palawanensis
* jaMonSpea1_Montipora_sp.UDUK0000274
* jaPorCyli1_Porites_cylindrica
* jaPorDiva4_Porites_divaricata
* jaPorLute2_Porites_lutea
* jaPorRusx1_Porites_rus
* jaSidRadi1_Siderastrea_radians
* jaSidSide1_Siderastrea_siderea
* jaSteInte3_Stephanocoenia_intersepta
* jaTurReni1_Turbinaria_reniformis

## Robust_Aug_2025.faa.xz (Aug 2025)
Collection of 438,329 proteins, including BRAKER3 first round prediction of:
* jaBlaWell11_Blastomussa_wellsi
* jaCauFurc1_Caulastraea_furcata
* jaCypSala7_Cyphastrea_salae
* jaDenCyli1_Dendrogyra_cylindrus
* jaDipLaby1_Diploria_labyrinthiformis
* jaEchHorr1_Echinopora_horrida
* jaMadAure2_Madracis_auretenra
* jaMadSena2_Madracis_senaria
* jaMeaMean2_Meandrina_meandrites
* jaMicLord3_Micromussa_lordhowensis
* jaOcuArbu1_Oculina_arbuscula
* jaOrbFran1_Orbicella_franksi
* jaPocDami1_Pocillopora_damicornis
* jaPocGran1_Pocillopora_grandis
* jaStyPist1_Stylophora_pistillata


## cnidaria_uniprot_25_08_2023_without_A0A6S7FRV1_PARCT.fa.xz
Unprot cnidaria proteins (with isoforms) with A0A6S7FRV1_PARCT, a centrosomal protein, that will align to too many regions for SPALN to deal with removed.

## uniprotkb_hexacorallia_2023_11_20.fasta.xz
UniProt hexacorallia proteins with isoforms.

### NOTE: 

To reassemble and decompress:

```bash

cat file.fasta.xz_part* | xz -d > file.fasta

```
