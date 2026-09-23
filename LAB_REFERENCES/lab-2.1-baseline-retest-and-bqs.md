# Baseline Re-Test and Business Quality Score

## Lab Objective

**Score a fixed baseline set of AI responses against a written standard, read the Business Quality Score your scoring produces, and compare it to the recorded baseline to decide whether business quality has degraded.**

This is the periodic control test that turns "we monitor the AI" into evidence. You are handed two exports and first have to work out which one you can actually score. Then you score a 20-response sample against a supplied quality standard, read the single Business Quality Score that results, and compare it to the score the same responses received when the baseline was set. The result is a defensible, documented statement about whether PolicyPal is still doing a good job.

If you ask an administrator for "the audit log," on any platform, expect a spreadsheet of who-did-what-when, not the actual questions and answers. Microsoft Copilot's audit search and its eDiscovery collection are two different requests to two different tools; Claude Enterprise's "Export logs" and "Export Data" are two separate buttons on the same settings page, and only one of each pair has real content. Knowing which one to ask for is the first skill this lab tests.

In this lab, you will:
- Identify which of two platform exports contains scorable content
- Calibrate your scoring against a reference before the full run
- Score 20 responses against four pass/fail criteria
- Read the Business Quality Score your scoring produces
- Compare current scores to a recorded baseline and see how many responses moved
- Check the result against a quality alarm level set in advance
- State whether business quality has degraded, with the numbers to support it

By the end of this lab you will be able to run a baseline re-test on any AI workflow that has a written quality standard.

## In Plain Words

- **What you are doing:** You will mark 20 answers that PolicyPal gave to employees, the way a teacher marks a test. Then you will find out whether PolicyPal is doing worse than it used to.
- **Why it matters:** An AI tool can get worse without anyone noticing. Marking the same kind of answers on a regular schedule is how a company catches that early.
- **You do not have to:** download anything, open a spreadsheet, or do any maths. The workspace adds up the score for you, and everything you type saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

**Words you will see in this lab**
- **Business Quality Score:** a score out of 100. It is the share of your pass or fail marks that were passes.
- **Baseline:** the score PolicyPal got when it was first checked. It is the starting point that new scores are compared with.
- **Criteria:** the four things a good answer must do. You mark every answer against all four.
- **Alarm level:** the score at which the company has already decided "something is wrong, so investigate". It is decided before the test, not after.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `2.1 Baseline Re-Test and Business Quality Score` in the left sidebar.

## Procedure

1. **Look at the first of the two files you were sent.** You asked your administrator for "the data" and got two files. Each file is a tab in the workspace. You need to work out which one is any use for marking answers.
    - Click the tab called `Activity Log`. It is probably already open.
    - Read the column headings across the top, from left to right.
    - Click the tab called `Output Export`. Read its column headings too.

0. **Decide which file you can mark.** You can only mark an answer if you can see the answer. One of the two files has the actual questions and answers, and the other only has facts about who used PolicyPal and when.
    - Look at the headings again. Which tab has a column with what PolicyPal actually said?
    - Click the `My Answer` tab.
    - In the section **Which file can you score?**, use the drop-down to pick the file that has the actual answers.

    <details><summary>ANSWER:</summary>

    `Output Export` is the file you can mark. `Activity Log` cannot be marked, because it has no answers in it.

    </details>

0. **Say why you are keeping the other file.** You are not going to throw the `Activity Log` away, even though you cannot mark it. It might come in useful later, and you should be able to say why.
    - Click the `Activity Log` tab and look at the three columns `ModelProviderName`, `ModelName`, and `ModelVersion`. These say which AI model was running.
    - Click the `My Answer` tab.
    - In the same section, write one line saying why you are keeping the activity log.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "It records which ______ was running on each date, which could explain a ______ later."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "It shows which AI model was running on each date, which could explain a change in quality later."

    </details>

