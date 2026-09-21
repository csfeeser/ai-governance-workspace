# Business Quality Standard — PolicyPal

*Supplied reference standard. This is a complete, strong instance of the standard a
Business AI Owner writes in Lab 1.1. Labs 2.1 and 2.2 score PolicyPal responses against
Section 3.*

## 1. Workflow and purpose

PolicyPal answers employee questions about company HR policy (PTO, benefits, expense,
travel, and conduct), grounded on the HR Policy Library in SharePoint.

## 2. Risk tier, review cadence, and sample size

Tier: **Medium**  ·  Review cadence: **Monthly**  ·  Baseline sample: **20 responses**

The tier was assigned by Risk & InfoSec with HR. The Business AI Owner reads it off the
intake record and applies the cadence and sample size (`ref-review-cadence.md`); they do
not assess or change the tier.

## 3. Scoring criteria

Each response is scored against all four criteria. A criterion is met (1) or not met (0).

- **c1 — Current, named source.** The response cites a specific policy document by name,
  and that document is the current version, not a superseded one and not an unnamed
  paraphrase.
- **c2 — Exact figure or entitlement.** Any number, rate, day count, or entitlement the
  response states matches what current policy says, word for word where policy is
  specific.
- **c3 — Answers the question asked.** The response gives the specific entitlement or
  answer the employee asked for, not a general summary, a restatement of the question, or
  a paraphrase of the policy's intent.
- **c4 — Human referral where required.** The response refers the employee to a named
  human contact for any question about an accommodation, a protected or statutory leave,
  or a decision the employee is disputing.

## 4. Business rules that must always hold

- Never state a dollar figure, day count, or entitlement that is not written in current
  policy.
- Always name the policy document the answer is based on, with its effective date.
- Never give legal advice or interpret statutory entitlements; route those to HR.

## 5. Errors that are unacceptable

- Inventing a policy or a policy provision that does not exist.
- Citing a superseded version of a policy as if it were current.
- Answering an accommodation or protected-leave question directly instead of referring it
  to a human.

## 6. When a human must intervene

- Any question about an accommodation or a protected or statutory leave.
- Any answer the employee disputes or pushes back on.
- Any question where current policy is silent or two policy documents conflict.

## 7. Tolerable inconsistency

Two employees who ask the same policy question must receive the same entitlement figure,
every time. Wording may vary; the entitlement may not.

## 8. Quality alarm level

Investigate the workflow when the Business Quality Score falls below **85**, or drops more
than **5 points** from the recorded baseline, whichever comes first. A movement inside
that band is logged and watched; a movement past it triggers a diagnosis (Lab 2.2). The
alarm level is set here, in advance, so that a later result is measured against it rather
than judged after the fact.
