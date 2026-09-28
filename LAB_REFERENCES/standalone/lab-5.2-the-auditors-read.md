# The Auditor's Read

## Objectives

In this lab, you will read an evidence packet the way an auditor would, judge each section, and say what is missing from the weak ones.

Knowing what auditors expect is tested by whether you can spot its absence, not by whether you can recite the list. In this lab a colleague has drafted PolicyPal's evidence packet for Q3 2026, the quarter you have run it since Lab 1.1, and you read it the way internal audit will before it goes to them. It looks competent, and most of it is right, but two sections are there in name only: the human checking gives numbers with no judgement of the reviewers, and the quality scores do not say what they were marked against. You judge each section, then say what is missing from the two weak ones and why an auditor would care.

By the end of this lab you will be able to review an AI evidence packet against what an auditor actually needs: check a packet section by section against the question each section must answer, tell a section present in substance from one present in name only, and say what is missing from a section that gives numbers without the judgement or the standard behind them.

## Background (Why This Matters)

```text
Draft packet, section by section
       │
       ▼
Judge against the auditor's question for that section
       │
       ▼
Present in substance / in name only / missing
       │
       ▼
For each weak section: what's missing, and why it matters
```

The best way to learn what a good packet needs is to spot what a bad one is missing. Noticing what is absent is much harder than noticing what is there. The question an auditor asks is not "is this neat?" It is "is there enough here to believe the company really watched over its AI?" A section can look fine because it has a heading and an entry, and still fail to prove what it is for.

**Words you will see in this lab**
- **Auditor:** a person whose job is to check that a company really did what it says it did.
- **Finding:** a problem that an auditor writes down. A good finding says what is wrong, why it matters, and what would fix it.
- **Quality standard:** the rulebook that a quality score was marked against. A score means nothing without it.

## Procedure

1. **Read the packet the way an auditor will.** Today is Friday 2026-10-02. Internal audit will want PolicyPal's packet for Q3 (2026-07-01 to 2026-09-30) next, the quarter you have run it since Lab 1.1. A colleague, P. Haddad, has drafted it for you. Before it goes to the auditors, read it the way they will: as someone who does not trust it yet.

    #### AI Evidence Packet: PolicyPal, 2026-Q3

    | Field | Value |
    |---|---|
    | Workflow | PolicyPal (HR policy assistant, Microsoft Copilot) |
    | Packet coverage period | 2026-Q3 (2026-07-01 to 2026-09-30) |
    | Prepared by | P. Haddad, for PolicyPal's Business AI Owner |
    | Date assembled | 2026-10-02 |

    Known gaps: none identified.

    For each of the six sections you see next, judge it against the auditor's question for it, choosing one:

    - Present in substance: it really answers the auditor's question for Q3.
    - Present in name only: it has an entry, but an auditor could not use it to answer the question.
    - Missing: it is not there at all.

0. **Section 1 of 6: Business purpose statement.** The auditor's question: what is this tool for?

    | Item | Source file | Date | Coverage period | Retention location |
    |---|---|---|---|---|
    | PolicyPal business purpose statement | business-purpose.md | 2026-03-02, last reviewed 2026-06-05 | Ongoing | GRC evidence library / PolicyPal / 2026 |

    ***Section 1.***

    - Present in substance
    - Present in name only
    - Missing

    <details><summary>Hint: where to look</summary>

    Read the Item and Coverage period columns. Does the row say what PolicyPal is for, and does it apply to the whole of Q3?

    </details>

    <details><summary>Show the answer</summary>

    `Present in substance`. It says what PolicyPal is for and who uses it, and it applies all through Q3.

    </details>

0. **Section 2 of 6: System instructions and baseline business rules.** The auditor's question: what was it told to do?

    | Item | Source file | Date | Coverage period | Retention location |
    |---|---|---|---|---|
    | System instructions v2 and business rules | system-instructions-v2.md | 2026-03-02 | 2026-07-01 to 2026-07-12 | GRC evidence library / PolicyPal / 2026 |
    | System instructions v3 and business rules | system-instructions-v3.md | 2026-07-13 | 2026-07-13 onward | GRC evidence library / PolicyPal / 2026 |

    ***Section 2.***

    - Present in substance
    - Present in name only
    - Missing

    <details><summary>Hint: where to look</summary>

    Q3 runs from 2026-07-01 to 2026-09-30. Read the Coverage period of each row. Between them, do the rows cover every day of Q3?

    </details>

    <details><summary>Show the answer</summary>

    `Present in substance`. v2 covers 2026-07-01 to 2026-07-12 and v3 covers 2026-07-13 onward, so between them the rules for every day of Q3 are there.

    </details>

