# Set the Business Quality Standard for a Deployed AI Workflow

## Objectives

In this lab, you will take operational ownership of a deployed AI workflow and write the business quality standard that every later review will measure against.

An AI workflow called PolicyPal is already running in production, answering employee HR policy questions, and today it becomes yours. Before you can tell whether it is doing a good job, you need three things: an understanding of what you have been handed, a clear split between the problems you own and the problems the platform team owns, and a written standard for what a good answer looks like. This lab walks through all three in the order you would actually do them on the day a workflow transfers to you. The standard you produce here is the yardstick for every measurement in the rest of the course.

By the end of this lab you will be able to read a workflow intake record and identify its risk tier, review cadence, and baseline sample size; sort a list of open issues into the ones you own and the ones the platform team owns; justify the ownership of two borderline issues; and write a five-part business quality standard precise enough for a colleague to apply.

## Background (Why This Matters)

```text
Deployed AI workflow (PolicyPal)
       │
       ▼
Read what you inherited (the intake record)
       │
       ▼
Split the open issues: yours vs. the platform team's
       │
       ▼
Business Quality Standard
(what "good" means, written down)
```

A company has just handed you an AI assistant called PolicyPal and said "this is yours now." You cannot check whether something is doing a good job until you have written down what "a good job" means. The rulebook you write in this lab, the Business Quality Standard, is what every later check in the course is measured against.

**Words you will see in this lab**
- **Business AI Owner:** that is you. The person on the business side who is responsible for whether the AI's answers are good enough.
- **Risk tier:** a rating (Low, Medium or High) of how much could go wrong with an AI tool. Someone else decides it. You only read it.
- **Review cadence:** how often the AI must be checked. Riskier tools are checked more often.
- **Baseline sample size:** how many of the AI's answers you must check each time.
- **Business Quality Standard:** the rulebook you will write. It says what a good answer looks like and what must never happen.
- **Platform team:** the technical people who run the computers and software behind the AI.

## Required Reading

Read this before you start the procedure. Every lab in this course uses PolicyPal as its example, so what you read here applies all day.

**What PolicyPal is.** PolicyPal is a chat assistant that employees use to ask questions about HR policy. An employee types a question, such as "How many PTO days do I accrue in my second year?" or "What is the mileage reimbursement rate?", and PolicyPal replies with an answer and names the policy document it came from. It runs inside Microsoft Copilot, and about 1,900 employees use it each month.

**What it is for.** PolicyPal gives employees a fast, consistent answer to one question: "What does our policy say?" It covers five topics: paid time off (PTO), benefits, expenses, travel, and conduct. Employees get an answer in seconds instead of searching through policy documents or waiting on someone in HR.

**Where its answers come from.** PolicyPal reads only the HR Policy Library, the company's collection of official HR policy documents. It has no rules of its own. It repeats what those documents say, so if the library still holds an out-of-date document, PolicyPal can repeat the out-of-date rule.

**Who is involved.**
- **You** are the Business AI Owner. As of today, you are responsible for whether PolicyPal's answers are good enough for the business: correct, current, and appropriately cautious.
- **The platform team** runs the technology behind it, such as the AI model, sign-in, and system speed.
- **Five HR operations reviewers** spot-check answers that have been flagged.

**Why it needs an owner.** PolicyPal is not broken on the day it launches. Problems show up later: an old policy stays in the library and keeps getting quoted, a vendor changes the AI model and the answers get vaguer, or a sensitive question gets answered when it should have gone to a person. Nothing raises an alarm when this happens, so someone has to be checking. That is the job you are taking over today.

## Procedure

