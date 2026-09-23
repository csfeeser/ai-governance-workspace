# Reviewer Metrics and Anomaly Detection

## Lab Objective

**Read human-oversight metrics from a reviewer decision log and flag the reviewers whose patterns warrant a closer look.**

Human review is a control, and controls need monitoring. A reviewer who approves everything gives you the appearance of oversight with none of the substance. In this lab you take a 30-day log of human review decisions on PolicyPal, read the overall agreement and override rates, then cut those numbers by reviewer, by case type, and by week. The anomalies only become visible once the numbers are broken down, and that breakdown is the skill.

In this lab, you will:
- Read the overall agreement and override rates
- Break override rates down by reviewer, case type, and week
- Flag a reviewer whose override rate is anomalously low and one whose rate is anomalously high, and test each read before naming it
- Read a week-over-week override trend
- Check seeded duplicate cases for reviewer consistency

By the end of this lab you will be able to audit whether human oversight of an AI workflow is real.

## In Plain Words

- **What you are doing:** Companies often say "a human checks the AI's work". You will look at a list of what five human checkers actually did, and spot any who may not be doing the job properly.
- **Why it matters:** A human check only protects anyone if the human is really checking. Someone who clicks "approve" on everything makes it look safe when it is not.
- **You do not have to:** download anything, open a spreadsheet, or do any maths. The workspace adds up the numbers when you ask, and everything you type saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

**Words you will see in this lab**
- **Reviewer:** a person who checks the AI's work.
- **Override:** when a reviewer disagrees with the AI and does something different. Overriding is normal. A reviewer who never does it is suspicious.
- **Override rate:** out of every 100 decisions, how many the reviewer changed. It is shown as a percentage.
- **Outlier:** someone whose numbers are far away from everyone else's.
- **Duplicate case:** the same case, secretly given to the same reviewer twice on different days, to see whether they decide it the same way both times.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `3.1 Reviewer Metrics and Anomaly Detection` in the left sidebar.

## Procedure

1. **Look at the list of decisions.** This list is what the whole lab is built on, so take a minute to understand what a row means. Each row is one case that a human reviewer looked at. It shows what the AI decided, what the human decided (approve, reject, or route to a human), which reviewer it was, and which week.
    - Click the tab called `Reviewer Log`. It is probably already open.
    - Find the `override` column on the right. It has already been filled in for you.
    - `1` means the human disagreed with the AI. `0` means the human agreed.

0. **Find the overall override rate.** This is the number to compare each reviewer against. It tells you how often the reviewers disagree with the AI when everyone is put together.
    - At the top of the `Reviewer Log` tab, find the drop-down called **Group by**. Choose `reviewer`.
    - The table now has one row per reviewer, and one extra row at the bottom called **All**.
    - Read the percentage in the **Rate** column of the **All** row.
    - Click the `My Findings` tab.
    - In the section **Overall**, type that percentage.

    <details><summary>ANSWER:</summary>

    About `18%`. That means the humans agreed with the AI about 82% of the time.

    </details>

0. **See the rate for each reviewer.** Now compare the five reviewers with each other. A reviewer who is far above or far below the others needs a closer look.
    - Go back to the `Reviewer Log` tab. **Group by** should still say `reviewer`.
    - Read the **Rate** column for each of the five reviewers.

    <details><summary>ANSWER:</summary>

    Roughly: R-A 2%, R-B 43%, R-C 17%, R-D 16%, R-E 14%.

    </details>

0. **Spot the reviewer who almost never disagrees.** A reviewer far below the others might be clicking "approve" without reading. That is only a reason to look closer. It is not proof yet.
    - Find the reviewer whose rate is much lower than the others.
    - Click the `My Findings` tab.
    - In the section **Low-override outlier**, use the first box to type that reviewer and their rate.

    <details><summary>ANSWER:</summary>

    R-A, at about 2%, when the team average is 18%.

    </details>

0. **Check whether R-A just has an easy pile.** Before you accuse anyone, check the boring explanation. Maybe R-A simply got easy cases that did not need changing. If so, R-A would still change the odd hard case. If R-A never changes any of them, that is different.
    - Go back to the `Reviewer Log` tab. Keep **Group by** on `reviewer`.
    - Find the drop-down called **Split by** and choose `case_type`. Find R-A's row and read across.
    - Now change **Split by** to `week`. Read R-A's row again.
    - Each cell shows overrides out of decisions. For example, `1/11` means 1 override out of 11 decisions.

    <details><summary>ANSWER:</summary>

    R-A overrides nothing in four of the five case types, including case types where most of the other reviewers change decisions regularly. R-A's rate is zero in three of the four weeks. The one exception is a single override on a `pto` case in week 3. Mention that exception. Do not explain it away. With only 42 decisions, one override is what an honest look at this data looks like.

    </details>

0. **Write down what you found, and what would settle it.** Numbers on their own settle nothing. You need to say what they suggest, and what one check would turn the suggestion into proof.
    - Click the `My Findings` tab.
    - In the section **Low-override outlier**, use the second box to write what the case-type and week tables showed.
    - Add the one check that would settle it.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "R-A overrides ______ in ______ of the five case types and ______ of the four weeks, which an easy queue would not ______. A ______ reviewer re-scoring a sample of R-A's ______ would settle it."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "R-A overrides nothing in four of the five case types and in three of the four weeks, which an easy queue would not produce. A second reviewer re-scoring a sample of R-A's approvals would settle it."

    </details>

