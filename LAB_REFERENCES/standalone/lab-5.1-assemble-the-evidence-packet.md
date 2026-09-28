# Assemble the AI Evidence Packet

## Objectives

In this lab, you will build a six-section evidence packet for one quarter from a folder of candidate papers, list its gaps and who will fill them, and choose where the copies are kept.

This is the capstone. When an auditor asks you to show that oversight of an AI workflow actually happened, the answer is a packet: business purpose, system instructions and rules, sampled review records and scores, the override summary and reviewer audit, incident history, and the change-control log. Internal audit has asked for PolicyPal's packet for Q2 2026, the quarter before you took it over. You get a folder with more papers than the packet needs, including a newer version of the rules and another tool's quality record. You decide what belongs, find what is missing, say who will supply it, and keep the copies somewhere they will last.

By the end of this lab you will be able to assemble an audit-ready evidence packet for any AI workflow: sort candidate papers into the six packet sections, keeping only papers about this workflow and this quarter; choose the version of a document that was in force during the period, even when a newer one exists; check whether each section's evidence covers the whole period; name who can supply each missing piece of evidence; and choose a place to keep the copies that outlasts the AI platform's own records.

## Background (Why This Matters)

```text
Folder of eight candidate papers
       │
       ▼
Sort into six packet sections (or leave out)
       │
       ▼
List the gaps, and who can supply each
       │
       ▼
Choose where the copies are kept
```

"We looked after it" is not proof. Papers are. A packet with the right papers in the right places is what lets a company pass an audit. A paper goes in the packet only if both are true: it is about the workflow being audited, and it is evidence for the period being audited (made during the period, or in force during it).

**Words you will see in this lab**
- **Auditor:** a person whose job is to check that a company really did what it says it did.
- **Evidence packet:** a set of papers, organised into sections, that proves the company kept watch over its AI.
- **Coverage period:** the stretch of time a packet or paper proves something about. For example, "2026-Q2" means 2026-04-01 to 2026-06-30.
- **Retention:** where the company keeps its records, and for how long. A record kept only on the AI platform can be deleted by the platform after about 180 days, so it must also be kept somewhere else.
- **Gap:** something that should be in the packet but is missing.
- **Superseded:** replaced by a newer version. A superseded paper can still be the right one for a packet about the time before it was replaced.
- **In force:** the version of a rule or document that applied at the time.

## Procedure

1. **See what the auditor has asked for.** Today is Monday 2026-09-28. The company's internal audit team is checking how its AI tools are looked after, and has asked for PolicyPal's evidence packet for Q2 2026 (2026-04-01 to 2026-06-30).

    You took over PolicyPal in July (Lab 1.1), so Q2 was before your time. The previous owner's papers have been exported from their shared drive into one folder of eight papers. The packet has six sections, and each answers one question an auditor asks.

    #### The six sections of the packet

    | Section | The auditor's question |
    |---|---|
    | 1. Business purpose statement | What is this tool for? |
    | 2. System instructions and baseline business rules | What was it told to do? |
    | 3. Sampled review records and quality scores | Did you check its quality, and when? |
    | 4. HITL override summary and reviewer quality audit | Was the human checking real? (HITL means "human in the loop": a person checking the AI.) |
    | 5. Incident and escalation history | What went wrong, and what did you do about it? |
    | 6. Change-control and approval log | What changed, and who approved it? |

    A paper goes in the packet only if both of these are true: it is about PolicyPal, and it is evidence for Q2 (it was made during Q2, or it was in force during Q2). In the next eight steps you see one paper at a time and choose its section.

    <details><summary>Hint: where to look, for every paper below</summary>

    The top of each paper gives its workflow and its dates: look for Workflow, and for Effective, Period or Plan date. The two tables give theirs in the Workflow, Quarter and Re-test date columns. For every paper, check whose it is, and whether its dates fall in 2026-04-01 to 2026-06-30. A paper that took effect after that did not govern PolicyPal in Q2, however new it is. One section takes two papers.

    </details>

