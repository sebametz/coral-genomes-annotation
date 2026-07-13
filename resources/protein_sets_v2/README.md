# Protein reference databases
 
Reference protein datasets used for gene prediction with BRAKER3.
Each annotation version used a different set of databases, described below.
 
---
 
## Version 2.0 (current)
 
Two protein databases were constructed for the two-round BRAKER3 pipeline.
 
### D1 — Full Scleractinia dataset (Round 1)
 
Used in **Round 1** gene prediction for all 95 genomes.
 
**Composition:**
- Predicted protein sequences for Cnidaria from **OrthoDB v12.2** ([orthodb.org](https://www.orthodb.org/)) — the set of orthogroups predicted for Cnidaria at the level of this clade
- All protein sequences predicted from the **v1 Scleractinia annotations** (40 genomes; BRAKER3)
- Number of proteins: 1,739,628

**Construction:**
```bash
# 1. Download OrthoDB v12.2 Cnidaria proteins
cat odb12v0_Cnidaria_proteins.fasta \         ← OrthoDB v12.2 Cnidaria subset
    scleractinia_v1_all_proteins.fasta \       ← all 40 v1 predicted proteomes concatenated
    > Scleractinia.fasta
```
Link D1: [cnidaria_odb12v2_plus40corals_braker.faa.tar.gz](https://unimailderbyac-my.sharepoint.com/:u:/g/personal/305120_derby_ac_uk/IQAfE4ejvuqSRLvg5OYgrS0XAYz3Zb9HPcRU_9FbaJFEb8Y?e=JQ5DCA) 

### D2 — All predicted annotations from Round 1

Used in **Round 2** gene prediction, all predicted proteins from Round 1.
 
**Composition:**
- All Scleractinia protein sequences predicted in **Round 1** (using D1)
- Number of proteins:2,813,597 

The rationale: Round 1 provides a first set of gene models for all genomes using a wider database. Round 2 refines predictions using a scleractinia-specific training set that more closely reflects the evolutionary context.
 
Link D2: [Scleractinia_apr_2026_braker.faa.tar.gz](https://unimailderbyac-my.sharepoint.com/:u:/g/personal/305120_derby_ac_uk/IQByI5geMOHFQpvtZfKr0Vu0Aa2jVvaev5PDM6R_P3TrpFw?e=Os63hE)

---
