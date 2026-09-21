# Triaged Incident — Sales-Support Assistant (Claude)

*This incident has already been triaged. Use it to write the escalation ticket in Lab 4.2.*

## Triage result

| Field | Value |
|---|---|
| Category | Technical / vendor |
| Responsible owner | The team responsible for the platform and the vendor relationship for this assistant |
| Urgency | Elevated — ongoing customer-facing impact, but not a security or privacy exposure |

## Supporting facts

- The assistant drafts customer-facing sales-support emails. About **200 emails per week**
  are produced through it.
- Behavior changed on **2026-08-12**: replies became roughly **40% longer** and shifted
  off-tone (informal, verbose).
- The platform activity log shows the **model identity changed on 2026-08-11**, the day
  before the change in output.
- A sample of **50 recent replies** scored against the tone standard: **18 fail** (36%).
- Business Quality Score moved from **86 to 68**.
- Already ruled out: the grounding content is unchanged; the system prompt is unchanged;
  the question phrasing coming from users is unchanged.

## Evidence available

*This triage record is the evidence; there is no separate file to open for each item.*

- The scored 50-reply sample: results summarized above (18 of 50 fail, 36%)
- The activity-log excerpt showing the model identity change: summarized above (2026-08-11)
- The tone standard the sample was scored against: referenced above
