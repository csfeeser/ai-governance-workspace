# Triaged Incident: Customer-Facing Support Bot (data exposure)

*Supplied for the Lab 4.2 Bronze challenge. This incident has already been triaged.*

## Triage result

| Field | Value |
|---|---|
| Category | Security or privacy |
| Responsible owner | The responsible information-security function, with the legal function notified in parallel |
| Urgency | Immediate: possible ongoing exposure |

## Supporting facts

- A customer-facing support bot returned another customer's account balance and the last
  four digits of a payment card in a chat reply.
- Noticed on 2026-09-21 when the receiving customer forwarded the transcript to a
  support agent.
- Scope is not yet known: it is unclear how many sessions were affected or whether the
  exposure is still occurring.
- The bot draws on a shared account-lookup connection.
- No mitigation has been applied yet.

## Evidence available

*This triage record is the evidence; there is no separate file to open for each item.*

- The forwarded transcript showing the exposed fields: described above
- The bot's account-lookup connection configuration: referenced above
