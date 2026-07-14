I’ll use the `speckit-clarify` skill and limit the inputs to the three files you named.

---

The skill’s normal workflow writes accepted answers back into the spec, but your experimental instructions override that: I’m only reading the allowed inputs and returning unresolved clarification questions.

---

1. [NEEDS CLARIFICATION] What defines “sufficient profile and interaction history” for personalized recommendations? Answer in <=5 words.

2. [NEEDS CLARIFICATION] When a user disables interaction-history use, may recommendations still use their declared interests?
   | Option | Description |
   |--------|-------------|
   | A | Yes, use declared interests only |
   | B | No, use only non-personalized popular content |

3. [NEEDS CLARIFICATION] How should non-personalized popular fallback content be ranked?
   | Option | Description |
   |--------|-------------|
   | A | Most viewed eligible content |
   | B | Most saved eligible content |
   | C | Most positively rated eligible content |
   | D | Composite popularity score |

4. [NEEDS CLARIFICATION] What makes content “eligible” for recommendation beyond not being dismissed? Answer in <=5 words.

5. [NEEDS CLARIFICATION] What should be communicated when no eligible recommendations are available? Answer in <=5 words.