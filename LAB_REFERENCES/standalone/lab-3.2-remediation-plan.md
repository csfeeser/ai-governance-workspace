# The Remediation Plan

## Objectives

In this lab, you will turn a reviewer-quality finding into a remediation plan with a dated, measurable test of whether the fix worked.

Most remediation plans name a problem and an intention and stop there, which leaves no way to tell later whether anything improved. In this lab you take the finding from Lab 3.1, about a reviewer whose approvals are not getting an independent check, and build the plan one decision at a time: how to state the finding, the corrective action, a temporary safeguard, and (the part that is usually missing) a re-check date, a measurable target, and where the re-check's number will come from. The owner was decided at the end of Lab 3.1. The plan you produce is one of the six components of the Module 5 evidence packet.

By the end of this lab you will be able to write a remediation plan an auditor would accept: state a finding as a checkable gap in a process, not a personal failing; choose the corrective action that fixes that gap, and a safeguard for the meantime; set a re-check date from the workflow's review cadence; and tell a measurable target from a vague one, with the evidence that will measure it.

## Background (Why This Matters)

```text
Finding (from Lab 3.1)
       │
       ▼
State it as a process gap, with numbers
       │
       ▼
Corrective action + interim safeguard
       │
       ▼
Verification: re-check date, measurable target, evidence source
```

A plan that only says "we will do better" is worth nothing, because nobody can tell later whether it worked. A good plan says who will do what, by when, and what number will show that it worked. That last part, verification, is what auditors look for and what most remediation plans leave out.

**Words you will see in this lab**
- **Finding:** a problem that has been discovered and written down.
- **Remediation plan:** a plan to fix a problem. "Remediate" means "fix".
- **Owner:** the person or team responsible for getting the job done. You name them by their job, for example "the team that runs the reviewers", and not by a person's name.
- **Interim safeguard:** a temporary protection that stays in place until the real fix is finished.
- **Measurable target:** a number that shows whether the fix worked. For example, "R-A's rate is back within 5 points of the team average".
- **Auditor:** a person whose job is to check that a company really did what it says it did.

## Procedure