0. **Paper 1 of 8: a1-business-purpose.**

    #### Business purpose statement

    Workflow: PolicyPal. Effective: 2026-03-02. Last reviewed: 2026-06-05.

    PolicyPal is an internal HR policy assistant, deployed on Microsoft Copilot, that answers employee questions about company HR policy (paid time off, benefits, expense, travel, and conduct). It is grounded on the HR Policy Library in SharePoint. It serves roughly 1,900 monthly active users. It is not a system of record and does not make or approve any employment decision; it retrieves and states current policy and refers employees to a human for accommodation, protected-leave, and disputed-decision questions.

    Assigned risk tier: Medium (Risk & InfoSec with HR, 2026-02-18). Review cadence: monthly.

    ***Where does a1-business-purpose go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `1. Business purpose statement`. It says what PolicyPal is for and who uses it, and it was in force all through Q2 (effective 2026-03-02, last reviewed 2026-06-05).

    </details>

0. **Paper 2 of 8: a2-system-instructions-v3.**

    #### System instructions and baseline business rules

    Workflow: PolicyPal. Version: v3. Effective: 2026-07-13. Supersedes: v2 (effective 2026-03-02).

    System instructions (summary): PolicyPal answers employee questions about company HR policy using only the current documents in the HR Policy Library. It names the policy document and its effective date in every substantive answer. It does not speculate where policy is silent.

    Baseline business rules:
    1. Never state a figure, day count, or entitlement that is not written in current policy.
    2. Always name the source policy document and its effective date.
    3. Never cite a superseded version of a policy.
    4. Refer the employee to their HR business partner for any question about an accommodation, a protected or statutory leave, or a decision the employee is disputing.
    5. Do not give legal or tax advice; refer statutory questions to HR.

    Change from v2: rules 3, 4 and 5 were added in v3 after the new Business AI Owner reviewed the open issues at handover in July 2026: an old PTO policy still being cited, no trigger for handing accommodation and protected-leave questions to a person, and legal detail given about statutory leave. v2 had a single general "escalate sensitive questions" instruction with no list.

    ***Where does a2-system-instructions-v3 go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `Leave it out`. v3 took effect on 2026-07-13, after Q2 ended, so it is not what PolicyPal was told to do in Q2, even though it is the newest version. It will belong in the Q3 packet.

    </details>

0. **Paper 3 of 8: a3-system-instructions-v2.**

    #### System instructions and baseline business rules

    Workflow: PolicyPal. Version: v2. Effective: 2026-03-02. Status: superseded by v3 on 2026-07-13.

    System instructions (summary): PolicyPal answers employee questions about company HR policy using the documents in the HR Policy Library. It names the policy document in substantive answers.

    Baseline business rules:
    1. Never state a figure, day count, or entitlement that is not written in policy.
    2. Name the source policy document.
    3. Escalate sensitive questions to HR.

    ***Where does a3-system-instructions-v2 go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `2. System instructions and baseline business rules`. v2 was in force from 2026-03-02 to 2026-07-12, the whole of Q2. It is superseded now, but the auditor asks what PolicyPal was told to do during Q2, not today.

    </details>

0. **Paper 4 of 8: a4-review-sample-q2.**

    #### a4-review-sample-q2

    | Workflow | Quarter | Scored against | Re-test date | Answers scored | c1 met | c2 met | c3 met | c4 met | Criteria met | Score |
    |---|---|---|---|---|---|---|---|---|---|---|
    | PolicyPal | 2026-Q2 | PolicyPal Quality Checklist v1 (previous owner, 2026-03-02) | 2026-04-28 | 20 | 19 | 19 | 19 | 18 | 75 of 80 | 94 |
    | PolicyPal | 2026-Q2 | PolicyPal Quality Checklist v1 (previous owner, 2026-03-02) | 2026-05-27 | 20 | 18 | 18 | 19 | 18 | 73 of 80 | 91 |
    | PolicyPal | 2026-Q2 | PolicyPal Quality Checklist v1 (previous owner, 2026-03-02) | 2026-06-24 | 20 | 19 | 18 | 18 | 18 | 73 of 80 | 91 |
    | PolicyPal | 2026-Q2 | PolicyPal Quality Checklist v1 (previous owner, 2026-03-02) | Quarter | 60 | 56 | 55 | 56 | 54 | 221 of 240 | 92 |

    ***Where does a4-review-sample-q2 go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `3. Sampled review records and quality scores`. It is PolicyPal's (see the Workflow column), and it holds the three monthly re-tests from April, May and June.

    </details>

