I’ll use the `speckit-clarify` skill for this clarification-only pass and restrict inputs to the files you named.

---

The system skill path for this run is under the experiment repo, not the default Codex skill directory. I’m reading that local instruction file now, then I’ll inspect only the allowed inputs.

---

I have the clarification workflow, but your experiment constraints override the interactive/write-back parts: I’ll only read `spec.md`, `user-story.md`, and `context.md` if present, then return unresolved questions.

---

1. [NEEDS CLARIFICATION] What exact threshold defines “sufficient history” for personalized recommendations: minimum declared interests, minimum interactions, both, or another rule?

2. [NEEDS CLARIFICATION] When fallback recommendations are used, how should “popular eligible content” be determined: recent views, saves, positive feedback, overall engagement, or another popularity metric?

3. [NEEDS CLARIFICATION] Besides dismissed content, should recommendations exclude content the user has already viewed, saved, or positively rated?

4. [NEEDS CLARIFICATION] If a user disables interaction-history use, may the system still personalize recommendations using declared interests, or must all recommendations become non-personalized?

5. [NEEDS CLARIFICATION] How should ties or ranking weights be handled across shared interests, viewed content, saved content, and positive feedback when calculating similar-profile recommendations?