I’ll use the `speckit-clarify` skill and only inspect the allowed local files before producing the clarification output.

---

I’ve loaded the skill instructions. Because this is experimental collection mode, I’ll follow the user’s stricter constraints: no spec edits, no prerequisite scripts, no hooks, and no inferred answers.

---

1. [NEEDS CLARIFICATION] Is the required estimator set fixed at round start, or recalculated from Presence Service active estimators at reveal-check time?

2. [NEEDS CLARIFICATION] If an estimator submitted an estimate and then disconnects before reveal, should their stored estimate still be revealed?

3. [NEEDS CLARIFICATION] Who should receive revealed estimates: active estimators only, all connected participants including spectators, or all participants who later view the round?

4. [NEEDS CLARIFICATION] What should happen when the moderator closes voting with no submitted estimates?

5. [NEEDS CLARIFICATION] Are estimators allowed to change their hidden estimate before the reveal condition is met?