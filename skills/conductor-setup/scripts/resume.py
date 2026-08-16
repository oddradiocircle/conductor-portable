"""Determines the next unblocked setup step in the Conductor workflow."""

import json
import sys
from pathlib import Path


def _resolve_inside(path, root, expected_type):
  """Resolve path and require the target to remain inside root."""
  try:
    resolved_root = root.resolve(strict=True)
    resolved_path = path.resolve(strict=True)
  except (FileNotFoundError, OSError, RuntimeError):
    return None

  if not resolved_path.is_relative_to(resolved_root):
    return None
  if expected_type == "file" and not resolved_path.is_file():
    return None
  if expected_type == "directory" and not resolved_path.is_dir():
    return None
  return resolved_path


def determine_resumption():
  """Checks existing setup artifacts and returns the next unblocked step."""
  project_root = Path.cwd().resolve()
  conductor_path = project_root / "conductor"
  conductor_dir = _resolve_inside(conductor_path, project_root, "directory")
  files = ("product.md", "product-guidelines.md", "tech-stack.md", "workflow.md")

  checklist = {
      filename: bool(
          conductor_dir
          and _resolve_inside(conductor_dir / filename, conductor_dir, "file")
      )
      for filename in files
  }
  styleguide_dir = (
      _resolve_inside(conductor_dir / "code_styleguides", conductor_dir, "directory")
      if conductor_dir
      else None
  )
  checklist["code_styleguides"] = (
      bool(styleguide_dir)
      and any(
          entry.suffix == ".md"
          and bool(_resolve_inside(entry, conductor_dir, "file"))
          for entry in styleguide_dir.iterdir()
      )
  )

  index_exists = bool(
      conductor_dir
      and _resolve_inside(conductor_dir / "index.md", conductor_dir, "file")
  )
  setup_complete = index_exists and all(checklist.values())

  next_step = None

  chain = [
      ("product.md", "Product Definition"),
      ("product-guidelines.md", "Product Guidelines"),
      ("tech-stack.md", "Technology Stack"),
      ("code_styleguides", "Code Style Guides"),
      ("workflow.md", "Workflow Configuration"),
  ]

  for filename, step_name in chain:
    if not checklist[filename]:
      next_step = {
          "step": step_name,
          "file": filename,
      }
      break

  if next_step is None and not index_exists:
    next_step = {
        "step": "Project Index",
        "file": "index.md",
    }

  return {
      "setup_complete": setup_complete,
      "checklist": checklist,
      "next_step": next_step,
  }


if __name__ == "__main__":
  result = determine_resumption()
  print(json.dumps(result, indent=2))
  sys.exit(0)
