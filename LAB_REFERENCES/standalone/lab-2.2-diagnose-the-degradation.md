# Diagnose the Degradation and Document the Test

## Objectives

In this lab, you will find the real cause of a drop in AI answer quality by checking all four possible causes, decide whether the AI is actually at fault, and write a test record that sends the finding to the right owner.

Confirming that quality dropped is only half of an audit. The half that makes it evidence is naming why it dropped, with proof, so the right person can act on it. In Lab 2.1 the cause was a change of AI model. This lab is the next month's review: the score is below the alarm floor again, the model has changed again, and it would be easy to blame it a second time. It is not the model this time. You test the drop against all four causes of degradation, find that a company policy changed, and work out that PolicyPal is quoting the new policy correctly: it is the Quality Standard that is out of date.

By the end of this lab you will be able to diagnose and document a quality drop in any AI workflow that keeps an activity log, without assuming the cause: decide whether a drop is big enough to investigate, find when it started and which kinds of answer it affects, test it against the four causes of degradation, tell a changed policy apart from a changed input, and write the conclusion of a test record that sends the finding to the right owner.

## Background (Why This Matters)

```text
Score below the alarm level again
       │
       ▼
When did it start, and which answers dropped?
       │
       ▼
Check all four causes: model, prompt, inputs, policy
       │
       ▼
Is the AI actually wrong, or is the yardstick out of date?
       │
       ▼
Conclusion, and who to tell
```

The cause decides who can fix it. Blaming the wrong thing sends the problem to people who cannot fix it, and sometimes the AI is not broken at all. It is a month later, and time for PolicyPal's next monthly review. After Lab 2.1, the platform team moved PolicyPal back to the AI model it used before. A colleague has already marked 20 of PolicyPal's answers from 26 August to 18 September against the Quality Standard. The score is higher than August's 81, but it is still below where it should be. Your job is to find out why, and to write it down so someone else can act on it. Do not assume it is the same cause as last month.

**Words you will see in this lab**
- **Business Quality Score:** a score out of 100 for how well PolicyPal's answers are doing.
- **Baseline:** the score PolicyPal got when it was first checked. New scores are compared with it.
- **AI model:** the "brain" inside PolicyPal. Another company makes it.
- **Prompt:** the instructions PolicyPal is given.
- **Activity log:** a diary the platform keeps of every time the AI is used, including which model was running and which documents it read.
- **Effective date:** the date a policy starts to apply.
- **Test record:** a short written report of a check: what you tested, what you found, and what happens next.

## Procedure

1. **Decide whether this drop is big enough to investigate.** The score box below adds up a colleague's marks on 20 of PolicyPal's answers from 26 August to 18 September, the same way you marked answers in Lab 2.1.

    | Statistic | Value |
    |---|---|
    | Current Business Quality Score | 83 |
    | Recorded baseline | 88 |
    | Change (points) | -5 |
    | Responses below their own baseline | 5 of 20 |

    How each criterion moved:

    | Criterion | Passing now | Passing at baseline | Change |
    |---|---|---|---|
    | c1 Current, named source | 16 of 20 | 16 of 20 | +0 |
    | c2 Exact figure or entitlement | 13 of 20 | 18 of 20 | -5 |
    | c3 Answers the question asked | 19 of 20 | 19 of 20 | +0 |
    | c4 Human referral where required | 18 of 20 | 18 of 20 | +0 |

    #### 8. Quality alarm level

    Investigate the workflow when the Business Quality Score falls below 85, or drops more than 5 points from the recorded baseline, whichever comes first. A movement inside that band is logged and watched; a movement past it triggers a diagnosis.

    First, decide whether the drop is big enough that the company's own rules say you must investigate.

    ***Has the score reached the alarm level?***

    - Yes
    - No

    <details><summary>Show the answer</summary>

    `Yes`. The score of 83 is below the floor of 85. It has dropped exactly 5 points from the baseline of 88, which is not more than the limit of 5, so only one of the two lines is crossed. Crossing either line is enough, so you must investigate.

    </details>

