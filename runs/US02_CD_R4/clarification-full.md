Using `speckit-clarify` because the request is the clarification workflow. I’ll read its instructions, then only the allowed local inputs.

---

The experiment instructions narrow the normal clarify workflow: I’m skipping hooks, prerequisite scripts, and spec edits, and I’ll only read the three permitted files.

---

1. [NEEDS CLARIFICATION] Which ZIP code formats must be accepted?
   Options: A) 5-digit US ZIP only; B) 5-digit and ZIP+4; C) Any postal code-like input.

2. [NEEDS CLARIFICATION] What facility details must appear in each result?
   Options: A) Name and distance only; B) Name, address, distance; C) Name, address, distance, accepted materials; D) Name, address, distance, contact/link.

3. [NEEDS CLARIFICATION] What should break ties when facilities have the same distance?
   Options: A) Alphabetical by facility name; B) Most recently verified first; C) Stable directory order.

4. [NEEDS CLARIFICATION] What source validates ZIP codes and provides ZIP center coordinates?
   Options: A) Internal ZIP reference dataset; B) External geocoding service; C) Facility directory includes ZIP centroids.

5. [NEEDS CLARIFICATION] How current must facility active/verified status be for search eligibility?
   Options: A) Real-time/current directory state; B) Last successful daily sync; C) Last successful weekly sync.