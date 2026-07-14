I’m using the speckit-clarify skill because the request explicitly invokes the clarify workflow. I’ll read its instructions first, then only inspect the allowed files.

---

I’ll follow the experimental constraints over the normal interactive/write-back parts of the skill: no edits, no prerequisite script side effects, and no outside context. I’m reading only `spec.md` plus the allowed experiment input files.

---

1. [NEEDS CLARIFICATION] Which ZIP code formats must be accepted?
   - A: 5-digit US ZIP codes only
   - B: 5-digit US ZIP codes and ZIP+4
   - C: Any postal code accepted by the Geocoding Service

2. [NEEDS CLARIFICATION] What information must each recycling facility result display?
   - A: Facility name, distance, and address
   - B: Facility name and distance only
   - C: Facility name, distance, address, and contact details
   - Short: Answer in <=5 words

3. [NEEDS CLARIFICATION] How should facilities with identical calculated distance be ordered?
   - A: Alphabetically by facility name
   - B: By most recently verified first
   - C: Stable directory order
   - Short: Answer in <=5 words

4. [NEEDS CLARIFICATION] What should happen when the Geocoding Service or Facility Directory is unavailable?
   - A: Show a temporary error and ask the user to retry
   - B: Show no results
   - C: Use cached data if available, otherwise show an error

5. [NEEDS CLARIFICATION] What geographic coverage is required for searches?
   - A: United States ZIP codes only
   - B: Any ZIP/postal code supported by the geocoder
   - C: Only areas present in the Facility Directory