# Case File: Sales-Support Assistant (Claude)

*Incident 2 from Lab 4.1. Today is Monday 2026-09-21. Use this case file to write the escalation ticket.*

## Triage result

What you decided in Lab 4.1:

| Field | Value |
|---|---|
| Category | Technical or vendor |
| Routed to | The team responsible for the platform and the vendor relationship |
| What they are responsible for | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
| Action | Escalate soon: a real error or harm to fix; raise it this week, not at the monthly review |

## The report that came in

Posted to the AI incident queue on 2026-09-15 by the sales team lead:

> Since the update the sales assistant has gone weird. The emails are way too long and chatty, and customers are noticing. My reps are fixing drafts by hand. Can someone sort this out ASAP?

## Sales team notes

What the sales team told you when you spoke to them on 2026-09-17:

- The team lead first noticed the long drafts on 2026-09-10.
- The team lead says the assistant "feels lazier" and is "less professional than it used to be".
- One rep thinks the vendor has "cut costs and switched us to a cheaper AI".
- On Friday 2026-09-18 the team lead checked 5 drafts. 3 of them were off-tone.
- Reps say they now rewrite most drafts by hand. Nobody has timed how long this takes.
- Since 2026-09-01, 9 customers have replied to an email to ask about its tone.

## What the records show

- Activity log: on 2026-08-31 the assistant's model version changed from `2025-10-01` to `2026-08-20`. The vendor (Anthropic) is the same.
- Draft length: in July the average draft was 70 words (three or four sentences). Since 2026-09-01 it is 190 words (two or three paragraphs), and the drafts read as informal.
- The Sales Tone Standard is the sales team's written rules for how customer emails should sound.
- Scored sample, July 2026: 50 drafts scored against the Sales Tone Standard. 3 fail (6%).
- Scored sample, 2026-09-01 to 2026-09-18: 50 drafts scored against the Sales Tone Standard. 18 fail (36%).
- Business Quality Score for this workflow: 86 in July, 68 now.
- About 200 customer emails a week are drafted by the assistant.

## Checks already made

| What could have changed | Last changed |
|---|---|
| The assistant's model version | 2026-08-31 |
| The system prompt (the assistant's standing instructions) | 2026-06-30 |
| The product sheets the assistant reads from | 2026-08-17 |
| The Sales Tone Standard | 2026-02-02 |
| How reps word their requests (50 requests compared with July) | No difference found |

## Files you could attach

| File | What it contains |
|---|---|
| `sample-2026-09.csv` | The 50 drafts from 2026-09-01 to 2026-09-18, each with its score |
| `sample-2026-07.csv` | The 50 drafts from July, each with its score |
| `activity-log-2026-08-31.csv` | The activity-log lines showing the model version change |
| `sales-tone-standard.pdf` | The standard both samples were scored against |
| `team-lead-report.txt` | The report the team lead posted to the incident queue |
| `customer-replies.eml` | The 9 customer replies about tone |
