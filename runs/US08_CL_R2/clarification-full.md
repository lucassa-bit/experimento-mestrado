Using the `speckit-clarify` skill because the request explicitly invokes clarification output for the current spec. I’ll read only the allowed local files and keep the result to unresolved questions.

---

The command’s experimental constraints override the normal interactive/update workflow: I’m not going to run prerequisite scripts, hooks, or modify the spec. I’m only reading `spec.md` and the allowed experiment input files.

---

1. [NEEDS CLARIFICATION] Should revealed estimates be visible to spectators as well as estimators, or only to active estimators?

2. [NEEDS CLARIFICATION] If an estimator disconnects after submitting but before reveal, should their submitted estimate still be revealed?

3. [NEEDS CLARIFICATION] If an active estimator disconnects before submitting, should the system immediately exclude them and reveal once remaining active estimators have submitted?

4. [NEEDS CLARIFICATION] When the moderator closes voting with no submitted estimates, should the round reveal an empty result or remain unrevealed?

5. [NEEDS CLARIFICATION] Before reveal, may an estimator revise their hidden estimate, or is only the first submission accepted?