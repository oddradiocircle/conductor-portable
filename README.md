# Conductor Portable

[![skills.sh](https://skills.sh/b/oddradiocircle/conductor-portable)](https://skills.sh/oddradiocircle/conductor-portable)

Portable, en-US canonical Conductor protocols for spec-driven development.

This project preserves the six Conductor protocols and their project artifacts
while replacing assumptions about a particular agent or harness with a small
capability contract. The canonical workflow remains in English (en-US). Each
host binds the abstract capabilities to its own tools and skill directories.

## Included Skills

- [`conductor-setup`](https://skills.sh/oddradiocircle/conductor-portable/conductor-setup)
- [`conductor-new-track`](https://skills.sh/oddradiocircle/conductor-portable/conductor-new-track)
- [`conductor-implement`](https://skills.sh/oddradiocircle/conductor-portable/conductor-implement)
- [`conductor-review`](https://skills.sh/oddradiocircle/conductor-portable/conductor-review)
- [`conductor-status`](https://skills.sh/oddradiocircle/conductor-portable/conductor-status)
- [`conductor-revert`](https://skills.sh/oddradiocircle/conductor-portable/conductor-revert)

## Installation

List the available skills:

```bash
npx skills@latest add oddradiocircle/conductor-portable --full-depth --list
```

The recommended installation installs all six skills so every protocol handoff
is available:

```bash
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --all --copy -y
```

Advanced: install one protocol only:

```bash
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill conductor-setup --copy -y
```

A single-skill installation does not install handoff dependencies. If a sibling
protocol is unavailable, Conductor halts and asks for the complete package
instead of silently skipping the handoff.

For Hermes, use the technical agent identifier `hermes-agent`:

```bash
HERMES_HOME="$HOME/.hermes/profiles/<profile>" \
  npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --global --agent hermes-agent --skill conductor-setup \
  --copy --yes
```

## Usage

The protocols operate on a project-local `conductor/` directory. Start with
`conductor-setup`, then use `conductor-new-track`, `conductor-implement`,
`conductor-status`, `conductor-review`, and `conductor-revert` as needed.

The canonical artifact model is documented in
[`shared/artifact-contract.md`](shared/artifact-contract.md). The host-neutral
execution rules are documented in
[`shared/capability-contract.md`](shared/capability-contract.md) and
[`shared/interaction-contract.md`](shared/interaction-contract.md).

## Design Guarantees

- The normative protocol and artifact language remains canonical en-US.
- The six protocols remain independently discoverable and installable.
- The project root is the active project directory; Conductor artifacts stay
  under `conductor/`.
- Host-specific tool names are bindings, not workflow changes.
- The original decision gates, status markers, Git history requirements, and
  verification checkpoints are preserved.
- Optional external skills are resolved from immutable Git revisions, validated,
  and installed through the active host rather than a hardcoded directory.

## Verification

Run the network-free package and behavior checks:

```bash
python3 tests/validate_package.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Attribution

Conductor Portable is derived from
[Conductor](https://github.com/gemini-cli-extensions/conductor), licensed under
the Apache License, Version 2.0. See [`NOTICE.md`](NOTICE.md) and
[`LICENSE`](LICENSE).
