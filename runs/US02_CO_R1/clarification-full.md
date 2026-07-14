I’m using the `speckit-clarify` skill because the request explicitly invokes `/speckit.clarify`. I’ll read its instructions, then inspect only the allowed local files.

---

The standard skill is interactive and writes accepted answers back to the spec, but your experimental constraints are narrower: I’ll only read the three allowed inputs and return the unresolved clarification questions, without answering or editing anything.

---

1. [NEEDS CLARIFICATION] Should search results require facilities to be both active and verified, or only active? Answer in <=5 words.

2. [NEEDS CLARIFICATION] What ZIP code formats are valid for search input: 5-digit only, ZIP+4, or both? Answer in <=5 words.

3. [NEEDS CLARIFICATION] What facility details must each result display so users can decide which facilities to consider? Answer in <=5 words.

4. [NEEDS CLARIFICATION] How should facilities with identical calculated distances be ordered? Answer in <=5 words.

5. [NEEDS CLARIFICATION] What should happen when a syntactically valid ZIP code cannot be converted to coordinates? Answer in <=5 words.