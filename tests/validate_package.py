"""Validate the portable Conductor package without network access."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "conductor-setup",
    "conductor-new-track",
    "conductor-implement",
    "conductor-review",
    "conductor-status",
    "conductor-revert",
}


def frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    raw, body = text[4:].split("\n---\n", 1)
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    assert body.strip(), "SKILL.md body must not be empty"
    return result


def main() -> None:
    skill_dirs = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    }
    assert skill_dirs == EXPECTED, f"unexpected skills: {skill_dirs}"

    for name in sorted(EXPECTED):
        path = ROOT / "skills" / name / "SKILL.md"
        data = frontmatter(path.read_text(encoding="utf-8"))
        assert data.get("name") == name
        assert data.get("description"), f"missing description: {name}"
        assert not re.search(
            r"\b(?:en-US|English|language)\b",
            data["description"],
            re.IGNORECASE,
        ), f"language metadata does not belong in the description: {name}"
        assert "# Conductor" in path.read_text(encoding="utf-8")
        assert "Portable Capability Contract" in path.read_text(encoding="utf-8")
        assert not re.search(r"/home/[A-Za-z0-9_.-]+", path.read_text(encoding="utf-8"))

    for required in (
        "README.md",
        "LICENSE",
        "NOTICE.md",
        "shared/capability-contract.md",
        "shared/interaction-contract.md",
        "shared/artifact-contract.md",
    ):
        assert (ROOT / required).exists(), f"missing required file: {required}"

    print(f"validated {len(EXPECTED)} Conductor skills")


if __name__ == "__main__":
    main()
