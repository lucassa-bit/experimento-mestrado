Using `speckit-clarify` because the request explicitly invokes the clarify workflow. I’ll read its instructions, then only inspect the allowed spec and experiment-input files.

---

The standard clarify skill normally edits the spec after answers, but this experimental instruction forbids answering, resolving, or writing. I’m applying the scan-only part and limiting inputs to the three allowed files.

---

1. [NEEDS CLARIFICATION] Which ZIP code formats must be accepted: 5-digit US ZIP only, ZIP+4, or another postal-code scope?

2. [NEEDS CLARIFICATION] What facility details must each search result display so users can decide which facilities to consider?

3. [NEEDS CLARIFICATION] What should happen if the Geocoding Service is unavailable or cannot return coordinates for a syntactically valid ZIP code?

4. [NEEDS CLARIFICATION] What should happen if the Facility Directory is unavailable or returns incomplete facility data?

5. [NEEDS CLARIFICATION] When multiple eligible facilities have the same calculated distance, what tie-breaker should determine their order?