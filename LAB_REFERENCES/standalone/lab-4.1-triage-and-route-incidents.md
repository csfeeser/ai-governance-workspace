# Triage and Route Five Incidents

## Objectives

In this lab, you will classify five AI workflow incidents by category and route each one to a responsible owner named by responsibility, not by department.

Your company runs several AI tools, and this week you are on the triage rota for the company's AI incident queue. You cannot fix everything an AI workflow throws at you, and trying to is its own failure. The first move is always triage: what kind of incident is this, who is responsible for the affected thing, and does it even meet the bar to escalate right now. In this lab you work five realistic incidents, including one that is genuinely ambiguous between two categories and one where the right answer may be "monitor, do not escalate yet."

By the end of this lab you will be able to triage an AI incident into a category and a route in a few minutes: assign each incident one of the five incident categories, route it to a responsible owner named by responsibility rather than by org-chart title, resolve an incident that fits two categories by deciding which risk matters more, decide whether a low-signal incident needs escalating yet, and decide the next move when an owner does not respond.

## Background (Why This Matters)

```text
Incident reported
       │
       ▼
Category: what kind of problem is it?
       │
       ▼
Responsible owner: who runs the thing that went wrong?
       │
       ▼
Action: how quickly?
```

You cannot fix everything yourself, and you should not try. The skill is to quickly get each problem to the right person. Getting it wrong wastes time, or leaves a serious problem sitting. Triage means sorting problems by type and urgency, the way nurses sort patients in an emergency room. You are not fixing anything; you are getting each problem to the person who can fix it, at the right speed.

**Words you will see in this lab**
- **Incident:** something that went wrong.
- **Triage:** sorting problems by type and urgency, the way nurses sort patients in an emergency room.
- **Escalate:** pass a problem to someone who has the power to fix it.
- **Owner by responsibility:** you name the job that is responsible, for example "the team that owns the policy documents," and you do not name a department, because departments do not tell you who actually does the work.
- **The five categories:**
  - **Business rule:** the AI broke a rule the business set for it.
  - **Business content:** the material the AI reads from is wrong, missing, or out of date.
  - **Security or privacy:** private data was shown, leaked, or misused.
  - **Technical or vendor:** the computer system, the AI model, the connections, or the speed.
  - **Risk or compliance:** the company could get into legal, regulatory, or money trouble.

## Procedure

1. **Sort incident 1.** Each week, one Business AI Owner is on the triage rota: they sort every new report and send it to the right owner. This week it is you, and five incidents have come in.

    For each incident you choose three things: the category (what kind of problem it is), the responsible owner (who should deal with it — route by responsibility, sending it to whoever runs the thing that went wrong, not to a department that will have to pass it on), and the action (how quickly).

    #### Incident 1

    PolicyPal, the HR policy assistant, has been answering some PTO carryover questions using "PTO Policy 2023." The current policy is "PTO Policy 2026," effective 2026-09-01; the 2023 document is still present in the grounding source. Over the past two weeks at least nine employees were told the carryover cap is 10 days. The current cap is 3 days. Two employees have already submitted year-end plans based on the wrong figure. The assistant's wording and behavior are otherwise unchanged, and it cites the 2023 document by name when asked.

    #### Who is responsible for what

    | Owner | What they are responsible for |
    |---|---|
    | The team that owns the HR policy library | The HR policy documents the HR assistant reads from |
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The information-security function, with the legal function notified | Leaks and misuse of private or confidential data |
    | The risk and compliance function | Legal, regulatory, tax and financial risk to the company |
    | The IT, HR or legal department | A whole department. Someone there has to work out who should deal with it, which costs time. |

    ***Category.***

    - Business rule: the AI broke a rule the business set for it
    - Business content: what the AI reads from is wrong, missing, or out of date
    - Security or privacy: private data was shown, leaked, or misused
    - Technical or vendor: the computer system, the AI model, the connections, or speed
    - Risk or compliance: the company could get into legal, regulatory, or money trouble

    ***Responsible owner.***

    - The team that owns the HR policy library
    - The IT department, which will pass it to the right team
    - The team responsible for the platform and the vendor relationship
    - The HR department, which will pass it to the right team
    - The information-security function, with the legal function notified
    - The legal department, which will pass it to the right team
    - The risk and compliance function

    ***Action.***

    - Escalate immediately: data is exposed or harm is spreading right now; act today
    - Escalate soon: a real error or harm to fix; raise it this week, not at the monthly review
    - Monitor and log: a known problem with no measured harm yet; watch it for now

    <details><summary>Show the answer</summary>

    - Category: `Business content`. PolicyPal faithfully repeated an out-of-date policy document, so the fix is to remove the old document from what it reads, not to change the AI.
    - Owner: `The team that owns the HR policy library`. They own the documents.
    - Action: `Escalate soon`. Employees are getting a wrong figure and two have already acted on it, but no private data is exposed.

    </details>

