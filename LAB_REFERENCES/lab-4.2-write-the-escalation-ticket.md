# Write the Escalation Ticket

## Lab Objective

**Write an escalation ticket that gives a responsible owner everything they need to act, and pressure-test it from the receiver's side.**

Escalations fail in practice by describing a feeling instead of a frequency. "The assistant seems worse" is not a ticket. In this lab you take a fully triaged incident and write the handoff a responsible owner actually needs: what was observed, how often, over what period, what evidence is attached, what it is costing the business, and the specific action you are asking for. Then you check it from the receiver's point of view.

In this lab, you will:
- Convert a triaged incident into an escalation ticket
- State observations as behavior and frequency, not impression
- Name the evidence and what you have already ruled out
- Set a response-by expectation aligned to urgency
- Test the ticket from the receiving owner's perspective

By the end of this lab you will be able to write an escalation an owner can act on without coming back to you with questions.

## In Plain Words

- **What you are doing:** A problem has already been sorted for you, and you know who has to fix it. Now you write them a message that tells them what is wrong and what you need from them.
- **Why it matters:** If your message is vague, the other person has to come back with questions, and the fix is delayed. A good message means they can start work straight away.
- **You do not have to:** download anything, open a spreadsheet, or make anything up. Every fact you need is on the first tab, and everything you type saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

**Words you will see in this lab**
- **Ticket:** a written request that asks someone to fix something. It has fixed parts, so nothing is left out.
- **Escalation:** passing a problem to the person who can fix it.
- **Evidence:** the proof behind what you are saying, such as a count, a date, or a record.
- **Ruled out:** checked and found not to be the cause. Saying what you have ruled out saves the other person from checking it again.
- **The ask:** the one clear thing you want the other person to do.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `4.2 Write the Escalation Ticket` in the left sidebar.

## Procedure

1. **Read the problem and the facts.** Everything you need for the ticket is already on this page. Your job is only to turn it into a clear message.
    - Click the tab called `Triaged Incident`. It is probably already open.
    - Read it from top to bottom.
    - Notice the three parts: the **Triage result**, the **Supporting facts**, and the **Evidence available**.

0. **Say what the problem is and who it goes to.** The first thing a person needs is what this is about and why they are getting it.
    - Click the `Escalation Ticket` tab.
    - In the section **Incident, category, and routed to**, write what the problem is, its category, and who is responsible for it.
    - Copy these from the **Triage result** table on the `Triaged Incident` tab.
    - Name the owner by the job they do, not by a department.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "______ assistant, category ______, routed to the team responsible for ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Sales-support assistant (Claude), category Technical / vendor, routed to the team responsible for the platform and the vendor relationship for this assistant."

    </details>

0. **Say what is happening.** Say what anyone could see for themselves. "It seems worse" is a feeling. "The replies are 40% longer" is something anyone can check.
    - In the section **What was observed**, describe what the assistant is doing.
    - Use the **Supporting facts** on the `Triaged Incident` tab.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Since ______, draft replies are roughly ______% longer than before and have shifted ______ in tone."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Since 2026-08-12, draft replies are roughly 40% longer than before and have shifted off-tone (informal and verbose)." Anyone could check this. "The assistant seems worse" is only a feeling.

    </details>

0. **Say how often, and since when.** Numbers turn "it happens a lot" into something a person can judge for themselves.
    - In the section **How often, and over what period**, write how many, out of how many, and since when.
    - The numbers are in the **Supporting facts**.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "______ of ______ sampled replies fail the tone standard (______%), since ______, about ______ weeks."

    </details>

    <details><summary>ANSWER:</summary>

    18 of 50 sampled replies fail the tone standard (36%), since 2026-08-12, about three weeks at the time of writing.

    </details>

0. **List your proof.** A claim with no proof is easy to dismiss. Say what evidence you have, and what each piece shows.
    - In the section **Evidence attached**, list each piece of evidence and say what it shows.
    - Look at **Evidence available** on the `Triaged Incident` tab. The page already summarises each one, so there is nothing else to open.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "1. The scored sample of ______ replies, showing ______. 2. The activity-log excerpt, showing ______ on ______. 3. The ______ standard used to score the sample."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "1. The scored sample of 50 replies, showing 18 fail the tone standard. 2. The activity-log excerpt, showing the model identity changed on 2026-08-11. 3. The tone standard used to score the sample."

    </details>

0. **Say what you have already checked.** This saves the other person from repeating your work.
    - In the section **Already ruled out**, write what you have already checked and found was not the cause.
    - The list is in the **Supporting facts**.

    <details><summary>ANSWER:</summary>

    The material the assistant reads from is unchanged, the instructions given to it are unchanged, and the way users phrase their questions is unchanged.

    </details>

0. **Say what it is costing.** A problem gets fixed faster when people can see what it costs.
    - In the section **Business impact**, write what this is costing the business. Use numbers if you can.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "About ______ customer-facing ______ per week are drafted in the wrong ______, which is a ______ risk."

    </details>

    <details><summary>ANSWER:</summary>

    About 200 customer-facing emails per week are drafted in the wrong tone, which is a risk to the brand and to consistency.

    </details>

0. **Say exactly what you want them to do.** This is the most important part. If you only say "please look into this", nothing specific will happen.
    - In the section **The ask**, write the one specific thing you want the owner to do.
    - Think about this: the AI model changed the day before the problem started. What could the team that runs the platform do about a model version?

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Confirm whether the ______ can be ______, and advise a ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Confirm whether the model version can be pinned or rolled back, and advise a timeline."

    </details>

0. **Say when you need an answer.** People fit work around deadlines. If you do not give one, yours will be last in the queue.
    - In the section **Response-by**, say when you need a reply.
    - Match it to how urgent this is. It is serious and it is still going on, and it is customer-facing, but it is not private data being shown.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Initial response within ______ business days; this is ______ and ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Initial response within 3 business days; this is customer-facing and ongoing."

    </details>

0. **Read your ticket as the person receiving it.** You know everything about this problem, so it is easy to leave out things that seem obvious to you. The person receiving it knows nothing.
    - Scroll back through the whole `Escalation Ticket` tab.
    - Pretend you have never seen this problem before.
    - Ask: could I start work from this message alone, without asking any questions?
    - If not, find the gap and fix it by typing in that box.

0. **Check that you have finished.** The workspace keeps count of the boxes you have filled in.
    - Look at the top right of the workspace. It says something like `X of Y answers filled in`.
    - When X is the same as Y, you are done.
    - Your answers save automatically as you type, so there is nothing to save or send.
    - A ticket like this is one of the papers that go in the evidence packet in Module 5.
    - If you would like a copy for yourself, click the `Save as PDF` button on the `Escalation Ticket` tab.

## Challenges

This is optional. Your answers to it are saved on the `Bronze: Second Ticket` tab.

**🥉 Bronze:** Click the `Bronze: Second Incident` tab. This is a more serious problem: private customer information was shown to the wrong person. Then write the ticket for it on the `Bronze: Second Ticket` tab. What you ask for and when you need it will be very different from the first ticket, because this one is urgent. The form is the same.

## Conclusion

In this lab you wrote an escalation ticket that gives the responsible owner the observation, frequency, period, evidence, impact, and a specific ask, and you pressure-tested it from the receiver's side. That ticket is also a line in the audit packet's incident history.
