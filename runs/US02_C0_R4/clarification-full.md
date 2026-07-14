I’m using the `speckit-clarify` skill because the request is explicitly a Spec Kit clarification pass. I’ll read its instructions, then only inspect the allowed files in this run folder.

---

The experiment instructions narrow the normal clarify workflow: no interactive answering, no outside context, and no file updates. I’m treating this as a read-only ambiguity scan and will return only the unresolved questions.

---

1. [NEEDS CLARIFICATION] What facility information must each search result display so the user can decide which facilities to consider? Answer in <=5 words.

2. [NEEDS CLARIFICATION] What ZIP code formats are valid for this feature?
A. 5-digit US ZIP only  
B. 5-digit and ZIP+4  
C. Any postal code format  

3. [NEEDS CLARIFICATION] If multiple facilities have the same calculated distance, how should they be ordered? Answer in <=5 words.

4. [NEEDS CLARIFICATION] What should happen when ZIP code geocoding fails for a syntactically valid ZIP code?
A. Show invalid ZIP message  
B. Show location unavailable message  
C. Show no-results message  

5. [NEEDS CLARIFICATION] What is the authoritative source for facility active and verified status? Answer in <=5 words.