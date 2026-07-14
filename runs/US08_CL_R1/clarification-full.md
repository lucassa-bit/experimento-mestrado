Using `speckit-clarify` because the request explicitly invokes the clarification workflow. I’ll read the skill instructions and the allowed local inputs only.

---

The experiment instructions narrow the normal workflow: I’m not running prerequisite scripts, hooks, planning, or writes. I’m only inspecting `spec.md` plus the permitted experiment input files to produce unresolved questions.

---

1. [NEEDS CLARIFICATION] When an active estimator disconnects before submitting, should they be immediately excluded from the required completion count, or should the round continue waiting until the moderator closes voting?

2. [NEEDS CLARIFICATION] Are revealed estimates visible to all participants including spectators, or only to connected estimators and moderators?

3. [NEEDS CLARIFICATION] If the moderator closes voting when no estimates have been submitted, should the system reveal an empty result, cancel the round, or prevent closure?

4. [NEEDS CLARIFICATION] If an estimator submitted an estimate, disconnects, and later reconnects before reveal, should their stored estimate remain included in the reveal?

5. [NEEDS CLARIFICATION] What should happen when a participant attempts to submit or change an estimate after reveal: reject silently, show an error, or require starting a new round first?