0. **Section 3 of 6: Sampled review records and quality scores.** The auditor's question: did you check its quality, and when?

    | Item | Source file | Date | Coverage period | Retention location |
    |---|---|---|---|---|
    | Monthly re-tests, 20 marked answers each. Business Quality Score: July 88, August 81, September 83 | q3-retests.csv (60 marked answers) | 2026-09-18 | 2026-Q3 | Copilot audit log |

    ***Section 3.***

    - Present in substance
    - Present in name only
    - Missing

    <details><summary>Hint: where to look</summary>

    Read the Item column and ask yourself: could you tell from this row alone whether 83 is a good score or a bad one? What would you need to know about how the answers were marked?

    </details>

    <details><summary>Show the answer</summary>

    `Present in name only`. It gives three scores, but nothing says which quality standard, or which version of it, the answers were marked against. Without that nobody can tell what 88, 81 or 83 means.

    </details>

0. **Section 4 of 6: HITL override summary and reviewer quality audit.** The auditor's question: was the human checking real? (HITL means "human in the loop": a person checking the AI.)

    | Item | Source file | Date | Coverage period | Retention location |
    |---|---|---|---|---|
    | Override rates by reviewer (R-A to R-E), team 17% | q3-override-rates.csv | 2026-09-30 | 2026-Q3 | Purview audit |

    ***Section 4.***

    - Present in substance
    - Present in name only
    - Missing

    <details><summary>Hint: where to look</summary>

    The auditor's question is whether the human checking was real. Does a list of override rates answer that on its own? Think back to Lab 3.1: R-A's 2% looked fine until you worked out what it meant.

    </details>

    <details><summary>Show the answer</summary>

    `Present in name only`. It gives each reviewer's override rate, but nothing says whether the reviewers were really checking. Lab 3.1 showed that a normal-looking number can hide a reviewer who approves everything.

    </details>

0. **Section 5 of 6: Incident and escalation history.** The auditor's question: what went wrong, and what did you do about it?

    What happened in Q3, from your earlier labs:

    - 2026-07-06: you took over PolicyPal and gave the eight open issues owners (Lab 1.1).
    - 2026-07-13: v3 of PolicyPal's rules took effect, replacing v2.
    - 2026-08-11: the AI model version changed and the score fell from 88 to 81 (Lab 2.1). The platform team moved it back on 2026-08-25.
    - 2026-09-01: PTO Policy 2026 took effect, and the Quality Standard's PTO figures went out of date (Lab 2.2).
    - September: PolicyPal was still citing PTO Policy 2023 for carryover questions (Lab 4.1).

    | Item | Source file | Date | Coverage period | Retention location |
    |---|---|---|---|---|
    | Eight open issues from the handover given owners (old PTO policy cited, no human-referral trigger, and six more) | handover-issue-routing.md | 2026-07-06 | 2026-Q3 | GRC evidence library / PolicyPal / 2026 |
    | Answers vaguer after the model version changed on 2026-08-11 (score 88 to 81). Routed to the platform team; model moved back 2026-08-25 | ticket-model-change.md | 2026-08-17 | 2026-Q3 | Purview audit |
    | PTO answers marked down after PTO Policy 2026 took effect on 2026-09-01. Routed to the HR policy library team; the Quality Standard's PTO figures to be updated | ticket-pto-policy-2026.md | 2026-09-21 | 2026-Q3 | GRC evidence library / PolicyPal / 2026 |
    | PTO Policy 2023 still cited for carryover (cap given as 10 days, current cap 3). Routed to the HR policy library team | ticket-pto-2023.md | 2026-09-22 | 2026-Q3 | GRC evidence library / PolicyPal / 2026 |

    ***Section 5.***

    - Present in substance
    - Present in name only
    - Missing

    <details><summary>Hint: where to look</summary>

    Go down the list of what happened in Q3, above, and look for each event in the Item column of the packet's rows.

    </details>

    <details><summary>Show the answer</summary>

    `Present in substance`. The handover routing, the model change, the PTO policy change and the old PTO document are all there, each with who it went to.

    </details>

