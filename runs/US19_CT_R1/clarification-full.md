I’m using the `speckit-clarify` skill because this is a `/speckit.clarify` request. I’ll read its instructions first, then only inspect the allowed input files.

---

The command’s normal workflow includes writing answers back to the spec, but your experimental constraints override that. I’m only reading the three allowed files and will return unresolved questions without answering them.

---

1. [NEEDS CLARIFICATION] When two attendees join at the same timestamp, how should waitlist order be determined? Options: A) deterministic secondary key, B) reject one retry, C) system-generated sequence.

2. [NEEDS CLARIFICATION] After an offer expires or is declined, should the system automatically offer the place to the next eligible attendee? Options: A) yes immediately, B) coordinator triggers manually, C) no specified behavior.

3. [NEEDS CLARIFICATION] If the first waitlisted attendee is no longer eligible when a place becomes available, should the system skip them and notify the next eligible attendee? Options: A) skip automatically, B) require coordinator removal first, C) block until resolved.

4. [NEEDS CLARIFICATION] What minimum information must be recorded for coordinator removals? Answer in <=5 words.

5. [NEEDS CLARIFICATION] What notification channel is required for available-place offers? Options: A) email, B) in-app, C) SMS, D) system-configured channel.