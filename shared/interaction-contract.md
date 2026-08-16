# Portable Interaction Contract

Conductor's user interaction semantics are canonical and en-US. The visual
presentation may vary by host, but the decision barrier must not.

## Question Types

- **Yes/No:** a binary approval or rejection.
- **Single-choice:** exactly one option from a suggested list.
- **Multiple-choice:** zero or more options from a suggested list.
- **Open question:** free-form user input when predefined options would distort
  the requested information.

## Host Bindings

1. Use a native structured question interface when the host provides one.
2. Otherwise, render the same question as formatted text.
3. In text-only sessions, ask questions sequentially and wait after each one.
4. When the canonical protocol requires an `Other` option, preserve it.
5. Do not treat a user-facing language translation as a protocol change. The
   canonical text and option semantics remain en-US.
6. Never infer approval from silence, a failed interaction, or an ambiguous
   answer.

## Confirmation Barriers

The host must pause before:

- creating or modifying crucial project infrastructure;
- committing changes when the protocol requires confirmation;
- installing external skills;
- applying review fixes;
- deleting or archiving a track;
- using a destructive Git strategy.