0. **Paper 5 of 8: a5-hitl-override-summary-q2.**

    #### HITL override summary and reviewer quality audit

    Workflow: PolicyPal. Period: 2026-Q2 (reviewer log, 30 days, 2026-05-19 to 2026-06-17). Reviewer pool: 5 HR operations reviewers (R-A to R-E).

    Override summary:

    | Reviewer | Decisions reviewed | Override rate |
    |---|---|---|
    | R-A | 42 | 2% |
    | R-B | 42 | 43% |
    | R-C | 42 | 17% |
    | R-D | 44 | 16% |
    | R-E | 42 | 14% |
    | Team | 212 | 18% |

    Overall human agreement rate: 82%. Override rate trend across the period: rising, from roughly 11% in the first week to roughly 26% in the last.

    Reviewer quality audit: two reviewers fall outside the normal range. R-A overrides 2% of AI decisions against a team average of 18%, with a near-zero rate in every week and every case type; the pattern is consistent with rubber-stamping and is the subject of a separate remediation plan. R-B overrides 43% of decisions on the same case mix the other reviewers handle, which points to the reviewer rather than the AI. R-D decided a seeded duplicate case inconsistently. The rising override trend was cross-checked against the Q2 quality audit; output quality was stable over the period, so the trend reflects reviewer behavior, not AI degradation, and warrants monitoring.

    ***Where does a5-hitl-override-summary-q2 go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `4. HITL override summary and reviewer quality audit`. It is PolicyPal's summary of how often the human reviewers disagreed with the AI, with a judgement of the reviewers, from inside Q2.

    </details>

0. **Paper 6 of 8: a6-remediation-plan-RA.**

    #### Remediation plan: reviewer R-A

    Workflow: PolicyPal. Plan date: 2026-06-18. Owner: the function that runs the human review process for PolicyPal.

    Finding: approvals from reviewer R-A are not getting an independent check: R-A's override rate is 2% against a team average of 18%, near zero in every week and case type.

    First step: a second reviewer re-marks a sample of R-A's recent approvals to confirm the pattern.

    Action: ongoing second-review sampling: each month, a second reviewer re-checks a sample of every reviewer's decisions.

    Interim safeguard: a second reviewer checks every one of R-A's approvals until the new sampling is running.

    Verification: re-check date 2026-07-18, one month after the plan starts (Medium-tier cadence). Measurable target: R-A's override rate within 5 points of the team average, over a two-week sample. Evidence: a fresh export of the reviewer log, covering the two weeks before the re-check date.

    Distribution: R-A's manager; the workflow record.

    ***Where does a6-remediation-plan-RA go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `4. HITL override summary and reviewer quality audit`. It is the plan to fix the reviewer problem that a5 found, dated 2026-06-18, inside Q2. Section 4 holds both papers.

    </details>

0. **Paper 7 of 8: a7-incident-history.**

    #### Incident and escalation history

    Workflow: PolicyPal. Period covered: 2026-Q2 (2026-04-01 to 2026-06-30).

    Ticket 1: Benefits Guide missing from the library. Raised 2026-04-14. Category: Business content. Routed to: the team that owns the HR Policy Library. Observed: after a SharePoint clean-up, "Benefits Guide 2025" was no longer in the HR Policy Library. PolicyPal told employees it could not find any benefits information. Impact: 31 benefits questions went unanswered over three days. Ask: restore the document to the library. Outcome: restored 2026-04-17. Re-tested 2026-04-21: benefits questions answered and the guide cited. Closed.

    Issues logged in June but not routed: the previous owner left PolicyPal in June. These issues were logged but not given an owner before the end of the quarter. All were open on 2026-06-30 and were handed to the new Business AI Owner in July.

    | Issue | Raised | Problem | Routed to | Status on 2026-06-30 |
    |---|---|---|---|---|
    | 1 | 2026-06-14 | The assistant sometimes cites "PTO Policy 2023" instead of the current 2025 version. The 2023 document is still present in the SharePoint source. | No one | Open |
    | 2 | 2026-06-19 | There is no defined trigger for handing accommodation or protected-leave questions to a human. The assistant answers them directly. | No one | Open |
    | 3 | 2026-06-21 | Two employees asked the same expense question and were given different per-diem figures. | No one | Open |
    | 4 | 2026-06-25 | Response latency spikes to 8-10 seconds around 9:00 each morning. | No one | Open |
    | 5 | 2026-06-27 | IT changed the underlying model version last Tuesday. No notice was given to the workflow owner. | No one | Open |
    | 6 | 2026-06-28 | Some users in one region intermittently get an "authentication failed" error when opening the assistant. | No one | Open |

    ***Where does a7-incident-history go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `5. Incident and escalation history`. It lists what went wrong in Q2 and what was done about it, including the June issues nobody picked up.

    </details>

