I’ll use the `speckit-clarify` skill and restrict myself to the specified files. I’ll only read the current spec and experiment input, then return the clarification output.

---

The skill’s normal flow writes accepted answers back into the spec, but your experimental constraints override that: I will not ask interactively, answer anything, or write files. I’m scanning only the allowed inputs for unresolved, high-impact questions.

---

1. [NEEDS CLARIFICATION] When two attendees have the same successful entry timestamp, what deterministic tie-breaker should define waitlist order? Answer in <=5 words.

2. [NEEDS CLARIFICATION] After a waitlist offer expires or is declined, should the system automatically offer the place to the next eligible attendee? Answer: Yes/No.

3. [NEEDS CLARIFICATION] If the first waitlisted attendee is no longer eligible when a place becomes available, should the system skip them automatically or require coordinator removal first? Answer: Skip automatically / Coordinator removal.

4. [NEEDS CLARIFICATION] What should happen when an attendee attempts to join the same waitlist more than once? Answer: Reject silently / Show existing entry / Error message.

5. [NEEDS CLARIFICATION] What minimum status must be tracked for each available-place offer? Answer in <=5 words.