# Conductor Portable

[![skills.sh](https://skills.sh/b/oddradiocircle/conductor-portable)](https://skills.sh/oddradiocircle/conductor-portable)

Portable Conductor protocols for spec-driven development.

This project preserves the six Conductor protocols and their project artifacts
while replacing assumptions about a particular agent or harness with a small
capability contract. Host adapters provide the binding to the tools available
in each environment.

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

Install all six skills for a supported agent:

```bash
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --all --copy -y
```

Install one protocol:

```bash
npx skills@latest add oddradiocircle/conductor-portable \
  --full-depth --skill conductor-setup --copy -y
```

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

- The six protocols remain independently discoverable and installable.
- The project root is the active project directory; Conductor artifacts stay
  under `conductor/`.
- Host-specific tool names are bindings, not workflow changes.
- The original decision gates, status markers, Git history requirements, and
  verification checkpoints are preserved.

## Attribution

Conductor Portable is derived from
[Conductor](https://github.com/gemini-cli-extensions/conductor), licensed under
the Apache License, Version 2.0. See [`NOTICE.md`](NOTICE.md) and
[`LICENSE`](LICENSE).