0. **Paper 8 of 8: a8-finance-assistant-sample-q2.**

    #### a8-finance-assistant-sample-q2

    | Workflow | Quarter | Scored against | Re-test date | Answers scored | c1 met | c2 met | c3 met | c4 met | Criteria met | Score |
    |---|---|---|---|---|---|---|---|---|---|---|
    | FinanceAssistant | 2026-Q2 | Finance Assistant Answer Standard v1 (2026-02-01) | 2026-06-19 | 10 | 9 | 6 | 9 | | 24 of 30 | 80 |
    | FinanceAssistant | 2026-Q2 | Finance Assistant Answer Standard v1 (2026-02-01) | Quarter | 10 | 9 | 6 | 9 | | 24 of 30 | 80 |

    ***Where does a8-finance-assistant-sample-q2 go?***

    - 1. Business purpose statement
    - 2. System instructions and baseline business rules
    - 3. Sampled review records and quality scores
    - 4. HITL override summary and reviewer quality audit
    - 5. Incident and escalation history
    - 6. Change-control and approval log
    - Leave it out

    <details><summary>Show the answer</summary>

    `Leave it out`. Its Workflow column says `FinanceAssistant`: it is another AI tool's quality record, laid out like PolicyPal's.

    </details>

0. **Gap 1: what is missing from section 6.** No paper in the folder went in section 6, which answers "What changed in PolicyPal, and who approved it?" That is a gap. A packet lists its own gaps, so the auditor hears about them from you instead of finding them.

    The June issues (from Paper 7, above) and who is responsible for what:

    #### Who is responsible for what

    | Owner | What they are responsible for |
    |---|---|
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The function that owns the PolicyPal system instructions | Writing, approving and publishing PolicyPal's instructions (v2, v3) |
    | The team that owns the HR policy library | The HR policy documents PolicyPal reads from |
    | The function that runs the human review process for PolicyPal | The reviewers, how they review, and the reviewer log |

    Choose what the missing record should show, and who can supply it.

    ***What should section 6's missing record show?***

    - IT's change to PolicyPal's AI model version in June (issue 5), and who approved it
    - The change from v2 to v3 of PolicyPal's rules, and who approved the new rules
    - The removal of PTO Policy 2023 from the HR Policy Library, and who approved it
    - The handover of PolicyPal from the previous owner to you, and who approved it

    ***Who can supply that record?***

    - The team responsible for the platform and the vendor relationship
    - The function that owns the PolicyPal system instructions
    - The team that owns the HR policy library
    - The function that runs the human review process for PolicyPal

    <details><summary>Hint: where to look</summary>

    Section 6 is about changes made to PolicyPal itself during Q2 (2026-04-01 to 2026-06-30). Go down the Problem column above for something that was changed, and check its Raised date. Then find who is responsible for that kind of thing in the second table.

    </details>

    <details><summary>Show the answer</summary>

    - `IT's change to PolicyPal's AI model version in June (issue 5)`. It is the one change to PolicyPal in Q2, and nobody was told about it.
      - v2 to v3 happened on 2026-07-13, after Q2.
      - PTO Policy 2023 was never removed, and the library is PolicyPal's reading material, not PolicyPal itself.
      - The handover was in July.
    - `The team responsible for the platform and the vendor relationship`. They run the AI models, so they hold the record of the change and of who approved it.

    </details>