0. **Find when the drop started and which answers it affects.** Below are the 20 marked answers in date order. Each has a mark at baseline and a mark now, out of 4.

    | Case | Date | Question | Mark at baseline (of 4) | Mark now (of 4) |
    |---|---|---|---|---|
    | L22-01 | 2026-08-26 | How many PTO days do I accrue in my second year? | 4 | 4 |
    | L22-02 | 2026-08-26 | What is the mileage reimbursement rate for my own car? | 4 | 4 |
    | L22-03 | 2026-08-27 | How long do I have to enroll in the health plan after I start? | 4 | 4 |
    | L22-04 | 2026-08-27 | How much is the home-office stipend? | 2 | 2 |
    | L22-05 | 2026-08-28 | How many days of bereavement leave do I get? | 4 | 4 |
    | L22-06 | 2026-08-28 | What is the domestic meal per diem? | 4 | 4 |
    | L22-07 | 2026-08-31 | My expense claim was rejected and I think that is wrong. What can I do? | 2 | 2 |
    | L22-08 | 2026-09-01 | How many unused PTO days can I carry into next year? | 4 | 4 |
    | L22-09 | 2026-09-02 | How many PTO days do I get in my second year? | 4 | 3 |
    | L22-10 | 2026-09-02 | What mileage rate do I claim for personal vehicle use? | 3 | 3 |
    | L22-11 | 2026-09-03 | What is the carryover cap for unused PTO? | 4 | 3 |
    | L22-12 | 2026-09-04 | What is the company 401(k) match? | 3 | 3 |
    | L22-13 | 2026-09-08 | How many bereavement days am I entitled to? | 4 | 3 |
    | L22-14 | 2026-09-08 | Is jury duty paid? | 4 | 4 |
    | L22-15 | 2026-09-09 | What is the per diem for meals on a domestic trip? | 3 | 3 |
    | L22-16 | 2026-09-10 | My doctor has recommended a standing desk. How do I get one? | 3 | 3 |
    | L22-17 | 2026-09-14 | How much notice should I give for a week of planned PTO? | 4 | 3 |
    | L22-18 | 2026-09-15 | When can I change my benefits after getting married? | 3 | 3 |
    | L22-19 | 2026-09-16 | How many PTO days will I get in my first year? | 4 | 3 |
    | L22-20 | 2026-09-18 | How long is the enrollment window for the health plan? | 4 | 4 |

    First find the first date on which an answer's mark now is lower than its mark at baseline. Then look at the questions of the answers that dropped: are they all kinds of question, or one kind?

    ***Date the quality drop begins.***

    ***Which answers dropped?***

    - All kinds of questions
    - Only questions about paid time off (PTO)
    - Only questions about expenses
    - Only questions about benefits

    <details><summary>Hint: where to look</summary>

    Compare the two mark columns row by row. For every row where the mark now is lower, read its question.

    </details>

    <details><summary>Show the answer</summary>

    - The drop begins on `2026-09-02`.
    - `Only questions about paid time off (PTO)`. The five answers that dropped (`L22-09`, `L22-11`, `L22-13`, `L22-17`, `L22-19`) are all about PTO. Expense and benefits answers from the same weeks kept their marks.

    </details>