1. **Get to know PolicyPal.** Below is PolicyPal's intake record, a fact sheet filled in by the person who looked after PolicyPal before you.

    | Field | Value |
    |---|---|
    | Workflow name | PolicyPal |
    | Platform | Microsoft Copilot (declarative agent) |
    | Business purpose | Answers employee questions about company HR policy (PTO, benefits, expense, travel, conduct) |
    | Grounding source | HR Policy Library, SharePoint site `HR-Policy` |
    | Deployed | 2026-03-02 |
    | Approval tier at deployment | Type 2 (reviewed before production) - context only |
    | Assigned risk tier | Medium (assigned by Risk & InfoSec with HR, 2026-02-18) |
    | Current owner | Transferring to you, effective today |
    | Monthly active users | ~1,900 |
    | Reviewer pool | 5 HR operations reviewers spot-check flagged answers |

    Read it from top to bottom, then answer:

    ***One sentence: what this workflow does and for whom.***

    <details><summary>Hint: where to look</summary>

    Look at the rows called Business purpose and Grounding source. Grounding source means where PolicyPal gets its answers from.

    </details>

    <details><summary>Hint: an example answer</summary>

    `PolicyPal answers employee questions about company HR policy (PTO, benefits, expense, travel, conduct), grounded on the HR Policy Library.`

    </details>

