# Write the Escalation Ticket

## Objectives

In this lab, you will write an escalation ticket that gives a responsible owner everything they need to act.

Escalations fail in practice by describing a feeling instead of a frequency. "The assistant seems worse" is not a ticket. In Lab 4.1 you triaged a sales-support assistant that started writing long, off-tone customer emails, and routed it to the platform team. In this lab you write that team the ticket: what was observed, how often and since when, the proof, what you have ruled out, what it is costing the business, the specific thing you are asking for, and when you need a reply. The case file you work from mixes checkable facts with feelings and guesses, and part of the job is telling them apart.

By the end of this lab you will be able to write an escalation an owner can act on without coming back to you with questions: state what was observed as facts the owner can check, choose the frequency that gives a fair picture, choose the evidence that lets the owner check every claim, say what you have ruled out, and make one specific ask with a response-by date that matches the urgency.

## Background (Why This Matters)

```text
Case file: report + team notes + records
       │
       ▼
Facts, not feelings: what was observed, how often, since when
       │
       ▼
Evidence attached + what's already ruled out
       │
       ▼
Business impact + one specific ask + response-by date
```

If your message is vague, the other person has to come back with questions, and the fix is delayed. A good message means they can start work straight away. The test of a ticket: can the owner start work without coming back to you with a question?

**Words you will see in this lab**
- **Ticket:** a written request that asks someone to fix something. It has fixed parts, so nothing is left out.
- **Escalation:** passing a problem to the person who can fix it.
- **Evidence:** the proof behind what you are saying, such as a count, a date, or a record.
- **Ruled out:** checked and found not to be the cause. Saying what you have ruled out saves the other person from checking it again.
- **Case file:** everything gathered about one incident: the report that came in, notes from the people affected, and what the records show.
- **The ask:** the one clear thing you want the other person to do.

## Procedure

1. **Say what is happening.** In Lab 4.1 you sorted incident 2, the sales-support assistant that started writing long, off-tone customer emails, and routed it to the team responsible for the platform and the vendor relationship. Now you write the ticket you send them: a message that says what is wrong and what you need from them.

    Below is the case file: the report that came in, what the sales team told you, and what the records show. Not everything in it belongs in a ticket.

    #### Case File: Sales-Support Assistant (Claude)

    Today is Monday 2026-09-21.

    **Triage result** (what you decided in Lab 4.1):

    | Field | Value |
    |---|---|
    | Category | Technical or vendor |
    | Routed to | The team responsible for the platform and the vendor relationship |
    | What they are responsible for | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | Action | Escalate soon: a real error or harm to fix; raise it this week, not at the monthly review |

    **The report that came in**, posted to the AI incident queue on 2026-09-15 by the sales team lead:

    > Since the update the sales assistant has gone weird. The emails are way too long and chatty, and customers are noticing. My reps are fixing drafts by hand. Can someone sort this out ASAP?

    **Sales team notes**, from speaking to the sales team on 2026-09-17:

    - The team lead first noticed the long drafts on 2026-09-10.
    - The team lead says the assistant "feels lazier" and is "less professional than it used to be."
    - One rep thinks the vendor has "cut costs and switched us to a cheaper AI."
    - On Friday 2026-09-18 the team lead checked 5 drafts. 3 of them were off-tone.
    - Reps say they now rewrite most drafts by hand. Nobody has timed how long this takes.
    - Since 2026-09-01, 9 customers have replied to an email to ask about its tone.

    **What the records show:**

    - Activity log: on 2026-08-31 the assistant's model version changed from `2025-10-01` to `2026-08-20`. The vendor (Anthropic) is the same.
    - Draft length: in July the average draft was 70 words (three or four sentences). Since 2026-09-01 it is 190 words (two or three paragraphs), and the drafts read as informal.
    - The Sales Tone Standard is the sales team's written rules for how customer emails should sound.
    - Scored sample, July 2026: 50 drafts scored against the Sales Tone Standard. 3 fail (6%).
    - Scored sample, 2026-09-01 to 2026-09-18: 50 drafts scored against the Sales Tone Standard. 18 fail (36%).
    - Business Quality Score for this workflow: 86 in July, 68 now.
    - About 200 customer emails a week are drafted by the assistant.

    Start with what was observed: what the assistant is doing, in facts the owner could check for themselves. Leave out feelings and guesses. The owner cannot check those.

    ***What was observed.***

    <details><summary>Hint: where to look</summary>

    Look in "What the records show" for the line on draft length. It gives the length before and after, and the date the drafts changed. The "Sales team notes" are mostly feelings ("feels lazier") and a guess about the cause, and the date there is when the team lead noticed, not when the drafts changed.

    </details>

    <details><summary>Show the answer</summary>

    "Since 2026-09-01, drafts average 190 words (two or three paragraphs), up from 70 words in July, and read as informal."

    Left out: "feels lazier" and "less professional" are feelings, and "switched us to a cheaper AI" is a guess. The date is when the drafts changed (2026-09-01), not when the team lead first noticed (2026-09-10).

    </details>

