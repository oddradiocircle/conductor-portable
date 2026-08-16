# Conductor Artifact Contract

The following project-local structure and names are normative for all compatible
agents and harnesses:

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

A host may store the skill package anywhere its installation system requires,
but it must resolve the project artifacts above relative to the active project
root. Host installation directories are not substitutes for `conductor/`.

Status markers are also normative:

- `[ ]` pending;
- `[~]` in progress;
- `[x]` complete.

Links in `index.md`, track indexes, and the tracks registry must be valid
relative links from the file containing them.
