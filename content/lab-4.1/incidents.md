# Incident Log — Five AI Workflow Incidents

*Five incidents raised against AI workflows this month. Triage each one in Lab 4.1.*

## Incident 1

PolicyPal, the HR policy assistant, has been answering PTO carryover questions using "PTO
Policy 2023." The current policy is "PTO Policy 2025," effective 2025-01-01; the 2023
document is still present in the grounding source. Over the past two weeks at least nine
employees were told the carryover cap is 10 days. The current cap is 5 days. Two employees
have already submitted year-end plans based on the wrong figure. The assistant's wording
and behavior are otherwise unchanged, and it cites the 2023 document by name when asked.

## Incident 2

A sales-support assistant built on Claude began producing noticeably longer, off-tone
replies starting 2026-09-01. Draft customer emails that used to run three or four
sentences now run two or three paragraphs and read as informal. A check of the platform
activity log shows the model version changed on 2026-08-31. Sampling 50 recent replies
against the team's tone standard, 18 fail. The workflow's Business Quality Score has moved
from 86 to 68. About 200 customer emails per week are drafted through this assistant. The
grounding content and the system prompt have not been changed.

## Incident 3

A customer-facing support bot returned another customer's account balance and last four
payment-card digits in a reply. It was noticed when the customer who received the
information forwarded the transcript to a support agent asking why someone else's details
were in their chat. It is not yet known how many other sessions were affected or whether
the exposure is ongoing. The bot draws on a shared account-lookup connection.

## Incident 4

A finance assistant was asked whether a client entertainment expense is tax-deductible. It
answered with a confident, specific figure — "50% deductible under current rules" — and
named a filing treatment. The rate it gave is wrong for this expense category, and an
employee has already used the answer to code three expense reports. The underlying tax
guidance document in the assistant's sources is outdated. An employee acting on this answer
could misstate a filing.

## Incident 5

An internal engineering assistant times out for roughly 20 minutes most mornings around
9:00. Users get a spinner and then an error, wait, and retry successfully later. It has
happened on and off for about three weeks. No one has quantified how many requests are
lost or what work is delayed. The behavior is already known to the people who run the
platform, and it recurs on a predictable schedule. There is no data yet on business
impact.