0. **Say how often, and since when.** A frequency lets the owner judge how big the problem is. The case file has several numbers that could go here. Choose the one that gives the owner a fair picture.

    ***How often, and since when.***

    - Since 2026-09-01 (three weeks): 18 of 50 sampled drafts fail the tone standard (36%), against 3 of 50 in July
    - Since 2026-09-10 (eleven days): 3 of the 5 drafts the team lead checked on Friday 2026-09-18 were off-tone (60%)
    - Since 2026-09-01 (three weeks): 9 customers have replied to ask about tone, out of about 600 emails sent (2%)
    - Since 2026-09-15 (six days): the workflow's Business Quality Score has dropped from 86 to 68, a fall of 18 points

    <details><summary>Show the answer</summary>

    `Since 2026-09-01 (three weeks): 18 of 50 sampled drafts fail the tone standard (36%), against 3 of 50 in July`. It starts when the drafts changed, counts a fair sample, and compares it with before.

    - The team lead's check: 2026-09-10 is when they noticed, not when it started, and 5 drafts are too few to judge from.
    - The customer replies: most customers who get an odd email say nothing, and reps rewrite many drafts before sending, so this undercounts.
    - The score: 2026-09-15 is when the report came in, and a score says how bad things are, not how often a draft fails.

    </details>

0. **Choose the proof to attach.** A claim with no proof is easy to dismiss. From the files alone, the owner should be able to check what you observed, how often it happens, and that the model changed. Tick each file you would attach, and only those.

    | File | What it contains |
    |---|---|
    | `sample-2026-09.csv` | The 50 drafts from 2026-09-01 to 2026-09-18, each with its score |
    | `sample-2026-07.csv` | The 50 drafts from July, each with its score |
    | `activity-log-2026-08-31.csv` | The activity-log lines showing the model version change |
    | `sales-tone-standard.pdf` | The standard both samples were scored against |
    | `team-lead-report.txt` | The report the team lead posted to the incident queue |
    | `customer-replies.eml` | The 9 customer replies about tone |

    ***Evidence attached (check all that apply).***

    - [ ] sample-2026-09.csv: the 50 drafts from 2026-09-01 to 2026-09-18, each with its score
    - [ ] sample-2026-07.csv: the 50 drafts from July, each with its score
    - [ ] activity-log-2026-08-31.csv: the activity-log lines showing the model version change
    - [ ] sales-tone-standard.pdf: the standard both samples were scored against
    - [ ] team-lead-report.txt: the report the team lead posted to the incident queue
    - [ ] customer-replies.eml: the 9 customer replies about tone

    <details><summary>Show the answer</summary>

    Attach four files: `sample-2026-09.csv`, `sample-2026-07.csv`, `activity-log-2026-08-31.csv` and `sales-tone-standard.pdf`.

    - The two samples show how often drafts fail, now and before the change.
    - The standard shows what "fail" means, so the owner can check the scores.
    - The log shows the model change.
    - Leave out the team lead's report and the customer replies. They show how people feel about the drafts. They do not help the owner check what you observed, how often it happens, or the model change.

    </details>

