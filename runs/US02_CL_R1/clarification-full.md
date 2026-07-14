I’ll use the `speckit-clarify` skill and restrict myself to the three files you named. I’ll only inspect the local spec and experiment input, then return the clarification output.

---

The standard clarify workflow normally asks interactively and writes answers back into the spec. Your experimental instructions narrow that: I’m treating this as a read-only ambiguity scan and will not update files or answer anything.

---

1. [NEEDS CLARIFICATION] Which ZIP code formats must be accepted: 5-digit US ZIP only, ZIP+4, or both?

2. [NEEDS CLARIFICATION] What facility details must each result display so users can decide which facilities to consider?

3. [NEEDS CLARIFICATION] What is the authoritative source for facility active/verified status and coordinates?

4. [NEEDS CLARIFICATION] How should facilities with identical calculated distances be ordered?

5. [NEEDS CLARIFICATION] What user-facing behavior is required when a syntactically valid ZIP code cannot be geocoded?