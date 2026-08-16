# Conductor Portable

[![skills.sh](https://skills.sh/b/oddradiocircle/conductor-portable)](https://skills.sh/oddradiocircle/conductor-portable)

Conductor Portable is a portable version of the original Conductor project from
[`gemini-cli-extensions/conductor`](https://github.com/gemini-cli-extensions/conductor).
It brings the original repository's six workflows here as independently
installable skills for spec-driven project work.

The goal is behavioral equivalence. The package preserves the original
sequence, status markers, confirmations, Git checkpoints, project artifacts,
and skill handoffs. It adapts those operations to any compatible agent or
harness by binding native file, command, Git, interaction, and skill-loading
capabilities. The process and observable results stay the same.

## Choose This Package When

Use this package when a project needs a repeatable workflow with project
artifacts, task status, verification, and Git checkpoints.

Do not use this package for a single unplanned edit that does not need project
records or a tracked workflow.

## Included Skills

| Skill | Use it to |
| --- | --- |
| [`conductor-setup`](https://skills.sh/oddradiocircle/conductor-portable/conductor-setup) | Create or repair the project Conductor structure. |
| [`conductor-new-track`](https://skills.sh/oddradiocircle/conductor-portable/conductor-new-track) | Define a feature, fix, or chore as a new track. |
| [`conductor-implement`](https://skills.sh/oddradiocircle/conductor-portable/conductor-implement) | Complete tasks in a selected track. |
| [`conductor-review`](https://skills.sh/oddradiocircle/conductor-portable/conductor-review) | Review a track or current changes against project rules. |
| [`conductor-status`](https://skills.sh/oddradiocircle/conductor-portable/conductor-status) | Read track and task status. |
| [`conductor-revert`](https://skills.sh/oddradiocircle/conductor-portable/conductor-revert) | Revert a track, phase, or task through Git history. |

Install the full package when you use Conductor. Skills hand work to sibling
skills. A single-skill installation does not install handoff dependencies.

## Requirements

Before you install the package, confirm that the host has:

- Node.js with `npx`.
- Git when you will implement, review, or revert work.
- Read and write access to the target project.
- A supported skill installer that accepts an `--agent` value.

The project root is the directory that contains `conductor/`. Run project
commands from that root unless the host has a defined workspace root.

## Install

### Inspect the Package

List the skills before you install them:

```bash
npx skills@latest add oddradiocircle/conductor-portable --full-depth --list
```

The command must list these six names:

```text
conductor-implement
conductor-new-track
conductor-revert
conductor-review
conductor-setup
conductor-status
```

### Install All Skills for One Harness

Install all skills for one harness. This keeps every handoff available.

```bash
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill '*' --agent <harness> --copy --yes
```

Replace `<harness>` with one value from this table. Use one command only.

| Harness | Value for `--agent` |
| --- | --- |
| Claude Code | `claude-code` |
| Codex | `codex` |
| Gemini CLI | `gemini-cli` |
| OpenCode | `opencode` |
| Hermes | `hermes-agent` |

Examples:

```bash
# Claude Code
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill '*' --agent claude-code --copy --yes

# Codex
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill '*' --agent codex --copy --yes

# Gemini CLI
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill '*' --agent gemini-cli --copy --yes

# OpenCode
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill '*' --agent opencode --copy --yes
```

For a named Hermes profile, set `HERMES_HOME` for the command. This installs the
complete package in that profile.

```bash
HERMES_HOME="$HOME/.hermes/profiles/<profile>" \
  npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --global --skill '*' --agent hermes-agent --copy --yes
```

Do not use `--all` for this package. That option selects every available agent,
not one selected harness.

### Install One Skill Only

Use a single-skill install only when you will not need a handoff.

```bash
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill conductor-status --agent <harness> --copy --yes
```

If a required sibling skill is absent, the active skill stops and requests the
complete package. It does not skip the handoff.

### Confirm the Install

List skills in the selected install scope:

```bash
npx skills@latest list --agent <harness> --json
```

For a named Hermes profile, use the same profile root when you verify it:

```bash
HERMES_HOME="$HOME/.hermes/profiles/<profile>" hermes skills list
```

Confirm that all six `conductor-*` skills are present after a full install.

## Start a Project

1. Open the target project in your selected harness.
2. Load `conductor-setup` by its installed skill name.
3. Complete the setup prompts and verify the created files.
4. Load `conductor-new-track` to define the first unit of work.
5. Load `conductor-implement` to complete the selected track.
6. Use `conductor-status` to inspect progress.
7. Use `conductor-review` before you close important work.
8. Use `conductor-revert` only when you need to undo a recorded unit of work.

Use the skill selector or loader provided by the active harness. Do not replace
a missing capability with a skipped workflow step.

## Project Files

`conductor-setup` creates or resumes this project-local structure:

```text
conductor/
├── index.md
├── product.md
├── product-guidelines.md
├── tech-stack.md
├── workflow.md
├── tracks.md
├── code_styleguides/
├── tracks/
│   └── <track-id>/
│       ├── index.md
│       ├── metadata.json
│       ├── spec.md
│       └── plan.md
└── archive/
```

Track markers have fixed meanings:

- `[ ]` means pending.
- `[~]` means in progress.
- `[x]` means complete.

Links in the project index, track indexes, and tracks registry must stay
relative to the file that contains the link.

## Harness Behavior

A compatible harness provides project inspection, file reading and editing,
command execution, Git operations, user interaction, skill loading, skill
installation, and result verification.

The package uses three roots:

- `<project-root>` is the active project directory.
- `<skill-root>` contains the active `SKILL.md` and its bundled resources.
- `<skills-root>` contains installed sibling skills.

Project artifacts stay under `<project-root>`. Bundled resources resolve from
`<skill-root>`. A handoff loads a sibling from `<skills-root>` when the host
cannot load it by name.

Read the full contracts when you adapt the package to another harness:

- [Artifact contract](shared/artifact-contract.md)
- [Capability contract](shared/capability-contract.md)
- [Interaction contract](shared/interaction-contract.md)

## Safety and Git Rules

The skills inspect project state before they change it. They keep pre-existing
changes separate from review fixes. They stage only the paths needed for a
commit and verify the staged result before they commit.

Destructive actions require explicit confirmation. A hard reset is available
only when the protocol proves that it is safe to offer. External skills require
an immutable revision, validation, approval, and a host-scoped install.

## Verify a Source Checkout

Run these checks from the repository root:

```bash
python3 tests/validate_package.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m py_compile skills/conductor-setup/scripts/resume.py tests/*.py
git diff --check
```

The package validator must report six valid skills. The test suite must finish
without failures.

## Verify a Published Package

Use a temporary directory. List the remote package, then install it for one
harness.

```bash
npx skills@latest add oddradiocircle/conductor-portable --full-depth --list

npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill '*' --agent hermes-agent --copy --yes
```

Open each skill page from the table above. Confirm that the page returns a
successful response and names the expected skill.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before you submit a change. Keep a
change limited to its purpose. Add a regression test for each fixed behavior.

## Attribution

Conductor Portable is derived from
[Conductor](https://github.com/gemini-cli-extensions/conductor). See
[NOTICE.md](NOTICE.md) and [LICENSE](LICENSE) for license and attribution
details.
