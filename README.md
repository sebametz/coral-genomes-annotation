# Coral Genomes Annotation

Gene prediction and functional annotation for 95 Scleractinia (stony coral) genomes.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20721096.svg)](https://doi.org/10.5281/zenodo.20721096)
[![DOI paper](https://img.shields.io/badge/paper-10.1038%2Fs41597--026--07499--3-blue)](https://doi.org/10.1038/s41597-026-07499-3)
[![License: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey)](DATA_LICENSE)

---

## Dataset overview

| | |
|---|---|
| Genomes | 95 Scleractinia |
| Genera | 41 |
| Families | 19 |
| Annotation version | v2.0 (2026) |
| Gene prediction | BRAKER3 (two-pass) |
| BUSCO lineage | cnidaria_odb12 |
| Assemblies | Chromosome-level (ENA/NCBI) |

The full per-genome statistics table is available at [`tables/genome_traits_summary.tsv`](tables/genome_traits_summary.tsv).

---

## Data access

Annotation files (GFF3, protein sequences, functional annotation, repeat libraries) for all 95 genomes are available on Zenodo:

> **Zenodo**: [https://doi.org/10.5281/zenodo.20721096](https://doi.org/10.5281/zenodo.20721096)

Genome assemblies are available through ENA/NCBI under their respective accession numbers listed in [`config/genomes.tsv`](config/genomes.tsv).

---

## Repository structure

```
coral-genomes-annotation/
│
├── config/
│   ├── genomes.tsv           Master manifest — one row per genome (47 columns)
│   └── tolid_mapping.tsv     genome_id ↔ ToLID / assembly name mapping
│
├── results/
│   └── {tolid}_{species}/    One folder per genome
│       └── README.md         Per-genome stats, quality metrics, download links
│
├── tables/
│   └── genome_traits_summary.tsv   Summary statistics for all 95 genomes
│
├── resources/
│   ├── protein_sets_v1/     Protein FASTA databases used in v1
│   │	└── README.md        Description of reference protein databases
│   └── protein_sets_v2/     Protein FASTA databases used in v2
│       └── README.md        Description of reference protein databases
│
├── workflow/
│   ├── annotation_method/    
│   │   ├──README.md	Description
│   │   ├──scripts/		LSF job scripts
│   │   └──pipeline_apr2025.jpeg Pipeline diagram
│   └── scripts/              Python/Bash utility scripts (parsers, organisers, portal)
│
├── CITATION.cff              Machine-readable citation (paper + Zenodo)
├── DATA_LICENSE              CC BY 4.0 — applies to all data files
└── LICENSE                   MIT — applies to all code and scripts
```

> Annotation data files (GFF3, FASTA, functional annotation) are **not stored in this repository** — they are too large for git and are archived on Zenodo (see above). Each `results/{tolid}_{species}/README.md` links directly to the Zenodo download for that genome.

---


**Tools usedi for annotation:**
| Step | Tool |
|---|---|
| Repeat annotation | [TETools](https://github.com/Dfam-consortium/TETools) (RepeatModeler + RepeatMasker) |
| RNA-seq alignment | [VARUS](https://github.com/Gaius-Augustus/VARUS) |
| Gene prediction | [BRAKER3](https://github.com/Gaius-Augustus/BRAKER) |
| Annotation QC | [BUSCO v5.8.2](https://busco.ezlab.org/) + [OMARK](https://github.com/DessimozLab/OMArk) |
| Functional annotation | [EggNOG-mapper v2](https://github.com/eggnogdb/emapper.py) + [InterProScan 5](https://www.ebi.ac.uk/interpro/about/interproscan/) |
| Comparative genomics | [OrthoFinder](https://github.com/davidemms/OrthoFinder) |
| Assembly stats | [QUAST](https://quast.sourceforge.net/) + [seqkit](https://bioinf.shenwei.me/seqkit/) |

---

## Per-genome results

Each genome has a dedicated folder under `results/` named `{tolid}_{species}/` (e.g., `jaAcrSpic1_Acropora_spicifera/`). The `README.md` inside each folder contains:

- Assembly and annotation statistics
- BUSCO and OMARK quality scores
- Repeat content breakdown
- Functional annotation coverage (EggNOG, InterProScan)
- Download links to Zenodo annotation files
- Changelog (what changed between v1 and v2)

Browse all genomes: [`results/`](results/)

---

## Citation

If you use these annotations, please cite:

> Metz, S., Paulini, M., Rising, K. et al. Chromosome-level genomes of scleractinian corals: gene prediction and functional annotation. *Scientific Data* (2026). https://doi.org/10.1038/s41597-026-07499-3

Data repository:

> [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17713987.svg)](https://doi.org/10.5281/zenodo.17713987)

A `CITATION.cff` file is included for automated citation tools. GitHub will display a **Cite this repository** button on the repo homepage.

---

## Licensing

| | License |
|---|---|
| **Code** (scripts, workflow, Snakefile) | [MIT](LICENSE) |
| **Data** (annotations, tables, per-genome READMEs) | [CC BY 4.0](DATA_LICENSE) |

---

## Versioning

| Version | Genomes | Date | Notes |
|---|---|---|---|
| v2.0 | 95 | 2026-07 | Two-pass BRAKER3, InterProScan, OMARK, cnidaria_odb12 |
| v1.0 | 40 | 2024-11 | Initial release |

Previous releases are archived on Zenodo with independent DOIs.

---

## Contributing

To add a new genome, please contact me: s.metz [at] derby.ac.uk
