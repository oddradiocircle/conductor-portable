"""Behavior tests for the bundled setup resumption helper."""

from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/conductor-setup/scripts/resume.py"
SPEC = importlib.util.spec_from_file_location("conductor_resume", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@contextmanager
def working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


class ResumeBehaviorTests(unittest.TestCase):
    def create_core(self, conductor: Path) -> None:
        for name in ("product.md", "product-guidelines.md", "tech-stack.md", "workflow.md"):
            (conductor / name).write_text(name, encoding="utf-8")
        guides = conductor / "code_styleguides"
        guides.mkdir()
        (guides / "general.md").write_text("# General", encoding="utf-8")

    def test_index_alone_is_not_complete(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            (conductor / "index.md").write_text("# Project Context", encoding="utf-8")
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertFalse(result["setup_complete"])
        self.assertEqual(result["next_step"]["file"], "product.md")

    def test_empty_styleguide_directory_is_not_complete(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            for name in ("product.md", "product-guidelines.md", "tech-stack.md", "workflow.md", "index.md"):
                (conductor / name).write_text(name, encoding="utf-8")
            (conductor / "code_styleguides").mkdir()
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertFalse(result["setup_complete"])
        self.assertEqual(result["next_step"]["file"], "code_styleguides")

    def test_complete_core_without_index_resumes_at_index(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            self.create_core(conductor)
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertFalse(result["setup_complete"])
        self.assertEqual(result["next_step"], {"step": "Project Index", "file": "index.md"})

    def test_complete_setup_requires_every_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            self.create_core(conductor)
            (conductor / "index.md").write_text("# Project Context", encoding="utf-8")
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertTrue(result["setup_complete"])
        self.assertIsNone(result["next_step"])

    def test_directory_named_markdown_is_not_a_styleguide(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            self.create_core(conductor)
            (conductor / "code_styleguides/general.md").unlink()
            (conductor / "code_styleguides/not-a-file.md").mkdir()
            (conductor / "index.md").write_text("# Project Context", encoding="utf-8")
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertFalse(result["setup_complete"])
        self.assertFalse(result["checklist"]["code_styleguides"])

    def test_symlink_escape_is_not_a_valid_core_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as raw, tempfile.TemporaryDirectory() as outside:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            self.create_core(conductor)
            external = Path(outside) / "product.md"
            external.write_text("outside", encoding="utf-8")
            (conductor / "product.md").unlink()
            (conductor / "product.md").symlink_to(external)
            (conductor / "index.md").write_text("# Project Context", encoding="utf-8")
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertFalse(result["setup_complete"])
        self.assertFalse(result["checklist"]["product.md"])

    def test_contained_symlink_is_a_valid_core_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            conductor = Path(raw) / "conductor"
            conductor.mkdir()
            self.create_core(conductor)
            target = conductor / "product-source.md"
            target.write_text("inside", encoding="utf-8")
            (conductor / "product.md").unlink()
            (conductor / "product.md").symlink_to(target.name)
            (conductor / "index.md").write_text("# Project Context", encoding="utf-8")
            with working_directory(Path(raw)):
                result = MODULE.determine_resumption()
        self.assertTrue(result["setup_complete"])


if __name__ == "__main__":
    unittest.main()