0. **Check the AI model first.** When an AI tool's answers get worse, there are four usual reasons:

    - The AI model changed: the company that makes the AI's "brain" swapped or updated it.
    - The prompt changed: someone changed the instructions given to the AI.
    - The inputs changed: the documents the AI reads from changed.
    - The company policy changed: the real rules changed, so the answers change with them.

    Last month the cause was a model change, so that is the first thing most people check. Below is the activity log, showing which AI model was running each time PolicyPal was used. Your drop date is 2026-09-02.

    | CreationTime | ModelProviderName | ModelName | ModelVersion |
    |---|---|---|---|
    | 2026-08-24T10:38:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-24T10:38:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-24T12:26:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-24T12:26:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-24T16:17:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-24T16:17:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-25T08:02:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-25T08:02:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-25T09:26:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-25T09:26:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-25T14:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-25T14:47:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-26T08:38:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-26T08:38:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-26T08:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-26T08:41:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-26T10:12:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-26T10:12:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-27T09:53:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-27T09:53:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-27T15:12:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-27T15:12:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-28T11:20:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-28T11:20:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-28T13:05:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-28T13:05:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-31T08:20:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-31T08:20:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-31T12:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-31T12:47:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-01T10:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-01T10:41:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-02T08:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-02T08:41:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-02T14:53:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-02T14:53:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-03T08:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-03T08:41:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-03T12:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-03T12:47:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-04T12:20:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-04T12:20:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-07T14:38:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-07T14:38:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-08T10:05:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-08T10:05:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-08T14:12:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-08T14:12:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-09T16:53:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-09T16:53:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-10T08:53:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-10T08:53:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-10T10:26:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-10T10:26:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-11T17:26:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-11T17:26:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-14T13:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-14T13:41:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-15T13:20:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-15T13:20:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-15T14:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-15T14:47:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-16T10:34:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-16T10:34:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-17T08:26:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-17T08:26:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-18T12:53:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-09-18T12:53:03Z | OpenAI | gpt-4o | 2024-11-20 |

    Did the model change? If it did, does the timing fit the drop?

    ***The AI model.***

    - Ruled out: the model did not change
    - Ruled out: the model changed, but the timing does not fit the drop
    - Not ruled out: the model changed just before the drop

    <details><summary>Show the answer</summary>

    `Ruled out: the model changed, but the timing does not fit the drop`. The model did change on 2026-08-25, from gpt-55-high back to gpt-4o, the model PolicyPal used before Lab 2.1. But the answers kept their marks for a whole week after that, and the drop only starts on 2026-09-02. If the model were the cause, the drop would start straight after the change.

    </details>

