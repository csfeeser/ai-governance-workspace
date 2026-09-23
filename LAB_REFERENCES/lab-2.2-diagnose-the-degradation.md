# Diagnose the Degradation and Document the Test

## Lab Objective

**Find the cause of a confirmed drop in AI output quality, cite the evidence that proves it, and complete a test record a third party could act on.**

Confirming that quality dropped is only half of an audit. The half that makes it evidence is naming *why* it dropped and writing it down so someone who was not there can act on it. In this lab you receive a PolicyPal sample that has already been scored and has clearly degraded, plus the platform activity log for the same period. You test the drop against the four known causes of degradation, identify the real one, cite the exact column that proves it, and complete a test record.

In this lab, you will:
- Confirm a Business Quality Score drop and locate when it happened
- Test a quality drop against the four causes of degradation
- Identify a vendor model change from an activity log and cite the proof
- Complete a test record with method, result, and conclusion

By the end of this lab you will be able to diagnose and document a quality regression in any AI workflow that keeps an activity log.

## In Plain Words

- **What you are doing:** PolicyPal's answers have got worse. You will play detective. You will work out when it started, what caused it, and then write it up.
- **Why it matters:** You cannot fix a problem until you know what caused it. And the people who can fix it will want proof before they act.
- **You do not have to:** download anything, open a spreadsheet, or do any maths. The workspace does the totals for you, and everything you type saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

**Words you will see in this lab**
- **Business Quality Score:** a score out of 100 for how well PolicyPal's answers are doing.
- **Baseline:** the score PolicyPal got when it was first checked. New scores are compared with it.
- **AI model:** the "brain" inside PolicyPal. Another company makes it.
- **Vendor:** a company you buy something from. Here, the vendor is the company that makes the AI model.
- **Activity log:** a diary the platform keeps of every time the AI is used.
- **Test record:** a short written report of a check: what you tested, how, and what you found.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `2.2 Diagnose the Degradation` in the left sidebar.

## Procedure

1. **Look at the marked answers.** In this lab, somebody has already marked the answers for you. Each answer has two marks out of 4: the mark it got when the baseline was set, and the mark it gets now. You are not marking anything. Your job is to work out why the marks dropped.
    - Click the tab called `Scored Sample`. It is probably already open.
    - Read the note at the top of the table.
    - Look at the columns **Baseline score (of 4)** and **Current score (of 4)**.

0. **Confirm that the score really dropped.** Before you look for a cause, make sure there really is a problem to explain. The workspace has already added up the marks for you.
    - Look at the box at the top of the `Scored Sample` tab.
    - Read the **Current Business Quality Score**, the **Recorded baseline**, and the **Change (points)**.

    <details><summary>ANSWER:</summary>

    The current score is about `69`, against a recorded baseline of `90`. That is a drop of roughly `21` points.

    </details>

0. **Find the date when it went wrong.** If the marks dropped suddenly on one day, that day points to what changed. If they crept down slowly, that is a different kind of problem.
    - Click the word `date` at the top of the date column. The rows now line up in date order.
    - Read down the **Baseline score (of 4)** and **Current score (of 4)** columns together.
    - Find the first date on which the current mark is lower than the baseline mark.
    - Click the `Test Record` tab.
    - In the section **Confirm the drop**, type that date.

    <details><summary>Hint 1: where to look</summary>

    Look for the first date where the current mark is lower than the baseline mark. Then ask: do the low marks start at one point, or are they spread out evenly?

    </details>

    <details><summary>ANSWER:</summary>

    Answers on or after `2026-08-12` get much lower marks, and answers before that date are at or near their baseline. It is a sudden step down, not a slow slide.

    </details>

0. **Read the four possible causes.** When an AI tool's answers get worse, there are only four usual reasons. You will check each one against the evidence, and not just guess.
    - The **inputs** changed: the documents the AI reads from changed.
    - The **AI model** changed: the company that makes the "brain" swapped or updated it.
    - The **company policy** changed: the real rules changed, so the old answers are now out of date.
    - The **prompt** changed: someone changed the instructions given to the AI.

