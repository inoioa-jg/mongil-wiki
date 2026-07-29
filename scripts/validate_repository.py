"""Fail when required records or confidence metadata are missing."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "account" / "roster.md"
CHARACTERS = ROOT / "data" / "characters"
VALID_CONFIDENCE = {"official", "in_game", "tested", "community", "hypothesis", "unknown"}


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main() -> int:
    errors: list[str] = []
    roster_names = []
    for line in ROSTER.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\| (Fire|Lightning|Earth|Ice|Wind) \| ([^|]+) \|", line)
        if match:
            roster_names.append((match.group(1).lower(), match.group(2).strip()))

    for element, name in roster_names:
        path = CHARACTERS / element / f"{slug(name)}.md"
        if not path.exists():
            errors.append(f"missing character record: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        confidence = re.search(r"^source_confidence:\s*(\S+)", text, re.MULTILINE)
        if not confidence or confidence.group(1) not in VALID_CONFIDENCE:
            errors.append(f"invalid source_confidence: {path.relative_to(ROOT)}")
        if f"element: {element}" not in text:
            errors.append(f"element mismatch: {path.relative_to(ROOT)}")

    if len(roster_names) != 23:
        errors.append(f"expected 23 roster entries, found {len(roster_names)}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {len(roster_names)} roster character records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