0. **Check whether the prompt changed.** The prompt is the set of instructions PolicyPal is given. You cannot see the prompt itself, but the platform gives PolicyPal a new version number, AgentVersion, every time someone changes its instructions and publishes them.

    Below is the activity log again, showing AgentVersion.

    | CreationTime | AgentVersion |
    |---|---|
    | 2026-08-24T10:38:00Z | 1.4 |
    | 2026-08-24T10:38:03Z | 1.4 |
    | 2026-08-24T12:26:00Z | 1.4 |
    | 2026-08-24T12:26:03Z | 1.4 |
    | 2026-08-24T16:17:00Z | 1.4 |
    | 2026-08-24T16:17:03Z | 1.4 |
    | 2026-08-25T08:02:00Z | 1.4 |
    | 2026-08-25T08:02:03Z | 1.4 |
    | 2026-08-25T09:26:00Z | 1.4 |
    | 2026-08-25T09:26:03Z | 1.4 |
    | 2026-08-25T14:47:00Z | 1.4 |
    | 2026-08-25T14:47:03Z | 1.4 |
    | 2026-08-26T08:38:00Z | 1.4 |
    | 2026-08-26T08:38:03Z | 1.4 |
    | 2026-08-26T08:41:00Z | 1.4 |
    | 2026-08-26T08:41:03Z | 1.4 |
    | 2026-08-26T10:12:00Z | 1.4 |
    | 2026-08-26T10:12:03Z | 1.4 |
    | 2026-08-27T09:53:00Z | 1.4 |
    | 2026-08-27T09:53:03Z | 1.4 |
    | 2026-08-27T15:12:00Z | 1.4 |
    | 2026-08-27T15:12:03Z | 1.4 |
    | 2026-08-28T11:20:00Z | 1.4 |
    | 2026-08-28T11:20:03Z | 1.4 |
    | 2026-08-28T13:05:00Z | 1.4 |
    | 2026-08-28T13:05:03Z | 1.4 |
    | 2026-08-31T08:20:00Z | 1.4 |
    | 2026-08-31T08:20:03Z | 1.4 |
    | 2026-08-31T12:47:00Z | 1.4 |
    | 2026-08-31T12:47:03Z | 1.4 |
    | 2026-09-01T10:41:00Z | 1.4 |
    | 2026-09-01T10:41:03Z | 1.4 |
    | 2026-09-02T08:41:00Z | 1.4 |
    | 2026-09-02T08:41:03Z | 1.4 |
    | 2026-09-02T14:53:00Z | 1.4 |
    | 2026-09-02T14:53:03Z | 1.4 |
    | 2026-09-03T08:41:00Z | 1.4 |
    | 2026-09-03T08:41:03Z | 1.4 |
    | 2026-09-03T12:47:00Z | 1.4 |
    | 2026-09-03T12:47:03Z | 1.4 |
    | 2026-09-04T12:20:00Z | 1.4 |
    | 2026-09-04T12:20:03Z | 1.4 |
    | 2026-09-07T14:38:00Z | 1.4 |
    | 2026-09-07T14:38:03Z | 1.4 |
    | 2026-09-08T10:05:00Z | 1.4 |
    | 2026-09-08T10:05:03Z | 1.4 |
    | 2026-09-08T14:12:00Z | 1.4 |
    | 2026-09-08T14:12:03Z | 1.4 |
    | 2026-09-09T16:53:00Z | 1.4 |
    | 2026-09-09T16:53:03Z | 1.4 |
    | 2026-09-10T08:53:00Z | 1.4 |
    | 2026-09-10T08:53:03Z | 1.4 |
    | 2026-09-10T10:26:00Z | 1.4 |
    | 2026-09-10T10:26:03Z | 1.4 |
    | 2026-09-11T17:26:00Z | 1.4 |
    | 2026-09-11T17:26:03Z | 1.4 |
    | 2026-09-14T13:41:00Z | 1.4 |
    | 2026-09-14T13:41:03Z | 1.4 |
    | 2026-09-15T13:20:00Z | 1.4 |
    | 2026-09-15T13:20:03Z | 1.4 |
    | 2026-09-15T14:47:00Z | 1.4 |
    | 2026-09-15T14:47:03Z | 1.4 |
    | 2026-09-16T10:34:00Z | 1.4 |
    | 2026-09-16T10:34:03Z | 1.4 |
    | 2026-09-17T08:26:00Z | 1.4 |
    | 2026-09-17T08:26:03Z | 1.4 |
    | 2026-09-18T12:53:00Z | 1.4 |
    | 2026-09-18T12:53:03Z | 1.4 |

    Is AgentVersion the same before and after your drop date (2026-09-02)?

    ***The prompt.***

    - Ruled out: AgentVersion is the same before and after the drop
    - Not ruled out: AgentVersion changed around the date of the drop

    <details><summary>Show the answer</summary>

    `Ruled out`. AgentVersion is 1.4 on every row. Nobody published new instructions.

    </details>

