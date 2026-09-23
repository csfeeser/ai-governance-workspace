# Triage and Route Five Incidents

## Lab Objective

**Classify five AI workflow incidents by category and route each one to a responsible owner named by responsibility, not by department.**

You cannot fix everything an AI workflow throws at you, and trying to is its own failure. The first move is always triage: what kind of incident is this, who is responsible for the affected thing, and does it even meet the bar to escalate right now. In this lab you work five realistic incidents, including one that is genuinely ambiguous between two categories and one where the right answer may be "monitor, do not escalate yet."

In this lab, you will:
- Assign each incident one of the five incident categories
- Route each incident to a responsible owner named by responsibility rather than by org-chart title
- Resolve an incident that fits two categories by deciding which risk matters more
- Decide whether a low-signal incident meets the bar to escalate now
- Decide the next move when a route stalls or ownership is disputed
- Produce a five-row triage of your own

By the end of this lab you will be able to triage an AI incident into a category and a route in a few minutes.

## In Plain Words

- **What you are doing:** Five different things have gone wrong with AI tools. For each one you will decide what kind of problem it is, who should deal with it, and how quickly.
- **Why it matters:** You cannot fix everything yourself, and you should not try. The skill is to quickly get each problem to the right person. Getting it wrong wastes time, or leaves a serious problem sitting.
- **You do not have to:** download anything, open a spreadsheet, or write long answers. Nearly everything is a drop-down menu, and everything you pick saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

**Words you will see in this lab**
- **Incident:** something that went wrong.
- **Triage:** sorting problems by type and urgency, the way nurses sort patients in an emergency room.
- **Escalate:** pass a problem to someone who has the power to fix it.
- **Owner by responsibility:** you name the job that is responsible, for example "the team that owns the policy documents", and you do not name a department, because departments do not tell you who actually does the work.
- **The five categories:**
  - **Business rule:** the AI broke a rule the business set for it.
  - **Business content:** the material the AI reads from is wrong, missing, or out of date.
  - **Security or privacy:** private data was shown, leaked, or misused.
  - **Technical or vendor:** the computer system, the AI model, the connections, or the speed.
  - **Risk or compliance:** the company could get into legal, regulatory, or money trouble.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `4.1 Triage and Route Five Incidents` in the left sidebar.

## Procedure

1. **Read all five incidents before you sort any.** Some of them only make sense once you have read the others, so do not start sorting straight away.
    - Click the tab called `Incident Log`. It is probably already open.
    - Read all five incidents from top to bottom.

0. **Sort incident 1.** Now sort the first problem. You pick the type of problem, the person responsible, and what to do.
    - Click the `My Triage` tab.
    - In the section **Incident 1**, use the three drop-downs to pick the **Category**, the **Responsible owner**, and the **Action**.
    - Pick the owner that names a job, for example "the team that ...". Do not pick one that is only a department.

    <details><summary>ANSWER:</summary>

    - Category: `Business content`. The AI faithfully repeated an out-of-date policy document, so the fix is to remove the old document from where the AI reads, not to change the AI.
    - Owner: `The team that owns the HR policy library`. This names a responsibility, not a department.
    - Action: `Escalate now`.

    </details>

0. **Sort incident 2.**
    - In the section **Incident 2**, pick the **Category**, the **Responsible owner**, and the **Action**.

    <details><summary>ANSWER:</summary>

    - Category: `Technical or vendor`. The AI model version changed and the output changed with it.
    - Owner: `The team responsible for the platform and the vendor relationship`.
    - Action: `Escalate now`.

    </details>

0. **Sort incident 3, and pay attention to urgency.** Anything to do with private data being shown to the wrong person is urgent. It cannot wait for the next monthly review.
    - In the section **Incident 3**, pick the **Category**, the **Responsible owner**, and the **Action**.

    <details><summary>ANSWER:</summary>

    - Category: `Security or privacy`. Another customer's private data was shown.
    - Owner: `The information-security function, with the legal function notified`.
    - Action: `Escalate immediately`.

    </details>

