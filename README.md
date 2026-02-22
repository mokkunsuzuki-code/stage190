# Stage190 — Claim ↔ Lemma ↔ Attack Coverage Matrix

MIT License © 2025 Motohiro Suzuki

---

## 🎯 Purpose

Stage190 provides a machine-verifiable traceability layer:

Claim → Formal Lemma → Attack Scenario → CI Result

The matrix is generated automatically from a YAML source of truth
and published as a CI artifact.

This ensures:

- Claims are machine-readable
- Lemmas are traceable
- Attack coverage is explicit
- CI enforces structural consistency

---

## 📂 Repository Structure


stage190/
├── claims/
│ └── claims.yaml
├── tools/
│ └── generate_matrix.py
├── out/
│ └── claim_matrix.md (generated)
├── .github/workflows/
│ └── claim-matrix.yml
├── README.md
└── LICENSE


---

## 🔁 Generation Flow

YAML → Markdown → CI Artifact → README reference

1. Define claims in `claims/claims.yaml`
2. Run generator
3. Markdown table is produced
4. CI uploads artifact

---

## 📊 Example Output

| Claim | Lemma | Attack Scenario | CI Status |
|-------|--------|----------------|-----------|
| A1 | lemma_fail_closed | attack_01_mismatch | PASS |
| A2 | lemma_handshake | attack_02_replay | PASS |
| A3 | lemma_epoch | attack_03_rollback | PASS |

---

## ⚙️ Local Usage

Install dependency:

```bash
python -m pip install pyyaml

Generate matrix:

python tools/generate_matrix.py

View result:

cat out/claim_matrix.md
🚀 CI Integration

GitHub Actions workflow:

.github/workflows/claim-matrix.yml

CI automatically:

Installs dependencies

Generates matrix

Uploads claim_matrix.md as artifact named:

claim-matrix
🔐 Design Philosophy

Stage190 is not a protocol implementation layer.

It is a structural verification layer ensuring:

Security claims are traceable

Formal lemmas are linked

Attack coverage is visible

CI guarantees reproducibility

📜 License

MIT License © 2025 Motohiro Suzuki
