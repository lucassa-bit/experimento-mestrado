I’m using the `speckit-clarify` skill because the request is explicitly a clarification pass over the current spec. I’ll read only the skill instructions and the three allowed local inputs, then return just the clarification output.

---

1. [NEEDS CLARIFICATION] When a place becomes available, should the system skip over ineligible waitlist entries automatically?
   - A: Yes, notify the next eligible attendee and leave skipped entries active
   - B: Yes, notify the next eligible attendee and mark skipped entries inactive
   - C: No, stop until a coordinator removes the ineligible first entry

2. [NEEDS CLARIFICATION] What should happen after a waitlist offer expires or is declined?
   - A: Automatically offer the place to the next eligible attendee
   - B: Require coordinator action before offering to the next attendee
   - C: Leave the place available through normal registration only

3. [NEEDS CLARIFICATION] How should ties be resolved when two attendees join at the same timestamp?
   - A: Use a deterministic secondary sequence number
   - B: Use attendee identifier order
   - C: Treat tied entries as same priority and require coordinator resolution

4. [NEEDS CLARIFICATION] What active statuses must a waitlist entry support?
   - A: Active, offered, enrolled, expired, removed
   - B: Active, offered, removed
   - C: Active and removed only

5. [NEEDS CLARIFICATION] What information must be recorded for coordinator removals?
   - A: Reason only
   - B: Reason, coordinator, and timestamp
   - C: Reason, coordinator, timestamp, and previous waitlist position