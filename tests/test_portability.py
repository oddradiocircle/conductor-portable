"""Regression tests for Conductor's host-neutral protocol bindings."""

from __future__ import annotations

import re
import unittest
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SKILLS = tuple(sorted((ROOT / "skills").glob("*/SKILL.md")))


class PortabilityContractTests(unittest.TestCase):
    def test_every_skill_is_self_contained_about_canonical_language_and_roots(self) -> None:
        for path in SKILLS:
            text = path.read_text(encoding="utf-8")
            with self.subTest(skill=path.parent.name):
                self.assertIn("canonical en-US", text)
                self.assertIn("<skill-root>", text)
                self.assertIn("<skills-root>", text)
                self.assertIn("explicitly designates", text)
                self.assertIn("higher-priority safety", text)
                self.assertIn("role-limited", text)
                self.assertIn("after normalization", text)
                self.assertIn("symlink", text)
                self.assertIn("absolute paths supplied by artifacts", text)
                self.assertIn("structured argument vectors", text)
                self.assertIn("NUL-delimited output", text)
                self.assertNotIn("skills/<skill-name>/SKILL.md", text)

    def test_protocols_do_not_hardcode_host_installation_paths(self) -> None:
        forbidden = (
            ".agents/skills/",
            ".agents/extensions/",
            ".geminiignore",
            "/conductor:",
        )
        for path in SKILLS:
            text = path.read_text(encoding="utf-8")
            for value in forbidden:
                with self.subTest(skill=path.parent.name, value=value):
                    self.assertNotIn(value, text)

    def test_setup_resolves_bundled_resources_from_skill_root(self) -> None:
        text = (ROOT / "skills/conductor-setup/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("<skill-root>/scripts/resume.py", text)
        self.assertIn("<skill-root>/assets/code_styleguides/", text)
        self.assertIn("<skill-root>/assets/workflow.md", text)
        self.assertIn("<skill-root>/assets/catalog.md", text)
        self.assertNotIn("python3 scripts/resume.py", text)

    def test_setup_and_new_track_never_stage_the_whole_conductor_tree(self) -> None:
        for relative in (
            "skills/conductor-setup/SKILL.md",
            "skills/conductor-new-track/SKILL.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            normalized = " ".join(text.split())
            with self.subTest(path=relative):
                self.assertNotIn("Stage the entire `conductor/` directory", text)
                self.assertIn("working tree baseline", normalized)
                self.assertIn("pre-existing changes", normalized)
                self.assertIn("Stage only", normalized)
                self.assertIn("staged diff contains no other paths", normalized)

    def test_implement_never_commits_a_dirty_baseline(self) -> None:
        text = (ROOT / "skills/conductor-implement/SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        self.assertIn("working tree baseline", normalized)
        self.assertIn("If the baseline is dirty", normalized)
        self.assertIn("Stage only the Tracks Registry", normalized)
        self.assertIn("Stage only the modified project documents", normalized)
        self.assertIn("staged diff contains no other paths", normalized)

    def test_external_skill_installation_is_pinned_and_host_neutral(self) -> None:
        for relative in (
            "skills/conductor-setup/SKILL.md",
            "skills/conductor-new-track/SKILL.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(path=relative):
                self.assertIn("immutable revision", text)
                self.assertIn("host's workspace-scoped skill installer", text)
                self.assertIn("frontmatter", text)
                self.assertIn("official publisher", text)
                self.assertIn("complete skill tree", text)
                self.assertIn("does not establish safety", text)
                self.assertIn("repository owner", text)
                self.assertIn("treat it as 3p", text)
                self.assertIn("reject every symlink", text)
                self.assertIn("regular files", text)
                self.assertIn("without executing", text)
                self.assertNotIn("verified Conductor skill", text)
                self.assertNotIn("for your safety", text)
                self.assertNotIn("curl -sSL", text)
                self.assertLess(
                    text.index("**Validate Before Approval:**"),
                    text.index("**User Approval:**"),
                )

    def test_catalog_entries_are_immutable_and_well_formed(self) -> None:
        for path in (
            ROOT / "skills/conductor-setup/assets/catalog.md",
            ROOT / "skills/conductor-new-track/assets/catalog.md",
        ):
            text = path.read_text(encoding="utf-8")
            entries = text.split("\n### ")[1:]
            self.assertGreater(len(entries), 0)
            self.assertNotIn("raw.githubusercontent.com", text)
            self.assertNotRegex(text, r"/(?:main|master)/")
            self.assertIn("**Party semantics**", text)
            self.assertIn("- **Publisher**:", text)
            self.assertIn("\n### firebase-data-connect\n", text)
            self.assertNotIn("\n### firebase-data-connect-basics\n", text)
            for entry in entries:
                title = entry.splitlines()[0]
                with self.subTest(catalog=path, skill=title):
                    self.assertRegex(entry, r"(?m)^- \*\*Repository\*\*: [\w.-]+/[\w.-]+$")
                    self.assertRegex(entry, r"(?m)^- \*\*Publisher\*\*: [\w .-]+$")
                    self.assertRegex(entry, r"(?m)^- \*\*Revision\*\*: `[0-9a-f]{40}`$")
                    match = re.search(r"(?m)^- \*\*Path\*\*: `([^`]+/SKILL\.md)`$", entry)
                    if match is None:
                        self.fail("catalog entry has no valid skill path")
                    catalog_path = match.group(1)
                    parsed = PurePosixPath(catalog_path)
                    self.assertFalse(parsed.is_absolute())
                    self.assertNotIn("\\", catalog_path)
                    self.assertNotIn("..", parsed.parts)
                    self.assertNotIn(".", parsed.parts)
                    self.assertEqual(parsed.parts[0], "skills")
                    self.assertEqual(parsed.name, "SKILL.md")

    def test_status_parser_covers_every_normative_track_state(self) -> None:
        text = (ROOT / "skills/conductor-status/SKILL.md").read_text(encoding="utf-8")
        start = text.index("**Parsing Logic:**")
        parser_rule = text[start : text.index("For each track", start)]
        for marker in ("[ ]", "[~]", "[x]"):
            with self.subTest(marker=marker):
                self.assertIn(marker, parser_rule)

    def test_status_treats_missing_tracks_as_an_empty_project_plan(self) -> None:
        text = (ROOT / "skills/conductor-status/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("not a damaged setup", text)
        self.assertIn("zero tracks", text)
        self.assertIn("conductor-new-track", text)

    def test_hard_reset_requires_all_destructive_operation_gates(self) -> None:
        text = (ROOT / "skills/conductor-revert/SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        self.assertIn("working tree and index are clean", normalized)
        self.assertIn("contiguous suffix ending at `HEAD`", normalized)
        self.assertIn("not published to an upstream", normalized)
        self.assertIn("backup branch", normalized)
        self.assertIn("verify the backup ref", normalized)
        self.assertIn("RESET <branch> TO <base_sha>", normalized)
        self.assertIn("re-check every eligibility gate immediately before", normalized)

    def test_revert_requires_a_clean_baseline_for_every_strategy(self) -> None:
        text = (ROOT / "skills/conductor-revert/SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        self.assertIn("Before either strategy", normalized)
        self.assertIn("HALT before any revert command", normalized)
        self.assertIn("Stage only the corrected Implementation Plan", normalized)

    def test_review_redacts_secrets_and_preserves_preexisting_changes(self) -> None:
        text = (ROOT / "skills/conductor-review/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("[REDACTED]", text)
        self.assertIn("pre-existing changes", text)
        self.assertIn("only files changed by the review fixes", text)
        self.assertIn("git diff --cached", text)
        self.assertIn("baseline patches", text)

    def test_review_uses_content_complete_baseline_and_fail_safe_commits(self) -> None:
        text = (ROOT / "skills/conductor-review/SKILL.md").read_text(encoding="utf-8")
        lower = " ".join(text.lower().split())
        self.assertIn("--untracked-files=all", text)
        self.assertIn("NUL-delimited", text)
        self.assertIn("untracked content manifest", text)
        self.assertIn("compare the current staged patch", lower)
        self.assertIn("do not infer changes from porcelain status", lower)
        self.assertIn("if the baseline was dirty", lower)
        self.assertIn("do not stage, commit, archive, or delete", lower)
        self.assertIn("verify the baseline patches and untracked manifest are unchanged", lower)

    def test_review_allows_current_changes_before_first_track(self) -> None:
        text = (ROOT / "skills/conductor-review/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("track-based review is unavailable", text)
        self.assertIn("reviewing current changes remains available", text)
        self.assertIn("**Current changes:**", text)
        self.assertIn("git diff --cached", text)
        self.assertIn("untracked files", text)

    def test_review_archive_stages_source_destination_and_registry(self) -> None:
        text = (ROOT / "skills/conductor-review/SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        self.assertIn("source track path", normalized)
        self.assertIn("destination archived track path", normalized)
        self.assertIn("Tracks Registry", normalized)
        self.assertIn("source deletion and destination addition or rename", normalized)

    def test_readme_states_language_and_handoff_installation_contract(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("canonical workflow remains in English (en-US)", text)
        self.assertIn("recommended installation", text.lower())
        self.assertIn("does not install handoff dependencies", text)


if __name__ == "__main__":
    unittest.main()
