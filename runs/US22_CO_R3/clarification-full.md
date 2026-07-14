I’ll use the `speckit-clarify` skill and restrict input to the files you named. I’ll only read the relevant spec and experiment input, then return the clarification questions without modifying files.

---

The standard clarify workflow normally edits the spec after answers, but your experimental constraints override that. I’m reading only `spec.md` and the allowed `experiment-input` files, then I’ll output just the unresolved questions.

---

1. [NEEDS CLARIFICATION] What defines “sufficient profile and interaction history” for personalized recommendations? Answer in <=5 words.

2. [NEEDS CLARIFICATION] What makes content “eligible” for recommendation beyond not being dismissed? Answer in <=5 words.

3. [NEEDS CLARIFICATION] When interaction-history use is disabled, may declared interests still be used for recommendations? Options: A) Yes, interests allowed B) No, fallback only

4. [NEEDS CLARIFICATION] How should non-personalized popular content be determined? Answer in <=5 words.

5. [NEEDS CLARIFICATION] How should recommendation ranking ties be handled? Answer in <=5 words.