0. **Sort incident 2.**

    #### Incident 2

    A sales-support assistant built on Claude began producing noticeably longer, off-tone replies starting 2026-09-01. Draft customer emails that used to run three or four sentences now run two or three paragraphs and read as informal. A check of the platform activity log shows the model version changed on 2026-08-31. Sampling 50 recent replies against the team's tone standard, 18 fail. The workflow's Business Quality Score has moved from 86 to 68. About 200 customer emails per week are drafted through this assistant. The grounding content and the system prompt have not been changed.

    #### Who is responsible for what

    | Owner | What they are responsible for |
    |---|---|
    | The team that owns the HR policy library | The HR policy documents the HR assistant reads from |
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The information-security function, with the legal function notified | Leaks and misuse of private or confidential data |
    | The risk and compliance function | Legal, regulatory, tax and financial risk to the company |
    | The IT, HR or legal department | A whole department. Someone there has to work out who should deal with it, which costs time. |

    ***Category, responsible owner, and action for incident 2.***

    <details><summary>Show the answer</summary>

    - Category: `Technical or vendor`. The AI model version changed and the output changed with it.
    - Owner: `The team responsible for the platform and the vendor relationship`. They run the model and the vendor contract.
    - Action: `Escalate soon`. About 200 customer emails a week are affected, but nothing private is exposed.

    </details>

0. **Sort incident 3.**

    #### Incident 3

    A customer-facing support bot returned another customer's account balance and last four payment-card digits in a reply. It was noticed when the customer who received the information forwarded the transcript to a support agent asking why someone else's details were in their chat. It is not yet known how many other sessions were affected or whether the exposure is ongoing. The bot draws on a shared account-lookup connection.

    #### Who is responsible for what

    | Owner | What they are responsible for |
    |---|---|
    | The team that owns the HR policy library | The HR policy documents the HR assistant reads from |
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The information-security function, with the legal function notified | Leaks and misuse of private or confidential data |
    | The risk and compliance function | Legal, regulatory, tax and financial risk to the company |
    | The IT, HR or legal department | A whole department. Someone there has to work out who should deal with it, which costs time. |

    ***Category, responsible owner, and action for incident 3.***

    <details><summary>Show the answer</summary>

    - Category: `Security or privacy`. Another customer's private data was shown.
    - Owner: `The information-security function, with the legal function notified`. A data exposure may have legal reporting duties, so legal must know too.
    - Action: `Escalate immediately`. Nobody knows how many sessions were affected or whether it is still happening.

    </details>

0. **Sort incident 4, which fits two categories.** Real problems do not always fit one box. Incident 4 fits two categories. When that happens, you handle the bigger risk first.

    #### Incident 4

    A finance assistant was asked whether a client entertainment expense is tax-deductible. It answered with a confident, specific figure ("50% deductible under current rules"), and named a filing treatment. The rate it gave is wrong for this expense category, and an employee has already used the answer to code three expense reports. The underlying tax guidance document in the assistant's sources is outdated. An employee acting on this answer could misstate a filing.

    #### Who is responsible for what

    | Owner | What they are responsible for |
    |---|---|
    | The team that owns the HR policy library | The HR policy documents the HR assistant reads from |
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The information-security function, with the legal function notified | Leaks and misuse of private or confidential data |
    | The risk and compliance function | Legal, regulatory, tax and financial risk to the company |
    | The IT, HR or legal department | A whole department. Someone there has to work out who should deal with it, which costs time. |

    Decide which two categories fit. Put the one that matters more first, and the other second. Choose the responsible owner and the action. Then write one line saying why that risk is the bigger one.

    ***The category that matters more.***

    ***The other category that also fits.***

    ***Responsible owner.***

    ***Action.***

    ***One line: why does that risk matter more?***

    <details><summary>Hint: where to look</summary>

    Look at the two categories you chose. Which one involves a real person being harmed or the company facing money or legal trouble? That is the bigger risk.

    </details>

    <details><summary>Show the answer</summary>

    - The category that matters more: `Risk or compliance`. The assistant gave a confident, wrong tax answer that someone has already acted on, and could lead to a misstated filing.
    - The other category: `Business content`. The tax guidance document the assistant reads from is out of date.
    - Owner: `The risk and compliance function`. You may also tell whoever owns the tax document, but the escalation goes to risk and compliance.
    - Action: `Escalate soon`.
    - Why: "Someone acting on wrong tax advice could misstate a filing, which is a bigger harm than an outdated document sitting in the source."

    </details>

