# MIT License © 2025 Motohiro Suzuki

from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml  # type: ignore
except Exception:
    print("[ERROR] Missing dependency: pyyaml")
    print("        Install with: python -m pip install pyyaml")
    sys.exit(2)


INPUT = Path("claims/claims.yaml")
OUTPUT = Path("out/claim_matrix.md")


def generate_markdown(claims: list[dict]) -> str:
    lines: list[str] = []
    lines.append("| Claim | Lemma | Attack Scenario | CI Status |")
    lines.append("|-------|--------|----------------|-----------|")

    for c in claims:
        cid = c.get("id", "")
        lemma = c.get("lemma", "")
        attack = c.get("attack", "")
        status = c.get("ci_status", "")
        lines.append(f"| {cid} | {lemma} | {attack} | {status} |")

    return "\n".join(lines) + "\n"


def main() -> int:
    if not INPUT.exists():
        print(f"[ERROR] not found: {INPUT}")
        return 2

    data = yaml.safe_load(INPUT.read_text(encoding="utf-8")) or {}
    claims = data.get("claims", [])
    if not isinstance(claims, list):
        print("[ERROR] claims must be a list in claims/claims.yaml")
        return 2

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(generate_markdown(claims), encoding="utf-8")
    print(f"[OK] generated: {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