0. **Check whether the company policy changed.** If the policy changed, PolicyPal's answers would look worse because the rules moved, not because PolicyPal broke.
    - Click the `Scored Sample` tab.
    - Look at the `Cited source` column. Each source name includes the date its policy started.
    - Compare the sources for answers from before your date with the sources from after it.
    - Click the `Test Record` tab.
    - In the section **Rule out three of the four causes**, use the drop-down called **Changed company policy** to pick what you found.

    <details><summary>ANSWER:</summary>

    The sources and their start dates are the same before and after 2026-08-12. So it is not a policy change.

    </details>

0. **Check whether the prompt changed.** The prompt is the set of instructions PolicyPal is given. You cannot see the prompt itself, but the platform gives PolicyPal a new version number every time someone changes its instructions and publishes them. Do not judge this from the answers. Wordier answers could come from a new prompt or from a new model, so the answers cannot tell you which one it was.
    - Click the `Activity Log` tab.
    - Click the word `CreationTime` at the top of that column. The rows now line up in date order.
    - Read down the `AgentVersion` column. Ask: is the version number the same before and after your date?
    - Click the `Test Record` tab.
    - In the same section, use the drop-down called **Modified prompt** to pick what you found.

    > Not every platform shows an agent version. If yours does not, ask whoever manages the assistant for the dates its instructions were changed. The question you are answering is the same.

    <details><summary>ANSWER:</summary>

    `AgentVersion` is `1.4` on every row, before and after the drop. Nobody published new instructions, so the prompt did not change.

    </details>

0. **Check whether the inputs changed.** The inputs are the documents PolicyPal reads to find its answers. If those changed, the answers would change too. The activity log records which documents PolicyPal actually read each time.
    - Stay on the `Activity Log` tab, still sorted by `CreationTime`.
    - Read down the `AccessedResources` column. Ask: does PolicyPal read the same set of documents before and after your date?
    - Click the `Test Record` tab.
    - In the same section, use the drop-down called **Changed inputs** to pick what you found.

    <details><summary>ANSWER:</summary>

    Before and after the drop, PolicyPal reads the same five documents: `PTO Policy 2025`, `Expense & Travel Policy 2025`, `Benefits Guide 2025`, `Code of Conduct 2025`, and `Remote Work Policy 2024`. Nothing new appears and nothing goes missing, so the inputs did not change. (Another column does change later in the month. That is the Silver challenge. It starts after the drop, so it cannot be what caused it.)

    </details>

0. **Go and look at the AI model.** Three of the four causes are now ruled out. The last one is the AI model. The same activity log also records which AI model was running each time PolicyPal was used.
    - Stay on the `Activity Log` tab.
    - Find the three columns called `ModelProviderName`, `ModelName`, and `ModelVersion`. They say which AI model was running.

    > Real logs do not always show all three. It depends on the platform and how it is set up. The company name is the one you can most often see, and the version number is the one you see least. Look at whichever of these you are given. The method is the same.

0. **Find the date the AI model changed.** If the model was swapped a day or two before the answers got worse, that is very strong evidence.
    - Make sure the rows are still in `CreationTime` order.
    - Read down the `ModelName` and `ModelVersion` columns together.
    - Find where they change.
    - Click the `Test Record` tab.
    - In the section **The vendor model update**, write what changed and on what date.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "`ModelName` changes from ______ to ______ and `ModelVersion` from ______ to ______, on ______."

    </details>

    <details><summary>ANSWER:</summary>

    Both change on the same day. `ModelName` changes from `gpt-4o` to `gpt-55-high`, and `ModelVersion` changes from `2024-11-20` to `2025-06-15`, on `2026-08-11`. The company name stays `OpenAI`, so this is a new version from the same company, not a switch to a different company.

    </details>

0. **Compare the two dates.** Cause and effect need to be close together in time. If the model changed and the marks dropped just afterwards, that fits.
    - Compare the date the model changed with the date you found in step 3 when the marks dropped.

    <details><summary>ANSWER:</summary>

    The model changed on 2026-08-11 and the marks dropped on 2026-08-12. They are one day apart.

    </details>

0. **Write down the cause and the proof.** A cause without proof is only a guess. Someone who was not here needs to be able to check what you say.
    - Click the `Test Record` tab.
    - In the section **The vendor model update**, write one sentence that names the cause and gives the proof: the tab, the column, and the values.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Cause: ______. Evidence: in the ______, ______ changes from ______ to ______ on ______, ______ before the Business Quality Score drop."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Cause: vendor model update on 2026-08-11. Evidence: in the Activity Log, ModelName changes from gpt-4o to gpt-55-high and ModelVersion from 2024-11-20 to 2025-06-15 on that date, one day before the Business Quality Score drop."

    </details>

