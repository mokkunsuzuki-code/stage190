# Stage190 — Claim ↔ Lemma ↔ Attack Coverage Matrix

MIT License © 2025 Motohiro Suzuki

## Purpose

This repository generates a traceability matrix:

**Claim → Formal Lemma → Attack Scenario → CI Result**

It is YAML-driven and produces Markdown output, then publishes it as a CI artifact.

## Files

- `claims/claims.yaml` — single source of truth
- `tools/generate_matrix.py` — YAML → Markdown generator
- `out/claim_matrix.md` — generated output (CI artifact)
- `.github/workflows/claim-matrix.yml` — CI pipeline

## Output

- [out/claim_matrix.md](out/claim_matrix.md)

## Quickstart

```bash
python -m pip install pyyaml
python tools/generate_matrix.py
cat out/claim_matrix.md
sed -n '1,120p' README.md