0. **Sort incident 5.**

    #### Incident 5

    An internal engineering assistant times out for roughly 20 minutes most mornings around 9:00. Users get a spinner and then an error, wait, and retry successfully later. It has happened on and off for about three weeks. No one has quantified how many requests are lost or what work is delayed. The behavior is already known to the people who run the platform, and it recurs on a predictable schedule. There is no data yet on business impact.

    #### Who is responsible for what

    | Owner | What they are responsible for |
    |---|---|
    | The team that owns the HR policy library | The HR policy documents the HR assistant reads from |
    | The team responsible for the platform and the vendor relationship | The AI tools' technology: the models, the software, speed and uptime, and the contracts with the AI vendors |
    | The information-security function, with the legal function notified | Leaks and misuse of private or confidential data |
    | The risk and compliance function | Legal, regulatory, tax and financial risk to the company |
    | The IT, HR or legal department | A whole department. Someone there has to work out who should deal with it, which costs time. |

    Choose the category, the responsible owner, and the action for incident 5. Then say what would have to change for this incident to need escalating now.

    ***Category, responsible owner, and action for incident 5.***

    ***What would have to change for this to need escalating now?***

    <details><summary>Hint: where to look</summary>

    The incident says "nobody has quantified how many requests are lost or what work is delayed." If someone measured that, what would make it urgent? Also, when does it happen now, and when would it be worse?

    </details>

    <details><summary>Show the answer</summary>

    - Category: `Technical or vendor`. A slow-down that repeats every morning.
    - Owner: `The team responsible for the platform and the vendor relationship`. They run the platform, and they already know about it.
    - Action: `Monitor and log`. It comes and goes, the platform team knows about it, and nobody has measured what it costs.
    - What would change it: "I would escalate if the lost requests were measured as holding up real work, or if it started happening at other times of day."

    </details>

0. **Pick the one incident you would deal with first.** With five problems you cannot fix everything at once, so you need a way to choose. Think about how much harm each one does and how urgent it is.

    Look back at your triage for each incident: the action (Escalate immediately, soon, or monitor) and the category it falls under.

    ***The one incident you would escalate first.***

    - Incident 1
    - Incident 2
    - Incident 3
    - Incident 4
    - Incident 5

    ***One line: why? (harm combined with urgency)***

    <details><summary>Hint: where to look</summary>

    Which one combines the most urgent action with the highest-risk category?

    </details>

    <details><summary>Show the answer</summary>

    `Incident 3`. Private data is being shown right now and nobody knows how far it has spread. It is both the most harmful and the most urgent.

    </details>

0. **Decide what to do when the handoff stalls.** Passing a problem on is not the same as solving it. Here is what happened next with incident 2:

    > You sent incident 2 to the team responsible for the platform and the vendor relationship on Monday, asking for a reply within 3 business days. It is now the following Tuesday. There has been no reply, and the assistant is still drafting off-tone customer emails.

    ***What is your best next move?***

    - Wait for next month's review and raise the incident with the platform team again there
    - Escalate to the platform team's manager, attaching the ticket and the date that was missed
    - Change the sales assistant's settings yourself so the customer emails go back to normal
    - Re-send the same ticket to the IT department in case someone there can pick it up faster

    <details><summary>Show the answer</summary>

    `Escalate to the platform team's manager`, with the ticket and the date that was missed. The owner is right; they are just not responding, so you go one level up. Waiting a month leaves customers getting off-tone emails. Changing the settings yourself is not your job and bypasses the owner. Sending it to a department only adds another handoff.

    </details>

## Conclusion

In this lab you triaged five AI incidents into categories, routed each to a responsible owner by responsibility rather than by department, resolved an ambiguous case by deciding which risk mattered more, separated an escalation from a monitor-and-log item, and decided what to do when an owner does not respond. Triage is the first thing you do with any finding an AI workflow produces, and routing a finding is not the same as closing it.
