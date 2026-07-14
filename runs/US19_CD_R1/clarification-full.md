I’ll use the `speckit-clarify` skill and restrict inputs to the files you named. I’m only going to inspect those files and return the unresolved clarification questions.

---

The standard clarify workflow normally edits the spec after answers, but your experimental instructions override that. I’m reading only the current spec and the allowed experiment input files, then I’ll emit the questions without answering or integrating anything.

---

1. [NEEDS CLARIFICATION] When the first eligible attendee’s 24-hour offer expires, should the system automatically offer the place to the next eligible attendee?

2. [NEEDS CLARIFICATION] If two attendees successfully join at the same timestamp, what tie-breaker determines waitlist order?

3. [NEEDS CLARIFICATION] What status lifecycle should a waitlist entry support beyond “active” and “removed”?

4. [NEEDS CLARIFICATION] What information must be recorded for an available-place offer notification?

5. [NEEDS CLARIFICATION] What should happen if the first waitlisted attendee becomes ineligible before a place becomes available?