0. **Check the documents and the policy.** The last two causes are close cousins, and you tell them apart like this:

    - The inputs changed if the documents PolicyPal reads changed but the real rules did not. For example, someone uploaded a draft by mistake.
    - The company policy changed if the rules themselves changed, and PolicyPal is now reading and quoting the new, official policy.

    Below are two tables. The first shows which documents PolicyPal read each time (AccessedResources). The second shows the policy each answer cites, with its effective date.

    Documents PolicyPal read:

    | CreationTime | AccessedResources |
    |---|---|
    | 2026-08-24T10:38:00Z | Benefits Guide 2025.docx |
    | 2026-08-24T10:38:03Z | Benefits Guide 2025.docx |
    | 2026-08-24T12:26:00Z | PTO Policy 2025.docx |
    | 2026-08-24T12:26:03Z | PTO Policy 2025.docx |
    | 2026-08-24T16:17:00Z | Expense & Travel Policy 2025.docx |
    | 2026-08-24T16:17:03Z | Expense & Travel Policy 2025.docx |
    | 2026-08-25T08:02:00Z | Code of Conduct 2025.docx |
    | 2026-08-25T08:02:03Z | Code of Conduct 2025.docx |
    | 2026-08-25T09:26:00Z | PTO Policy 2025.docx |
    | 2026-08-25T09:26:03Z | PTO Policy 2025.docx |
    | 2026-08-25T14:47:00Z | Expense & Travel Policy 2025.docx |
    | 2026-08-25T14:47:03Z | Expense & Travel Policy 2025.docx |
    | 2026-08-26T08:38:00Z | Benefits Guide 2025.docx |
    | 2026-08-26T08:38:03Z | Benefits Guide 2025.docx |
    | 2026-08-26T08:41:00Z | Expense & Travel Policy 2025.docx |
    | 2026-08-26T08:41:03Z | Expense & Travel Policy 2025.docx |
    | 2026-08-26T10:12:00Z | PTO Policy 2025.docx |
    | 2026-08-26T10:12:03Z | PTO Policy 2025.docx |
    | 2026-08-27T09:53:00Z | Remote Work Policy 2024.docx |
    | 2026-08-27T09:53:03Z | Remote Work Policy 2024.docx |
    | 2026-08-27T15:12:00Z | Benefits Guide 2025.docx |
    | 2026-08-27T15:12:03Z | Benefits Guide 2025.docx |
    | 2026-08-28T11:20:00Z | Expense & Travel Policy 2025.docx |
    | 2026-08-28T11:20:03Z | Expense & Travel Policy 2025.docx |
    | 2026-08-28T13:05:00Z | PTO Policy 2025.docx |
    | 2026-08-28T13:05:03Z | PTO Policy 2025.docx |
    | 2026-08-31T08:20:00Z | Expense & Travel Policy 2025.docx |
    | 2026-08-31T08:20:03Z | Expense & Travel Policy 2025.docx |
    | 2026-08-31T12:47:00Z | PTO Policy 2025.docx |
    | 2026-08-31T12:47:03Z | PTO Policy 2025.docx |
    | 2026-09-01T10:41:00Z | PTO Policy 2025.docx |
    | 2026-09-01T10:41:03Z | PTO Policy 2025.docx |
    | 2026-09-02T08:41:00Z | Expense & Travel Policy 2025.docx |
    | 2026-09-02T08:41:03Z | Expense & Travel Policy 2025.docx |
    | 2026-09-02T14:53:00Z | PTO Policy 2026.docx |
    | 2026-09-02T14:53:03Z | PTO Policy 2026.docx |
    | 2026-09-03T08:41:00Z | PTO Policy 2026.docx |
    | 2026-09-03T08:41:03Z | PTO Policy 2026.docx |
    | 2026-09-03T12:47:00Z | Expense & Travel Policy 2025.docx |
    | 2026-09-03T12:47:03Z | Expense & Travel Policy 2025.docx |
    | 2026-09-04T12:20:00Z | Benefits Guide 2025.docx |
    | 2026-09-04T12:20:03Z | Benefits Guide 2025.docx |
    | 2026-09-07T14:38:00Z | PTO Policy 2026.docx |
    | 2026-09-07T14:38:03Z | PTO Policy 2026.docx |
    | 2026-09-08T10:05:00Z | PTO Policy 2026.docx |
    | 2026-09-08T10:05:03Z | PTO Policy 2026.docx |
    | 2026-09-08T14:12:00Z | PTO Policy 2026.docx |
    | 2026-09-08T14:12:03Z | PTO Policy 2026.docx |
    | 2026-09-09T16:53:00Z | Expense & Travel Policy 2025.docx |
    | 2026-09-09T16:53:03Z | Expense & Travel Policy 2025.docx |
    | 2026-09-10T08:53:00Z | Code of Conduct 2025.docx |
    | 2026-09-10T08:53:03Z | Code of Conduct 2025.docx |
    | 2026-09-10T10:26:00Z | Benefits Guide 2025.docx |
    | 2026-09-10T10:26:03Z | Benefits Guide 2025.docx |
    | 2026-09-11T17:26:00Z | PTO Policy 2026.docx |
    | 2026-09-11T17:26:03Z | PTO Policy 2026.docx |
    | 2026-09-14T13:41:00Z | PTO Policy 2026.docx |
    | 2026-09-14T13:41:03Z | PTO Policy 2026.docx |
    | 2026-09-15T13:20:00Z | Benefits Guide 2025.docx |
    | 2026-09-15T13:20:03Z | Benefits Guide 2025.docx |
    | 2026-09-15T14:47:00Z | Code of Conduct 2025.docx |
    | 2026-09-15T14:47:03Z | Code of Conduct 2025.docx |
    | 2026-09-16T10:34:00Z | PTO Policy 2026.docx |
    | 2026-09-16T10:34:03Z | PTO Policy 2026.docx |
    | 2026-09-17T08:26:00Z | Expense & Travel Policy 2025.docx |
    | 2026-09-17T08:26:03Z | Expense & Travel Policy 2025.docx |
    | 2026-09-18T12:53:00Z | Benefits Guide 2025.docx |
    | 2026-09-18T12:53:03Z | Benefits Guide 2025.docx |

    The policy each answer cites:

    | Case | Date | Cited source |
    |---|---|---|
    | L22-01 | 2026-08-26 | PTO Policy 2025 (effective 2025-01-01) |
    | L22-02 | 2026-08-26 | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | L22-03 | 2026-08-27 | Benefits Guide 2025 (effective 2025-01-01) |
    | L22-04 | 2026-08-27 | company policy |
    | L22-05 | 2026-08-28 | PTO Policy 2025 (effective 2025-01-01) |
    | L22-06 | 2026-08-28 | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | L22-07 | 2026-08-31 | company policy |
    | L22-08 | 2026-09-01 | PTO Policy 2025 (effective 2025-01-01) |
    | L22-09 | 2026-09-02 | PTO Policy 2026 (effective 2026-09-01) |
    | L22-10 | 2026-09-02 | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | L22-11 | 2026-09-03 | PTO Policy 2026 (effective 2026-09-01) |
    | L22-12 | 2026-09-04 | company policy |
    | L22-13 | 2026-09-08 | PTO Policy 2026 (effective 2026-09-01) |
    | L22-14 | 2026-09-08 | PTO Policy 2026 (effective 2026-09-01) |
    | L22-15 | 2026-09-09 | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | L22-16 | 2026-09-10 | Code of Conduct 2025 (effective 2025-01-01) |
    | L22-17 | 2026-09-14 | PTO Policy 2026 (effective 2026-09-01) |
    | L22-18 | 2026-09-15 | the benefits guide |
    | L22-19 | 2026-09-16 | PTO Policy 2026 (effective 2026-09-01) |
    | L22-20 | 2026-09-18 | Benefits Guide 2025 (effective 2025-01-01) |

    Look at what appears around your drop date (2026-09-02), and choose what you found.

    ***The documents and the policy.***

    - Neither changed: the same documents are read and cited throughout
    - The inputs changed: a draft or wrong document was added
    - The company policy changed: a new, official policy took effect

    <details><summary>Show the answer</summary>

    `The company policy changed`. From 2026-09-02, PTO questions read PTO Policy 2026.docx instead of the 2025 version, and the answers cite PTO Policy 2026 (effective 2026-09-01). It is a named policy with an official start date, one day before the drop, so the rules really changed.

    </details>

