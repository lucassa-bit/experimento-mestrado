Using `speckit-clarify` because the request explicitly invokes that workflow. I’ll read its instructions and the allowed input files only.

---

I’m applying the experimental constraints over the normal interactive workflow: no hook/script execution and no spec edits, only the three allowed inputs. Next I’m loading the current spec and experiment input files.

---

1. [NEEDS CLARIFICATION] When determining “every active estimator,” is the required estimator set fixed at round start or recalculated dynamically as participants connect/disconnect during the round?

2. [NEEDS CLARIFICATION] If an estimator disconnects after submitting but before reveal, should their stored estimate still be revealed?

3. [NEEDS CLARIFICATION] If the moderator closes voting when no estimates have been submitted, should the system create a reveal event with an empty result or leave the round unrevealed?

4. [NEEDS CLARIFICATION] After reveal, should participants who reconnect or join later be able to see the already revealed estimates for that round?

5. [NEEDS CLARIFICATION] Are spectators allowed to see revealed estimates after the reveal event, or only active estimators and moderators?