0. **Section 6 of 6: Change-control and approval log.** The auditor's question: what changed, and who approved it?

    What happened in Q3, from your earlier labs:

    - 2026-07-06: you took over PolicyPal and gave the eight open issues owners (Lab 1.1).
    - 2026-07-13: v3 of PolicyPal's rules took effect, replacing v2.
    - 2026-08-11: the AI model version changed and the score fell from 88 to 81 (Lab 2.1). The platform team moved it back on 2026-08-25.
    - 2026-09-01: PTO Policy 2026 took effect, and the Quality Standard's PTO figures went out of date (Lab 2.2).
    - September: PolicyPal was still citing PTO Policy 2023 for carryover questions (Lab 4.1).

    | Item | Source file | Date | Coverage period | Retention location |
    |---|---|---|---|---|
    | System instructions v2 to v3: approved and published | instructions-change-approval.md | 2026-07-13 | 2026-Q3 | GRC evidence library / PolicyPal / 2026 |
    | Platform change record: model version changed 2026-08-11 and moved back 2026-08-25 | platform-change-record.csv | 2026-08-25 | 2026-Q3 | Copilot audit log |

    ***Section 6.***

    - Present in substance
    - Present in name only
    - Missing

    <details><summary>Hint: where to look</summary>

    Go down the list of what happened in Q3, above, and pick out the changes made to PolicyPal itself. Look for each one in the Item column of the packet's rows.

    </details>

    <details><summary>Show the answer</summary>

    `Present in substance`. The two changes to PolicyPal itself are there: the move to v3 of the rules, and the model version change and move back. The PTO policy change and the old PTO document are changes to the policy library, not to PolicyPal, so they belong in section 5.

    </details>

0. **Finding 1: the human checking.** A finding is a problem an auditor writes down: what is wrong, why it matters, and what would fix it. You judged two sections present in name only. Start with section 4 (above). What is missing from it?

    ***What is missing from section 4?***

    - Any judgement of the reviewers: whether each one really checked, and the result of R-A's July re-check
    - How many decisions each reviewer made in Q3, so the auditor can see how busy the review team was
    - Q2's override rates next to Q3's, so the auditor can see whether the team's 17% is going up or down
    - The names of the five reviewers, so the auditor can interview each one about how they do their reviews

    <details><summary>Hint: where to look</summary>

    Section 4's question is "was the human checking real?" An override rate is only a number. Think back to Lab 3.1: what did you have to work out about R-A and R-B before the numbers meant anything? Then think of Lab 3.2's plan for R-A: its re-check was due on 2026-07-18, inside Q3. Is its result anywhere in this packet?

    </details>

    <details><summary>Show the answer</summary>

    `Any judgement of the reviewers`. Section 4 gives each reviewer's override rate, but nothing says whether they were really checking. Lab 3.1 showed that a 2% rate can mean a reviewer approves everything, and the result of R-A's re-check on 2026-07-18 is not in the packet at all.

    - Why the auditor cares: without it, the auditor cannot tell whether the human checking was real, which is the whole question of section 4.
    - The fix: add the reviewer quality audit for Q3, with the result of R-A's re-check.
    - Decision counts, Q2's rates and names are all extra numbers or people. None of them says whether anyone checked properly.

    </details>

0. **Finding 2: the quality scores.** Now section 3 (above). What is missing from it?

    ***What is missing from section 3?***

    - Which quality standard, and which version of it, the three monthly scores were marked against
    - The marked answers themselves, so the auditor can re-mark a few and check the scores are right
    - A score for each of the four rules, so the auditor can see which rule caused August's drop
    - The name of the person who marked each re-test, so the auditor can check they were trained

    <details><summary>Hint: where to look</summary>

    Read the Item and Source file columns of section 3: what is already there? Then think back to Lab 2.2. What did you find out about the Quality Standard in September, and what would that do to a September score?

    </details>

    <details><summary>Show the answer</summary>

    `Which quality standard, and which version of it`. A score only means something against the rulebook it was marked with. In Q3 that rulebook went out of date: PTO Policy 2026 took effect on 2026-09-01, and the Quality Standard still listed the 2025 PTO figures (Lab 2.2). So September's 83 means something different depending on which version was used.

    - Why the auditor cares: without the standard, nobody can tell what 88, 81 or 83 means, or compare them.
    - The fix: attach the Quality Standard, with the version and date each re-test used.
    - The marked answers are already there: `q3-retests.csv` holds all 60. Scores for each rule and the markers' names are useful, but without the standard they still cannot be read.

    </details>

## Conclusion

In this lab you read PolicyPal's Q3 evidence packet the way an auditor would. You judged each section against the question it has to answer, and found two that are there in name only: override rates with no judgement of the reviewers, and quality scores that cannot be read without the standard they were marked against. Spotting what is absent is the real test of knowing what auditors expect.