1. **Choose how to state the finding.** In Lab 3.1 you found that reviewer R-A almost never disagrees with PolicyPal, and you decided the fix belongs to the function that runs the human review process. Now you write the plan for fixing it, called a remediation plan.

    The plan goes to the manager who runs the review process and into PolicyPal's records, and it is one of the six papers an auditor checks in Module 5. A plan only counts if someone reading it a month from now can say plainly whether the fix worked.

    #### Reviewer-Quality Finding: R-A

    Reviewer R-A shows a 30-day override rate of 2% (1 of 42 review decisions) against a team average of 18%. R-A overrode nothing at all in four of the five case types, even though most of the other reviewers overrode some cases of those same types (R-B, for example, overrode 5 of 10 conduct cases), and R-A's rate was zero in three of the four weeks. The one exception is a single `pto` override in W3. In 27 of R-A's 28 approvals, another reviewer overrode a case of the same type in the same week. This pattern is consistent with rubber-stamping (approving the AI's decision without independent review), but 30 days of one reviewer's decisions is not enough to be certain, and an unusually clean queue, while less likely here, is a real alternative. Recommend a second-review sample of R-A's recent approvals to confirm the pattern, followed by remediation with a dated, measurable re-check if it holds.

    Read the finding above, then choose the statement that should open the plan. A good finding describes a gap in how the work is done, not a fault in a person, and includes the numbers, so it can be checked.

    ***Which statement should open the plan?***

    - Reviewer R-A is not doing the job properly and should be replaced: R-A's override rate is 2% against a team average of 18%, near zero in every week and case type.
    - Approvals from reviewer R-A are not getting an independent check: R-A's override rate is 2% against a team average of 18%, near zero in every week and case type.
    - PolicyPal proposes decisions that are too easy to approve: R-A agrees with 98% of its proposals against a team average of 82%, in every week and case type.
    - Reviewer R-A needs to take more care with flagged cases: R-A agrees with PolicyPal far more often than the other reviewers do, in most weeks and case types.

    <details><summary>Show the answer</summary>

    The second one: `Approvals from reviewer R-A are not getting an independent check...`. It names a gap in the process and gives numbers anyone can check.

    - The first has the same numbers, but it blames a person and jumps to a punishment. That is neither fair nor something a plan can fix.
    - The third blames PolicyPal. Lab 3.1 showed the other reviewers override the same kinds of proposal, so the AI is not the difference.
    - The fourth blames a person too, and has no numbers, so no one could check it later.

    </details>

0. **Choose what to do about it.** The first thing the plan does is check that the worry is real: a second reviewer re-marks a sample of R-A's recent approvals. If the pattern holds, one corrective action follows.

    #### The four actions

    | Action | What it changes |
    |---|---|
    | Targeted re-training on the review standard | R-A is taught the review standard again |
    | Ongoing second-review sampling | Each month, a second reviewer re-checks a sample of every reviewer's decisions |
    | Workload rebalancing | R-A is given fewer cases to review |
    | Reassignment | R-A moves to other work, and another reviewer takes over R-A's cases |

    #### Facts about R-A and how reviewing works today

    | Fact | |
    |---|---|
    | Training | R-A completed the review-standard training in March 2026 and passed, like the other four reviewers |
    | Workload | R-A reviewed 42 cases in the 30 days, the same as R-B, R-C and R-E (R-D reviewed 44) |
    | Checks on reviewers | Nobody re-checks any reviewer's decisions: each reviewer's call is final |
    | Experience | R-A has reviewed PolicyPal cases since it launched in March 2026 |

    Use the facts to rule out the actions that would not fix your finding, then choose the one that would.

    ***Corrective action.***

    - Targeted re-training on the review standard
    - Ongoing second-review sampling
    - Workload rebalancing
    - Reassignment

    <details><summary>Show the answer</summary>

    `Ongoing second-review sampling`. The finding is that R-A's approvals are not getting an independent check, and the facts show that nobody re-checks any reviewer today. Sampling adds exactly that check, for every reviewer.

    - Re-training: R-A already passed the training, like everyone else.
    - Workload rebalancing: R-A's workload is the same as the others'.
    - Reassignment: it removes R-A, but every reviewer's decisions would still go unchecked.

    </details>

0. **Add a temporary protection.** The real fix takes weeks to put in place. Until then, R-A's approvals are still going out without an independent check. An interim safeguard is a temporary protection that covers that gap until the fix is working.

    ***Interim safeguard.***

    - A second reviewer checks every one of R-A's approvals until the new sampling is running
    - R-A is asked to take extra care with every approval until the new sampling is running
    - PolicyPal is switched off for all employees until the new sampling is running
    - Nothing changes until the re-check date, when the new numbers are reviewed

    <details><summary>Show the answer</summary>

    `A second reviewer checks every one of R-A's approvals`. It closes the gap straight away, and only for the approvals at risk. Asking R-A for extra care adds no independent check. Switching PolicyPal off takes it away from 1,900 employees because of one reviewer's pattern. Changing nothing leaves the gap open for a month.

    </details>

0. **Choose when you will check again.** Without a re-check date, "we will check later" never happens. The date comes from how often PolicyPal must be reviewed, which depends on its risk tier.

    #### PolicyPal facts

    | Fact | |
    |---|---|
    | Deployed | 2026-03-02 |
    | Monthly active users | About 1,900 |
    | Assigned risk tier | Medium |
    | Reviewer pool | 5 HR operations reviewers |
    | Reviewer log export used in Lab 3.1 | 30 days, 19 May to 17 June |
    | Quality review in Lab 3.1 | April to June (one quarter) |

    #### Review cadence by risk tier

    | Risk tier | Review cadence | Baseline sample size |
    |---|---|---|
    | Low | Quarterly | 10 responses |
    | Medium | Monthly | 20 responses |
    | High | Weekly | 30 responses |

    ***When should the plan say the fix will be checked?***

    - One week after the plan starts
    - One month after the plan starts
    - One quarter (three months) after the plan starts
    - Whenever the review team has time

    <details><summary>Show the answer</summary>

    `One month after the plan starts`. PolicyPal's risk tier is Medium, and the chart says Medium-risk tools are reviewed monthly, so the re-check lines up with the next regular review. The 30-day log and the quarterly quality review are about past checks, not how often PolicyPal must be reviewed. "Whenever the review team has time" is not a date, and never happens.

    </details>

0. **Choose the number that will mean it worked.** "Improved" is not a number. The target must let someone who was not here look at the result and say plainly "yes, it worked" or "no, it did not."

    | From the finding | |
    |---|---|
    | R-A's override rate | 2% (1 of 42 decisions) |
    | Team average override rate | 18% |
    | Weeks with a zero rate for R-A | 3 of 4 |

    ***Measurable target.***

    - R-A's reviewing is clearly more careful and thorough, as judged by R-A's manager over a two-week period
    - R-A's override rate is back within 5 points of the team average, measured over a two-week sample of decisions
    - R-A's override rate goes up from 2%, measured over a two-week sample of R-A's decisions
    - No employee complaints about R-A's decisions are received during a two-week period

    <details><summary>Show the answer</summary>

    `Within 5 points of the team average, over a two-week sample`. It is a number with a clear pass line, measured over a stated period, so anyone can check it.

    - "More careful and thorough" is an opinion, not a number.
    - "Goes up from 2%" has no line to pass: 3% would count as success.
    - Employees never see the reviews, so they would not complain either way.

    </details>

0. **Choose where the number will come from.** A target is only useful if you know where its number will come from.

    | Source | What it records |
    |---|---|
    | The reviewer log | Every flagged case: what PolicyPal proposed, what the reviewer decided, and who the reviewer was |
    | PolicyPal's activity log | Every time PolicyPal was used: who, when, which AI model, and which documents it read |
    | R-A's manager | Their view of how R-A is doing |
    | Employee complaints | Problems employees report with PolicyPal's answers |

    Choose the data you will look at on the re-check date.

    ***Evidence for the re-check.***

    - A fresh export of the reviewer log, covering the two weeks before the re-check date
    - PolicyPal's activity log, covering the two weeks before the re-check date
    - A written view from R-A's manager on how R-A has done since the plan started
    - The employee complaints about PolicyPal received since the plan started

    <details><summary>Show the answer</summary>

    `A fresh export of the reviewer log`. It is the same list you measured R-A's override rate from in Lab 3.1, so the before and after numbers compare like with like. The activity log records PolicyPal's use and model, not reviewers' decisions. An opinion is not a number, and employees never see the reviews.

    </details>

## Conclusion

In this lab you turned a reviewer-quality finding into a plan that states the finding as a checkable process gap, names the corrective action and a safeguard for the meantime, and sets a dated, measurable test of whether it worked, with the evidence that will prove it. That last part is what auditors look for and what most remediation plans lack.