0. **Find PolicyPal's risk tier and review requirements.** Every AI tool gets a risk tier: Low, Medium, or High. It says how much could go wrong. You do not decide it. Another team (Risk & InfoSec) decided it with HR before PolicyPal went live. You only read it.

    The risk tier determines the review cadence (how often PolicyPal must be checked) and the baseline sample size (how many of PolicyPal's answers must be checked each time).

    | Field | Value |
    |---|---|
    | Assigned risk tier | Medium (assigned by Risk & InfoSec with HR, 2026-02-18) |

    | Risk tier | Review cadence | Baseline sample size |
    |---|---|---|
    | Low | Quarterly | 10 responses |
    | Medium | Monthly | 20 responses |
    | High | Weekly (plus an event-driven review on any model or policy change) | 30 responses |

    Find PolicyPal's risk tier above, find that risk tier in the chart, and answer:

    ***Risk tier, review cadence, and baseline sample size.***

    <details><summary>Show the answer</summary>

    - Risk tier: `Medium`
    - Review cadence: `Monthly`
    - Baseline sample size: `20 responses`

    </details>

0. **Decide who owns each of PolicyPal's open issues.** The person who looked after PolicyPal before you left a list of eight problems, below. Some problems are yours to fix. Others belong to the technical team. If a problem goes to the wrong person, nobody fixes it.

    | Issue | Raised | Problem | Owner |
    |---|---|---|---|
    | 1 | 2026-06-14 | The assistant sometimes cites "PTO Policy 2023" instead of the current 2025 version. The 2023 document is still present in the SharePoint source. | |
    | 2 | 2026-06-19 | There is no defined trigger for handing accommodation or protected-leave questions to a human. The assistant answers them directly. | |
    | 3 | 2026-06-21 | Two employees asked the same expense question and were given different per-diem figures. | |
    | 4 | 2026-06-25 | Response latency spikes to 8–10 seconds around 9:00 each morning. | |
    | 5 | 2026-06-27 | IT changed the underlying model version last Tuesday. No notice was given to the workflow owner. | |
    | 6 | 2026-06-28 | Some users in one region intermittently get an "authentication failed" error when opening the assistant. | |
    | 7 | 2026-07-01 | The assistant answered a question about statutory maternity leave with specific legal detail about entitlements and notice periods. | |
    | 8 | 2026-07-02 | Users have asked that the assistant also draft the leave-request email for them, not just answer the policy question. | |

    Read all eight problems, then decide an owner for each:

    - **Business AI Owner** (you): fixing it means changing a business rule, the content PolicyPal reads, or something people do.
    - **Platform / technical owner**: fixing it means changing the computer systems, the AI model, or code.

    ***For each issue, choose the owner: Business AI Owner or Platform / technical owner.***

    <details><summary>Show the answer</summary>

    - **Business AI Owner:** 1, 2, 3, 7
    - **Platform / technical owner:** 4, 5, 6, 8

    Issues 1 and 8 are the hardest to place. You will explain them in the next step.

    </details>

0. **Explain the two hardest ownership choices.** Some problems could belong to either side. Pick the two problems where you found it hardest to decide, using the owners you chose above.

    ***Borderline issue 1 (number and justification).***

    ***Borderline issue 2 (number and justification).***

    <details><summary>Hint: example answers</summary>

    - Issue 1 (the assistant cites an old policy version) is arguable: the old document sitting in the source is a content problem, but deciding the rule about what the assistant may cite is yours.
    - Issue 8 (users want a new drafting feature) is a build request for whoever owns the agent configuration, not a quality problem.

    </details>

0. **Say what a correct answer looks like.** Now you write the rulebook for PolicyPal: the Business Quality Standard. Start with what a correct answer looks like. The two problems below show answers that were not correct. For each one, write one check that would have caught it. Each check must be something a reviewer can mark yes or no, not a feeling.

    | Issue | Problem |
    |---|---|
    | 1 | The assistant sometimes cites "PTO Policy 2023" instead of the current 2025 version. The 2023 document is still present in the SharePoint source. |
    | 3 | Two employees asked the same expense question and were given different per-diem figures. |

    ***A criterion that would have caught Issue 1 (an old policy version cited).***

    ***A criterion that would have caught Issue 3 (two employees given different figures).***

    <details><summary>Hint: example answers</summary>

    - "Cites a named, current policy document."
    - "Every claim in the answer matches the entitlement or figure exactly as written in policy."

    </details>

0. **Write the rules that must always hold.** A business rule is an absolute: something PolicyPal must never do, or must always do. The two problems below happened because a rule was missing. For each one, write one rule that would have stopped it.

    | Issue | Problem |
    |---|---|
    | 3 | Two employees asked the same expense question and were given different per-diem figures. |
    | 7 | The assistant answered a question about statutory maternity leave with specific legal detail about entitlements and notice periods. |

    ***A rule that would have prevented Issue 3 (different per-diem figures).***

    ***A rule that would have prevented Issue 7 (legal detail about maternity leave).***

    <details><summary>Hint: example answers</summary>

    - "Never state a dollar figure or day count that is not written in current policy."
    - "Never give legal or interpretation advice; send those questions to HR."

    </details>

0. **Name the errors that are never acceptable.** An unacceptable error is a mistake that is never OK, no matter how rarely it happens. Each problem below shows one. Write the error each problem shows.

    | Issue | Problem |
    |---|---|
    | 1 | The assistant sometimes cites "PTO Policy 2023" instead of the current 2025 version. The 2023 document is still present in the SharePoint source. |
    | 7 | The assistant answered a question about statutory maternity leave with specific legal detail about entitlements and notice periods. |

    ***An unacceptable error shown by Issue 1 (an old policy version cited).***

    ***An unacceptable error shown by Issue 7 (legal detail about maternity leave).***

    <details><summary>Hint: example answers</summary>

    - "Citing an obsolete policy as if it were current."
    - "Answering a protected or statutory leave question with detail instead of referring it to HR."

    </details>

0. **Say when a person must take over.** A trigger is a situation where PolicyPal should stop and send the employee to a real person. Each problem below points to one. Write one trigger for each.

    | Issue | Problem |
    |---|---|
    | 2 | There is no defined trigger for handing accommodation or protected-leave questions to a human. The assistant answers them directly. |
    | 1 | The assistant sometimes cites "PTO Policy 2023" instead of the current 2025 version. The 2023 document is still present in the SharePoint source. |

    ***A trigger that would have caught Issue 2 (accommodation or protected-leave questions).***

    ***A trigger for the situation behind Issue 1 (two versions of one policy in the library).***

    <details><summary>Hint: example answers</summary>

    - "Any question about an accommodation or leave."
    - "Any question where two versions of a policy conflict, so it is unclear which one is current."

    </details>

0. **Say how much difference is acceptable.** In the problem below, two employees asked the same question and got different figures. Some difference in wording between two answers is normal. A difference in the figure is not.

    | Issue | Problem |
    |---|---|
    | 3 | Two employees asked the same expense question and were given different per-diem figures. |

    Write one limit: how much difference is acceptable between two answers to the same question? Say it in plain words or as a percentage.

    ***How much difference is acceptable between two answers to the same question? (Issue 3)***

    <details><summary>Hint: an example answer</summary>

    "Two employees who ask the same question must get the same entitlement figure, every time."

    </details>

## Conclusion

In this lab you took operational ownership of a deployed AI workflow, separated the problems you govern from the ones the platform team governs, and wrote a business quality standard precise enough for someone else to apply without asking you a question. That standard is the reference point for every quality audit, reviewer check, and evidence packet in the rest of this course, and it is the first thing to write or locate when any AI workflow becomes your responsibility.
