#!/bin/bash

GCA_SAFE="${1}"

# ── Edit these ────────────────────────────────────────────────────────────────
BASE_DIR=""
IPRSCAN_MODULE="interproscan/5.61-93.0"        # adjust to your module name
CHUNK_SIZE=1000                      # proteins per chunk
THREADS=8
TMPDIR="${BASE_DIR}/tmp/${GCA_SAFE}" # needs plenty of space
# ─────────────────────────────────────────────────────────────────────────────

PROTEIN_FA="${BASE_DIR}/${GCA_SAFE}/BRAKER3/braker.aa"
OUT_DIR="${BASE_DIR}/${GCA_SAFE}/interproscan"
CHUNK_DIR="${OUT_DIR}/chunks"

mkdir -p "${OUT_DIR}" "${CHUNK_DIR}" "${TMPDIR}"

module load "${IPRSCAN_MODULE}"

echo "[$(date)] Starting InterProScan for ${GCA_SAFE}"
echo "Input: ${PROTEIN_FA}"

# ── Remove stop codon asterisks (InterProScan rejects them) ──────────────────
CLEAN_FA="${OUT_DIR}/${GCA_SAFE}.clean.fa"
sed 's/\*//g' "${PROTEIN_FA}" > "${CLEAN_FA}"
echo "Sequences: $(grep -c '>' "${CLEAN_FA}")"

# ── Split into chunks ─────────────────────────────────────────────────────────
awk -v size="${CHUNK_SIZE}" -v dir="${CHUNK_DIR}" -v base="${GCA_SAFE}" '
    /^>/ { if (count % size == 0) {
               close(out)
               chunk = int(count/size)
               out = dir "/" base "_chunk_" chunk ".fa"
           }
           count++ }
    { print > out }
' "${CLEAN_FA}"

CHUNKS=( "${CHUNK_DIR}"/${GCA_SAFE}_chunk_*.fa )
echo "Chunks: ${#CHUNKS[@]}"

# ── Run InterProScan per chunk ────────────────────────────────────────────────
for CHUNK in "${CHUNKS[@]}"; do
    CHUNK_BASE=$(basename "${CHUNK}" .fa)
    echo "[$(date)] Processing ${CHUNK_BASE}..."

    interproscan.sh \
        -i  "${CHUNK}" \
        -o  "${CHUNK_DIR}/${CHUNK_BASE}.iprscan.tsv" \
        -f  TSV \
        -appl Pfam,TIGRFAM,PANTHER,Gene3D,CDD,Coils,MobiDBLite \
        -cpu "${THREADS}" \
        --tempdir "${TMPDIR}" \
        --goterms \
        --iprlookup \
        --disable-precalc \
        -dp

    echo "[$(date)] Done: ${CHUNK_BASE}"
done

# ── Merge chunk outputs ───────────────────────────────────────────────────────
MERGED="${OUT_DIR}/${GCA_SAFE}.iprscan.tsv"
cat "${CHUNK_DIR}"/${GCA_SAFE}_chunk_*.iprscan.tsv > "${MERGED}"

echo "[$(date)] Merged TSV: ${MERGED}"
echo "Total annotation lines: $(wc -l < "${MERGED}")"

# ── Clean up ──────────────────────────────────────────────────────────────────
rm -rf "${TMPDIR}" "${CLEAN_FA}" "${CHUNK_DIR}"

echo "[$(date)] Finished ${GCA_SAFE}"

# module load interproscan/5.61-93.0