0. **Say what you have already ruled out.** Saying what you have already ruled out saves the owner checking it again. The drafts changed on 2026-09-01. Using the checks below, write each possible cause you have ruled out, and how you know.

    #### Checks already made

    | What could have changed | Last changed |
    |---|---|
    | The assistant's model version | 2026-08-31 |
    | The system prompt (the assistant's standing instructions) | 2026-06-30 |
    | The product sheets the assistant reads from | 2026-08-17 |
    | The Sales Tone Standard | 2026-02-02 |
    | How reps word their requests (50 requests compared with July) | No difference found |

    ***Already ruled out.***

    <details><summary>Hint: where to look</summary>

    Go down the Last changed column above and compare each date with 2026-09-01, when the drafts changed. A change made long before that date, with the drafts still fine for weeks afterwards, did not cause it. A row that shows no difference did not cause it either. One row changed the day before.

    </details>

    <details><summary>Show the answer</summary>

    "Ruled out: the system prompt (unchanged since 2026-06-30), the product sheets (last changed 2026-08-17, and drafts were fine for two weeks after), the Sales Tone Standard (unchanged since 2026-02-02), and how reps word their requests (no difference from July)."

    The model version is the one thing that changed the day before the drafts did, so it is not ruled out. Ruling out the Sales Tone Standard also tells the owner the drafts got worse; the yardstick did not move.

    </details>

0. **Say what it is costing.** A problem gets fixed faster when the owner can see what it costs. Write what this is costing the business, using only facts from the case file. "Customers are noticing" is a feeling; a count is a fact.

    ***Business impact.***

    <details><summary>Hint: where to look</summary>

    In "What the records show" (Step 1), find how many customer emails a week the assistant drafts, and what share of the recent sample fails the tone standard. In "Sales team notes", find what the reps are doing about it and how many customers have replied about the tone. Leave out anything with no number or record behind it.

    </details>

    <details><summary>Show the answer</summary>

    "About 200 customer emails a week are drafted by the assistant, and 36% of sampled drafts fail the tone standard. Reps are rewriting drafts by hand, and 9 customers have replied about the tone since 2026-09-01. Off-tone emails reach customers under the company's name."

    </details>

0. **Say exactly what you want them to do.** This is the most important part of the ticket. "Please look into this" gets nothing specific done. The ask must be something this owner can do, and it must fix the problem you have described. The owner is responsible for the AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors.

    ***The ask.***

    - Move the assistant back to model version 2025-10-01 and keep it there until 2026-08-20 passes the tone standard
    - Rewrite the assistant's system prompt so its drafts are shorter and more formal, then re-score a sample of 50 drafts
    - Switch the assistant off for all sales reps until the vendor has fixed model version 2026-08-20 for this account
    - Find out why the assistant's drafts have become longer and less formal since 2026-09-01, and report back to us

    <details><summary>Show the answer</summary>

    `Move the assistant back to model version 2025-10-01` and keep it there until the new version passes the tone standard. The platform team runs the models, the drafts were fine on the old version, and it is a specific thing they can do.

    - Rewriting the system prompt: the prompt has not changed since June, so it is not the cause, and changing it is not the platform team's job.
    - Switching the assistant off: the old version worked, so reps would lose the tool for no reason. That is more than an "Escalate soon" problem needs.
    - Finding out why: this is "please look into this" with more words. You already know what changed.

    </details>

0. **Say when you need an answer.** People fit work around deadlines. With no deadline, your ticket goes to the bottom of the queue. Match the deadline to the action from Lab 4.1: Escalate soon (a real error or harm to fix; raise it this week, not at the monthly review). Today is Monday 2026-09-21.

    ***Response-by.***

    - By 17:00 today, Monday 2026-09-21: customers are getting off-tone emails every single day
    - By Thursday 2026-09-24 (three business days): a real harm to fix this week, nothing exposed
    - At the next monthly AI review in October: drafts are off-tone, but reps can still fix them by hand
    - Within 30 days, by 2026-10-21: the vendor has to be contacted before anything is able to change

    <details><summary>Show the answer</summary>

    `By Thursday 2026-09-24 (three business days)`. "Escalate soon" means raise it this week, so the owner needs to reply this week.

    - Today: that is for "Escalate immediately", when private data is exposed or harm is spreading right now.
    - The monthly review: "Escalate soon" says not to wait for it.
    - 30 days: the fix you asked for is a change the platform team makes themselves, and 30 days of off-tone emails is too long.

    </details>

## Conclusion

In this lab you wrote an escalation ticket that gives the responsible owner what was observed, how often and since when, the proof, what has been ruled out, the business impact, one specific ask, and a response-by date. You left out the feelings and guesses, used the date the problem started rather than the date someone noticed, and asked for something the owner can actually do. Tickets like this make up a workflow's incident history, which goes into the evidence packet in Module 5.