0. **Spot the reviewer who disagrees the most.** The opposite problem is worth looking at too. Someone who overrides far more than everyone else might be doing something odd.
    - Go back to the `Reviewer Log` tab. Change **Split by** back to `None`.
    - Find the reviewer whose rate is much higher than the others.
    - Click the `My Findings` tab.
    - In the section **High-override outlier**, use the first box to type that reviewer and their rate.

    <details><summary>ANSWER:</summary>

    R-B, at about 43%.

    </details>

0. **Check that it is the reviewer and not the AI.** If R-B just got a strange batch of cases, the AI could be to blame. If R-B got the same kind of work as everyone else, the reviewer is the difference.
    - Go back to the `Reviewer Log` tab. Set **Group by** to `reviewer` and **Split by** to `case_type`.
    - Compare the number of decisions in R-B's boxes (the number after the slash) with the other reviewers' boxes. Ask: does R-B get a similar mix of cases?
    - Now set **Split by** to `ai_decision` and look again.
    - Click the `My Findings` tab.
    - In the section **High-override outlier**, use the second box to write what you compared and what it tells you.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "R-B's ______ mix and ______ decisions look ______ the other reviewers', so the high override rate points to the ______, not the ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "R-B's case mix matches the rest of the team. The high override rate is the reviewer, not the AI."

    </details>

0. **Look at how the rate changed week by week.** A rate that is climbing means something is changing. You need to know when, so you can ask why.
    - Go back to the `Reviewer Log` tab. Set **Group by** to `week` and **Split by** to `None`.
    - Read the rate for weeks `W1`, `W2`, `W3`, and `W4`.
    - Click the `My Findings` tab.
    - In the section **Weekly trend**, write what the change shows and what you would check next.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "The override rate rose from ______ to ______ over the month. It could mean the ______ is getting worse or that the ______ are getting stricter. I would check the ______ for the same period."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "The override rate rose from about 11% to about 26% over the month. It could mean the AI is getting worse or that the reviewers are getting stricter. I would check a quality audit of the AI's output for the same period to tell which."

    </details>

0. **Find the secret repeat cases.** To test whether a reviewer is really reading, the company slipped the same case to the same reviewer twice, on two different days. A careful reviewer decides it the same way both times. Repeat cases have `DUP-` at the start of their case number.
    - Go back to the `Reviewer Log` tab and click the button **Clear sort, filters and grouping**.
    - Under the heading `case_id` there is a small box. Click in it and type `DUP-`.
    - Click the word `case_id` to put the rows in order.
    - Each case appears twice, ending in `a` and `b`, for example `DUP-01a` and `DUP-01b`.

    <details><summary>ANSWER:</summary>

    Twelve rows, making six pairs: `DUP-01a` and `DUP-01b`, up to `DUP-06a` and `DUP-06b`.

    </details>

0. **Compare the two decisions in each pair.** This is how you catch a reviewer who is not reading.
    - For each pair, compare the `human_decision` on the `a` row with the `human_decision` on the `b` row.
    - Ask: did the reviewer decide the same way both times?

0. **Name the reviewer who was inconsistent.**
    - Click the `My Findings` tab.
    - In the section **Duplicate cases**, type the reviewer who decided a repeat case two different ways. Add how many of their pairs came out different.

    <details><summary>ANSWER:</summary>

    R-D, on one of their two pairs.

    </details>

0. **Check that you have finished.** The workspace keeps count of the boxes you have filled in.
    - Look at the top right of the workspace. It says something like `X of Y answers filled in`.
    - When X is the same as Y, you are done.
    - Your answers save automatically as you type, so there is nothing to save or send.
    - The finding about R-A is what Lab 3.2 is about.
    - If you would like a copy for yourself, click the `Save as PDF` button on the `My Findings` tab.

## Challenges

These are optional and are not recorded in the workspace.

**🥉 Bronze:** On the `Reviewer Log` tab, set **Group by** to `reviewer`. Use the **Rows** and **overrides** columns to work out the overall override rate with R-A's decisions left out. By how many points was R-A's tiny rate pulling the overall number down?

**🥈 Silver:** One reviewer's own rate is climbing steeply from week to week, while the others stay flat. It is hidden inside the team total because their 30-day rate still looks normal. Set **Group by** to `reviewer` and **Split by** to `week`, find them, and say what you would check first.

**🥇 Gold:** The overall override rate rose from about 11% to about 26% over the month. Suggest the one number you would watch every week that would have shown this two weeks earlier, and say why it would have.

## Conclusion

In this lab you read agreement and override rates, cut them by reviewer and by week, flagged two reviewers whose rates warrant a closer look and one whose duplicate-case decisions were inconsistent, and read a rising override trend as a signal to cross-check output quality. The metrics point you to who to examine and what to check next; they do not hand you a verdict. This is how you check whether human oversight of an AI workflow is doing real work.