0. **Decide whether the new answers are actually wrong.** The five answers that dropped all lost their mark on c2, the rule that every figure must match the reference figures in the Quality Standard.

    | Case | Date | Question | Assistant response | Cited source |
    |---|---|---|---|---|
    | L22-09 | 2026-09-02 | How many PTO days do I get in my second year? | You accrue 12 PTO days per year in years one through four of employment. | PTO Policy 2026 (effective 2026-09-01) |
    | L22-11 | 2026-09-03 | What is the carryover cap for unused PTO? | You can carry up to 3 unused PTO days into the next year. | PTO Policy 2026 (effective 2026-09-01) |
    | L22-13 | 2026-09-08 | How many bereavement days am I entitled to? | Bereavement leave is 3 working days per eligible event. | PTO Policy 2026 (effective 2026-09-01) |
    | L22-17 | 2026-09-14 | How much notice should I give for a week of planned PTO? | Give at least three weeks' notice for planned PTO of three or more consecutive days. | PTO Policy 2026 (effective 2026-09-01) |
    | L22-19 | 2026-09-16 | How many PTO days will I get in my first year? | You accrue 12 PTO days per year in years one through four of employment. | PTO Policy 2026 (effective 2026-09-01) |

    | Topic | Current figure | Source |
    |---|---|---|
    | PTO accrual, years one to four | 15 days per year | PTO Policy 2025 |
    | Notice for planned PTO of 3+ consecutive days | At least two weeks | PTO Policy 2025 |
    | Unused PTO carried into the next year | Up to 5 days | PTO Policy 2025 |
    | Bereavement leave | 5 working days per eligible event | PTO Policy 2025 |
    | Mileage reimbursement, personal vehicle | $0.67 per mile | Expense & Travel Policy 2025 |
    | Domestic meal per diem | $64 per day | Expense & Travel Policy 2025 |
    | Health plan enrollment window for new hires | 30 days from hire date | Benefits Guide 2025 |
    | Benefits change after a qualifying life event | Within 30 days of the event | Benefits Guide 2025 |
    | 401(k) match | 100% of the first 4% of eligible pay | Benefits Guide 2025 |

    Compare the figures in the answers with the reference figures above (section 9 of the Quality Standard), and with the policy each answer cites. Is PolicyPal wrong, or is something else out of date?

    ***Are the new PTO answers wrong?***

    - Yes: PolicyPal should still give the 2025 figures
    - No: PolicyPal is quoting the new policy correctly; the Quality Standard's figures are out of date

    <details><summary>Show the answer</summary>

    `No`. PolicyPal gives the figures from PTO Policy 2026, which is now the official policy. The answers were marked down only because the reference figures in the Quality Standard still list the 2025 figures (15 days a year, a carryover cap of 5, 5 bereavement days, two weeks' notice). The yardstick is out of date, not the tool.

    </details>

0. **Write the conclusion.** The conclusion is the part of the test record a busy person reads first. It answers "so what happened?"

    Draw on the four cause checks you just completed (the model, the prompt, the documents, and whether the answers are wrong).

    ***In two or three sentences, what caused the drop, the evidence for it, and whether PolicyPal itself is at fault.***

    <details><summary>Hint: what to synthesize</summary>

    Summarize what caused the drop and whether PolicyPal itself is at fault, or whether something else (the reference figures in the standard) is out of date.

    </details>

0. **Decide who to speak to.** Send a finding to whoever can change the thing that is out of date.

    ***Who do you speak to, and what happens next?***

    - The platform / technical owner, to change the model again
    - The team that owns the HR policy library, to confirm PTO Policy 2026 is the official policy; then I update the Quality Standard's figures and re-set the baseline
    - The HR operations reviewers, to mark the answers again
    - No one: PolicyPal is right, so there is nothing to do

    ***Why? One line.***

    <details><summary>Show the answer</summary>

    `The team that owns the HR policy library`, then you update the standard. The policy changed, so the owners of the policy confirm it is official, and you, as the Business AI Owner, update the reference figures in the Quality Standard and re-set the baseline. The platform team cannot help: nothing is wrong with the model. Doing nothing is also wrong, because every future review would keep raising the same false alarm.

    </details>

## Conclusion

In this lab you confirmed that a drop in the Business Quality Score was big enough to investigate, found when it started and what it affected, and tested it against all four causes of degradation instead of assuming last month's answer. The model had changed, but the timing ruled it out; the real cause was a new company policy, and PolicyPal was quoting it correctly. A drop in the score does not always mean the AI is broken. Sometimes it means the yardstick needs updating, and the finding goes to the policy owner, not the platform team.
