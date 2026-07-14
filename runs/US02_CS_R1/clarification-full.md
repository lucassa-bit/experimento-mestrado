Using `speckit-clarify` to follow the project’s clarification workflow constraints.

---

1. [NEEDS CLARIFICATION] Which ZIP code formats are valid search inputs? Options: A) 5-digit US ZIP only, B) 5-digit ZIP and ZIP+4, C) Any postal code supported by geocoding service.

2. [NEEDS CLARIFICATION] What facility details must appear in each result item? Answer in <=5 words.

3. [NEEDS CLARIFICATION] If multiple facilities have the same distance, how should ties be ordered? Options: A) Alphabetically by facility name, B) Directory order, C) No guaranteed order.

4. [NEEDS CLARIFICATION] What should happen if the Geocoding Service or Facility Directory is unavailable? Options: A) Show temporary error, B) Show no results, C) Retry automatically then error.

5. [NEEDS CLARIFICATION] Should users be able to change the 25-mile search radius? Options: A) Fixed at 25 miles, B) User-selectable radius, C) Configurable but not user-facing.