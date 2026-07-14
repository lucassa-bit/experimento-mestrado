I’m using the `speckit-clarify` skill because the request explicitly invokes `/speckit.clarify`. I’ll read its instructions, then inspect only the allowed files.

---

The skill’s normal workflow includes interactive answers and spec edits, but your experimental constraints override that: I’ll only identify unresolved clarification questions from the allowed documents and won’t modify files.

---

1. [NEEDS CLARIFICATION] Is the set of required active estimators fixed at round start, or recalculated from Presence Service at each submission/reveal check?

2. [NEEDS CLARIFICATION] If an estimator disconnects after submitting but before reveal, should their stored estimate still be included in the reveal event?

3. [NEEDS CLARIFICATION] If an estimator reconnects before reveal after previously being disconnected and excluded, should they become required for completion again?

4. [NEEDS CLARIFICATION] Before reveal, may an estimator replace their own submitted estimate, or is only one immutable pre-reveal submission allowed?

5. [NEEDS CLARIFICATION] When the moderator closes voting with no submitted estimates, should the system broadcast an empty reveal event or keep the round unrevealed?