0. **Notice that incident 4 fits two categories.** Real problems do not always fit one box. Here you pick the two boxes that fit, and in the next step you decide which one matters more.
    - In the section **Incident 4**, use the two category drop-downs to pick the two categories that fit.
    - It does not matter which drop-down each one goes in for now.

    <details><summary>ANSWER:</summary>

    It is `Business content` (the tax document that the AI reads from is out of date). It is also `Risk or compliance` (the AI gave a confident, specific, wrong answer about tax that someone could act on).

    </details>

0. **Decide which of the two matters more, and why.** When a problem fits two categories, you handle the worse risk first. The other one can be mentioned later.
    - In the section **Incident 4**, check that **The category that matters more** shows the one you decided on. If it is the wrong way round, swap the two drop-downs.
    - Pick the **Responsible owner** and the **Action**.
    - In the last box, write one line saying why that risk is the bigger one.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Someone acting on ______ could ______, which is a larger harm than ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Someone acting on wrong tax advice could misstate a filing, which is a larger harm than an outdated document sitting in the source."

    </details>

    <details><summary>ANSWER:</summary>

    - Category that matters more: `Risk or compliance`. Someone acting on wrong tax advice is the bigger harm.
    - Owner: `The risk and compliance function`. You may also tell the owner of the documents, but the escalation goes to risk and compliance.

    </details>

0. **Sort incident 5.** This one is not as urgent as it may sound. Not every problem needs to be escalated straight away.
    - In the section **Incident 5**, pick the **Category**, the **Responsible owner**, and the **Action**.

    <details><summary>ANSWER:</summary>

    - Category: `Technical or vendor`. A slow-down that repeats every morning.
    - Owner: `The team responsible for the affected technology`.
    - Action: `Monitor and log, do not escalate yet`.

    </details>

0. **Say what would make you escalate incident 5.** "Monitor" does not mean "ignore". It means you have decided in advance what would make it serious enough to escalate.
    - In the section **Incident 5**, in the last box, write one line about what would have to change for you to escalate it now.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "I would escalate if ______ were quantified as ______, or if it started happening ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "I would escalate if the lost requests were quantified as affecting real work, or if it started happening at other times of day."

    </details>

    <details><summary>ANSWER:</summary>

    It is a "monitor and log" item, not an escalation yet. It comes and goes, the tech team already knows about it, and nobody has worked out what it costs. Escalate it if numbers show that it is happening more often or costing more.

    </details>

0. **Decide what you would do if the message goes nowhere.** Passing a problem on is not the same as solving it. Often the person does not answer, says it is not their job, or nobody owns the thing at all.
    - In the section **If the route stalls**, use the drop-down to pick your first move.

    <details><summary>ANSWER:</summary>

    Send it to whoever is responsible by their job, take a problem nobody owns to the risk and compliance team, go to the owner's manager, or write down the gap and set a follow-up date. All of those are sensible. Waiting for the next monthly review is not. A problem that nobody will act on is a finding in its own right.

    </details>

0. **Check that none of your owners is just a department.** A department name does not tell you who will do the work.
    - Go back through your five **Responsible owner** choices.
    - If any of them is only a department (for example "The IT department"), change it to the choice that names a job.

0. **Pick the one problem you would deal with first.** With five problems you cannot fix everything at once, so you need a way to choose.
    - In the section **Escalate first**, use the drop-down to pick the incident.
    - In the box below it, write one line saying why. Think about how bad it is and how urgent it is.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Because ______ has the highest ______ and the highest ______."

    </details>

    <details><summary>ANSWER:</summary>

    Incident 3. Private data is being shown right now and nobody knows how far it has spread. It is both the most urgent and the most serious.

    </details>

0. **Check that you have finished.** The workspace keeps count of the boxes you have filled in.
    - Look at the top right of the workspace. It says something like `X of Y answers filled in`.
    - When X is the same as Y, you are done.
    - Your answers save automatically as you pick them, so there is nothing to save or send.
    - If you would like a copy for yourself, click the `Save as PDF` button on the `My Triage` tab.

## Conclusion

In this lab you triaged five AI incidents into categories, routed each to a responsible owner by responsibility rather than by department, resolved an ambiguous case by deciding which risk mattered more, separated an escalation from a monitor-and-log item, and decided in advance what to do when a handoff stalls. Triage is the first thing you do with any finding an AI workflow produces, and routing a finding is not the same as closing it.