0. **Gap 2: does section 4 cover the whole quarter?** A section can have a paper and still be short, because the paper covers less time than the packet. The packet covers Q2: 2026-04-01 to 2026-06-30.

    The reviewer summary you put in section 4 (Paper 5, above) and who is responsible for what:

    | Owner | What they are responsible for |
    |---|---|
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The function that owns the PolicyPal system instructions | Writing, approving and publishing PolicyPal's instructions (v2, v3) |
    | The team that owns the HR policy library | The HR policy documents PolicyPal reads from |
    | The function that runs the human review process for PolicyPal | The reviewers, how they review, and the reviewer log |

    Decide whether it covers the whole quarter, and who can supply anything that is missing.

    ***Does a5-hitl-override-summary-q2 cover the whole of Q2?***

    - No: it covers only 2026-05-19 to 2026-06-17, so April, early May and late June are missing
    - Yes: its Period line says 2026-Q2, so it covers the quarter the auditor has asked about
    - Yes: its 212 decisions are far more than the 20 answers used in each monthly quality re-test
    - No: it leaves out reviewer R-A, whose decisions are covered by a separate remediation plan

    ***Who can supply the reviewer log for the rest of Q2?***

    - The team responsible for the platform and the vendor relationship
    - The function that owns the PolicyPal system instructions
    - The team that owns the HR policy library
    - The function that runs the human review process for PolicyPal

    <details><summary>Hint: where to look</summary>

    Read the Period line at the top of Paper 5, including the dates in brackets, and compare them with 2026-04-01 to 2026-06-30. Then check the table for who keeps the reviewer log.

    </details>

    <details><summary>Show the answer</summary>

    - `No: it covers only 2026-05-19 to 2026-06-17`. Its Period line says 2026-Q2, but the dates in brackets are 30 days of a 91-day quarter. R-A is in the table like everyone else, and the number of decisions says nothing about which dates they cover.
    - `The function that runs the human review process for PolicyPal`. They run the reviewers and keep the reviewer log.

    </details>

0. **Say where the copies are kept.** The papers only count as evidence if they still exist when someone asks for them.

    #### The company's records rule

    Evidence that an AI tool was overseen is kept for three years after the end of the period it covers.

    #### Where records can be kept

    | Place | What it is | How long it keeps records |
    |---|---|---|
    | GRC evidence library | The company's governance, risk and compliance (GRC) records system | As long as the company's rules require |
    | Copilot audit log | The record Microsoft Copilot keeps of how PolicyPal was used | About 180 days |
    | Purview audit | Microsoft's compliance tool for searching that record | About 180 days |
    | Claude workspace | The workspace of the other AI platform the company uses | About 180 days |

    Choose where the exported copies of the packet's papers should be kept.

    ***Where should the exported copies be kept?***

    - GRC evidence library: the company's own records system, kept for as long as the company's rules require
    - Copilot audit log: where PolicyPal's activity was first recorded, so the copies sit with the originals
    - Purview audit: Microsoft's compliance search for Copilot, which auditors can search by date and user
    - Claude workspace: the other AI platform the company uses, so all AI evidence is kept in one place

    <details><summary>Hint: where to look</summary>

    Read the company's records rule first: how long must this evidence be kept? Then go down the "How long it keeps records" column and cross out every place that keeps records for less than that. Today's date and the start of Q2 tell you how old the oldest Q2 records already are.

    </details>

    <details><summary>Show the answer</summary>

    `GRC evidence library`. The records rule says three years, and it is the only place that keeps records for as long as the company decides. The other three are parts of the AI platforms, which keep about 180 days. Q2 began on 2026-04-01, about 180 days ago, so the platform's records from early April are already due to be deleted.

    </details>

## Conclusion

In this lab you assembled PolicyPal's Q2 evidence packet from a folder of real and decoy papers. You kept the rules that were in force in Q2 rather than the newest ones, left out another tool's quality record, listed the two gaps with who can supply each, and chose a place to keep the copies that outlasts the platform's 180 days. That packet is what "we have oversight" looks like when an auditor asks for proof. What you carry to your own workflows is the test for each paper (this workflow, this period) and the habit of listing your own gaps.