0. **Start the test record.** A test record is a short written report of a check. This first part says what you tested, when, and against what rules.
    - Click the `Test Record` tab.
    - Fill in the three sections **What was tested**, **When**, and **Against what standard**.
    - The `Case` column on the `Scored Sample` tab shows the range of answers (the first and last case numbers).
    - These answers were marked against the PolicyPal Business Quality Standard.

    <details><summary>Hint 1: sentences to start from</summary>

    - What was tested: "The ______ workflow, using the ______-response baseline set, cases ______ to ______."
    - When: today's date.
    - Against what standard: the name of the standard.

    </details>

    <details><summary>Hint 2: example answers</summary>

    - What was tested: "The PolicyPal workflow, using the 20-response baseline set, cases L22-01 to L22-20."
    - Against what standard: "The PolicyPal Business Quality Standard."

    </details>

0. **Say how you did the check.** Someone reading your record needs to know what you did, so they can trust the result or repeat it.
    - In the section **Method**, write one or two sentences saying what you compared and where you looked.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Compared the ______ scores with the ______ scores, then tested the ______ causes against the ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Compared current scores with baseline scores in the scored sample. Tested the four causes: policy against the cited sources' effective dates, and prompt, inputs and model against the AgentVersion, AccessedResources and model columns of the activity log."

    </details>

0. **Say what the numbers were.** The result is the plain facts, without opinion yet.
    - Look at the box at the top of the `Scored Sample` tab.
    - In the section **Result**, write the score against the baseline, how many answers scored below their own baseline, and which rule (criterion) moved most.
    - To see the rule that moved most, click **How each criterion moved** in that box.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "The Business Quality Score fell from ______ to ______; ______ of 20 responses scored below their own baseline; ______ was the criterion most affected."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "The Business Quality Score fell from 90 to about 69; about 10 of 20 responses scored below their own baseline; c3 was the criterion most affected."

    </details>

0. **Say what you decided, and why.** The conclusion is the answer to "so what happened?". It is the part that a busy person reads first.
    - In the section **Conclusion**, say whether quality got worse.
    - If it did, say what caused it and what proof you are pointing to.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Degradation ______. The cause is ______ on ______. Evidence: ______."

    </details>

    <details><summary>Hint 2: an example answer</summary>

    "Degradation confirmed. The cause is a vendor model update on 2026-08-11. Evidence: the model name and version change in the Activity Log on that date, one day before the drop."

    </details>

0. **Check that you have finished.** The workspace keeps count of the boxes you have filled in.
    - Look at the top right of the workspace. It says something like `X of Y answers filled in`.
    - When X is the same as Y, you are done.
    - Your answers save automatically as you type, so there is nothing to save or send.
    - This record is the kind of paper you would later put in an evidence packet (Module 5), and the kind you would attach to a message asking the tech team to fix a problem (Module 4).
    - If you would like a copy for yourself, click the `Save as PDF` button on the `Test Record` tab.

## Challenges

These are optional. Your answers to them are saved on the `Challenges` tab.

**🥉 Bronze:** Click the `Bronze: Second Sample` tab. This is a second set of marked answers from a different time period. Find out why its marks dropped, in the same way. This time the clue is in the `Source effective date` column.

**🥈 Silver:** A second real change is hiding in the `Activity Log` in the same period as the model change. Find it, and explain in two or three sentences how it adds to the model change, instead of replacing it as the cause.

<details><summary>Hint: where to look</summary>

Sort the `Activity Log` by `CreationTime` and look at the columns other than the model ones. One of them is empty until a date in the same period as the model change.

</details>

**🥇 Gold:** Write your finding as a five-sentence note for people who are not technical. Say what changed, how you know, what it is costing, what you are asking for, and by when.

## Conclusion

In this lab you confirmed a drop in Business Quality Score, located the date it began, tested it against the four causes of degradation, identified an unannounced vendor model change from the activity log, and wrote a test record another person could act on. That record is both evidence for the audit packet and the basis for an escalation.
