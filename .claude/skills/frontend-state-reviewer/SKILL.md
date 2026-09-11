---
name: frontend-state-reviewer
description: "Review UI state for source of truth, derived data and sync bugs. Use when the interface shows stale data or state is scattered."
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Goal

One source of truth per fact, and nothing stored that can be derived.

## What to look for

- **Duplicated truth**: the same fact in two places, kept in sync by hand.
  This is the usual cause of "it shows the old value".
- **Derived data stored**: a total, a filtered list, or a flag that could be
  computed. Storing it creates a second thing to invalidate.
- **The DOM as state**: reading a value back out of an input or a class name
  instead of from the state that rendered it.
- **Effects that fight**: two effects writing the same value, or an effect
  whose dependency list hides a stale closure.
- **Server vs client**: cached response treated as truth after a mutation.
- **Reset gaps**: state that survives a navigation it should not, or is
  cleared when the user expected it kept.

## Output

A table of facts: where each one lives, who writes it, and who should. Then
the findings, each with the concrete stale-data scenario it produces.
