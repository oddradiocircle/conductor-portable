# Portable Capability Contract

This contract defines how the canonical Conductor protocols bind to an agent or
harness. It does not replace any Conductor protocol step. It only translates
host-specific operations into equivalent capabilities.

## Required Capabilities

A compatible host must provide, directly or through an equivalent mechanism:

- **Project inspection:** identify the current project root and inspect files.
- **File reading:** read text files and report missing or unreadable files.
- **File creation:** create directories and write text files.
- **File editing:** make targeted edits while preserving unrelated content.
- **Command execution:** execute project commands and return exit status and
  output.
- **Git operations:** inspect status/history and perform explicitly approved Git
  actions.
- **User interaction:** ask Yes/No, single-choice, multiple-choice, and open
  questions.
- **Protocol loading:** load another Conductor protocol when a handoff is
  required, or continue its instructions in the current session when the host
  has no module loader.
- **Result verification:** inspect the resulting files, command status, and Git
  state after every state-changing operation.

## Binding Rules

1. The active project root is the current working directory unless the host has
   an explicit workspace-root concept.
2. Relative paths in the canonical protocols are resolved from that root.
3. A host tool name mentioned by an original example may be replaced by the
   host's equivalent capability. The observable result and the protocol's
   decision gates must remain unchanged.
4. A host must not silently skip a required operation because its interface is
   different. It must use an equivalent capability or stop and report the
   missing capability.
5. A protocol handoff means loading the corresponding file under
   `skills/<protocol-name>/SKILL.md`; if loading is unavailable, execute that
   protocol as part of the current session.
6. File paths and artifact formats defined by Conductor are normative. Agent
   installation directories are not project artifact paths.
7. Destructive actions still require the explicit confirmation required by the
   canonical protocol and by the host's safety model.

## Failure Handling

Every capability call is a checkpoint. On failure, the agent must inspect the
reported error, attempt the canonical self-correction once when the protocol
allows it, and otherwise halt with the failure exposed to the user.