0. **Read the four rules for a good answer.** You cannot mark fairly without written rules. These rules come from the company's rulebook, called the Quality Standard.
    - Click the `Quality Standard` tab.
    - Find the part headed **3. Scoring criteria** and read it.
    - Here is the same thing in short. A good answer:

    ```text
    c1  cites a named, current policy document
    c2  states the figure or entitlement exactly as written in policy
    c3  answers the specific question asked, not a general summary
    c4  refers accommodation / protected-leave / disputed questions to a human
    ```

    - Scroll down to **9. Reference figures from current policy**. This table holds the correct figures from the current policies. You check every number an answer gives against it.

0. **Mark the first five answers, then compare with someone.** Before you mark all 20, you check that you and another person mark the same way. That is what makes marking fair, and not just your opinion.
    - Click the `Output Export` tab.
    - For answers `BL-01` to `BL-05`, read the `Assistant response` and the `Cited source`.
    - In each of the four last columns, choose `Met` if the answer passed that rule, or `Not met` if it failed.
    - Compare your five marks with a partner's, or with the instructor's answers. If you disagree, re-read the rule together, agree what it means, and fix any mark you now think is wrong.

    > When an auditor asks "isn't this just your opinion?", this step is the answer: the criteria are written down, more than one person applied them to the same responses, and the scores agreed. That is what makes a pass/fail judgment defensible. (An auditor is a person whose job is to check a company's proof.)

    <details><summary>Hint 1: how to mark each of the four rules</summary>

    - **c1:** Look at the `Cited source` column, not at the answer text. `Met` if it names a specific, current policy document. `Not met` if it is a vague phrase such as "company policy" or names an older version of a policy.
    - **c2:** `Met` if every number in the answer matches the table in section **9** of the `Quality Standard` tab. `Not met` if a number is different from the table, or is vague ("about", "roughly"). If the answer contains no numbers, choose `Met`, because there is nothing to get wrong.
    - **c3:** `Met` if the answer gives the specific thing the employee asked for. `Not met` if it only gives a general summary, or tells the employee to go and read the policy or check a website.
    - **c4:** This rule only applies to questions about an accommodation, a protected leave, or a decision the employee is disputing. `Met` if the answer sends the employee to a person in HR. For every other question, choose `Met`.

    </details>

    <details><summary>Hint 2: how to spot a wrong figure</summary>

    Click the `Cited source` heading to sort the list. Answers about the same policy end up next to each other, so when two answers give different numbers for the same thing you can see it straight away. Look both numbers up in section **9** of the `Quality Standard` tab: only the one that matches meets c2.

    </details>

0. **Mark the other 15 answers the same way.** Every answer in the list needs a mark, because the sample size of 20 is set by how risky PolicyPal is rated (Medium risk means 20 answers). You do not get to choose to do fewer. If you run short of time, the fix is to skip a rule, never to skip an answer.
    - Work down the `Output Export` tab from `BL-06` to `BL-20`.
    - For each answer, choose `Met` or `Not met` in all four columns.
    - Keep an eye on the score box at the top. It updates as you go.

0. **Read your result.** When every box is filled in, the score box at the top of the tab shows the answer. You do not have to do any maths.
    - Look at the box at the top of the `Output Export` tab. Find **Current Business Quality Score**, **Recorded baseline**, and **Change (points)**.
    - Click the `My Answer` tab.
    - In the section **The result**, type your current score and the change in points (your score minus the baseline).

    <details><summary>ANSWER:</summary>

    - Current Business Quality Score: about `81`, if you marked carefully
    - Recorded baseline: `88`
    - Change: a drop of about `7` points

    </details>

0. **Check the result against the alarm level.** The company decided in advance what score should set off an alarm. You now compare your score with that line, so you are not guessing after the fact.
    - Click the `Quality Standard` tab and read **8. Quality alarm level**.
    - Click the `My Answer` tab.
    - In the section **Check against the alarm level**, write which of the two lines your result crosses, and whether that means an investigation is needed.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "My score of ______ is ______ the floor of ______, and a drop of ______ points is ______ the limit of ______."

    </details>

    <details><summary>ANSWER:</summary>

    81 is below the 85 floor, and a 7-point drop is more than the 5-point limit. Both lines are crossed, so an investigation is needed.

    </details>

0. **Count the answers that got worse.** Each answer already had its own score when the baseline was set. Some answers now score lower than they did then. The number of those tells you how widespread the problem is.
    - Look at the box at the top of the `Output Export` tab.
    - Find **Responses below their own baseline** and read the number.
    - Click the `My Answer` tab and, in the section **The result**, type that number.

    <details><summary>ANSWER:</summary>

    About `4` of the 20 answers scored lower than they did at baseline.

    </details>

0. **Find the rule that got worse the most.** Knowing which of the four rules is failing tells you what kind of problem PolicyPal has.
    - In the box at the top of the `Output Export` tab, click **How each criterion moved**.
    - Look for the rule with the biggest drop in the **Change** column.
    - Click the `My Answer` tab and, in the section **The result**, type which rule it is.

    <details><summary>ANSWER:</summary>

    `c3` (answers the question that was asked). Several answers now give a general summary, or send the employee back to the policy, instead of giving the actual answer.

    </details>

0. **Say in one sentence whether quality has got worse.** A clear summary sentence is what a busy manager will actually read. It should include the numbers.
    - Click the `My Answer` tab.
    - In the section **State whether business quality has degraded**, write one sentence. It should say how much the score changed, whether the alarm level was crossed, and how many answers got worse.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Business quality has ______ and has ______ the alarm level: the Business Quality Score fell ______ points from ______ to ______, and ______ of 20 responses scored below their recorded baseline."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Business quality has degraded and has crossed the alarm level: the Business Quality Score fell 7 points from 88 to 81, below the 85 floor, and 4 of 20 baseline responses scored below their recorded baseline."

    </details>

0. **Start the test record.** A test record is a short written report of a check. Anyone reading it later should be able to see what you tested, when, and against what rules.
    - Click the `My Answer` tab.
    - In the section **Start the test record**, fill in all three boxes.
    - For the first box, use the `Case` column on the `Output Export` tab to see which answers you marked (the first and last case numbers).
    - For the third box, use the title at the top of the `Quality Standard` tab.

    <details><summary>Hint 1: sentences to start from</summary>

    - What was tested: "The ______ workflow, using the ______-response baseline set, cases ______ to ______."
    - When: today's date.
    - Against what standard: the name of the standard, from the title of the `Quality Standard` tab.

    </details>

    <details><summary>Hint 2: example answers</summary>

    - What was tested: "The PolicyPal workflow, using the 20-response baseline set, cases BL-01 to BL-20."
    - Against what standard: "The PolicyPal Business Quality Standard."

    </details>

0. **Decide what to do first.** Quality has got worse. You now decide whether to look for the cause yourself, or to hand the problem straight to the tech team. Look for the cause yourself first, because a symptom on its own is not much use to someone who has to fix it.
    - Click the `My Answer` tab.
    - In the section **The handoff**, use the drop-down to pick what you would do first.
    - Then write one line saying why.

    <details><summary>ANSWER:</summary>

    You look for the cause yourself first. You do not pass on a symptom. Lab 2.2 is where you find the cause and collect the proof that the tech team would need.

    </details>

0. **Check that you have finished.** The workspace keeps count of the boxes you have filled in.
    - Look at the top right of the workspace. It says something like `X of Y answers filled in`.
    - When X is the same as Y, you are done.
    - Your answers save automatically as you type, so there is nothing to save or send.
    - If you would like a copy for yourself, click the `Save as PDF` button on the `My Answer` tab.

## Conclusion

In this lab you determined which export could actually be scored, calibrated your scoring against a reference, ran a fixed baseline set against a written standard, read the Business Quality Score it produced, and measured it against an alarm level set in advance. This is the periodic control test that produces evidence rather than reassurance. You have run it once here, with the standard and the sample supplied; what transfers to a workflow of your own is the method and the completed test record, not this single run.
