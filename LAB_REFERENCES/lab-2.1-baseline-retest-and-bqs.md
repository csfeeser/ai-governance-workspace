# Baseline Re-Test and Business Quality Score

## Lab Objective

**Check whether the quality of an AI workflow's answers is drifting: score a sample against a written standard, compare it to the recorded baseline and the alarm level, find the most likely cause, and decide who to tell.**

This is the periodic control test that turns "we monitor the AI" into evidence. You are handed two exports and first have to work out which one shows the quality of PolicyPal's answers. Then you mark a sample of answers against a supplied quality standard, read the Business Quality Score that results, and compare it with the score the same kind of answers got when the baseline was set. When the score has dropped, you look for the most likely cause and decide who needs to hear about it.

If you ask an administrator for "the audit log," on any platform, expect a spreadsheet of who-did-what-when, not the actual questions and answers. Microsoft Copilot's audit search and its eDiscovery collection are two different requests to two different tools; Claude Enterprise's "Export logs" and "Export Data" are two separate buttons on the same settings page, and only one of each pair has real content. Knowing which one to ask for is the first skill this lab tests.

The quality standard says a Medium-risk workflow like PolicyPal needs 20 answers marked at every review. To save time, you mark five of them in this lab; the other 15 have already been marked for you.

In this lab, you will:
- Identify which of two platform exports shows the quality of the answers
- Mark answers against four pass/fail criteria, and check your marking against someone else's
- Read the Business Quality Score and say whether quality is going up or down
- Check the result against a quality alarm level set in advance
- Find the most likely cause of a drop in quality from the activity log
- Decide who to speak to about the cause

By the end of this lab you will be able to run a baseline re-test on any AI workflow that has a written quality standard.

## In Plain Words

- **What you are doing:** You will mark some of the answers PolicyPal gave to employees, the way a teacher marks a test. Then you will find out whether PolicyPal is doing worse than it used to, why, and who needs to know.
- **Why it matters:** An AI tool can get worse without anyone noticing. Marking the same kind of answers on a regular schedule is how a company catches that early.
- **You do not have to:** download anything, open a spreadsheet, or do any maths. The workspace adds up the score for you, and everything you type saves by itself.
- **If you feel lost:** in the workspace, every instruction is in a numbered orange box. Do the boxes in order, from the left-most tab to the right-most tab.

**Words you will see in this lab**
- **Business Quality Score:** a score out of 100. It is the share of your pass or fail marks that were passes.
- **Baseline:** the score PolicyPal got when it was first checked. It is the starting point that new scores are compared with.
- **Criteria:** the four things a good answer must do. You mark every answer against all four.
- **Activity log:** a record the platform keeps of who used the AI, when, and which AI model was running. It does not contain the answers.
- **Alarm level:** the score at which the company has already decided "something is wrong, so investigate". It is decided before the test, not after.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `2.1 Baseline Re-Test and Business Quality Score` in the left sidebar.
- Then do Step 1 to Step 7 in the workspace. You do not need to keep this page open while you work.

## What You Will Do in the Workspace

Everything you do in this lab happens in the workspace.

- The workspace has five tabs. Start on the left-most tab and work to the right. You never need to go back to a tab you have finished.
- On each tab, work from top to bottom. Every instruction is in an orange box with a step number, from Step 1 to Step 7. Everything outside the orange boxes is the material you need for that step.
- If a step asks you to answer something, the answer box is inside the orange box.
- Stuck? Each orange box has hints you can open, and most have a **Show the answer** button.
- At the bottom of each tab, click **Go to the next tab** when you have finished every step on it.
- Everything you type saves by itself. The counter at the top right shows how many answers you have filled in.

### Tab 1: The Two Files (Step 1)

![The Two Files tab, showing Step 1 above the Activity Log and the Output Export](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-2-1-1-the-two-files.png)

You learn the difference between the two kinds of export an AI platform can give you, an activity log and a content export, and choose the one that can show whether PolicyPal's answers are getting worse.

### Tab 2: Mark the Answers (Steps 2 and 3)

![The Mark the Answers tab, showing Step 2 above the scoring rules and five answers](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-2-1-2-mark-the-answers.png)

You mark five of PolicyPal's answers against four rules, choosing Met or Not met for each. The rules and the correct policy figures are shown right under the step. Then, if you have time, you compare your marks with a partner's.

### Tab 3: Your Result (Steps 4 and 5)

![The Your Result tab, showing Step 4 above the score box](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-2-1-3-your-result.png)

The workspace adds your marks to the 15 already marked. You say whether answer quality is going up or down compared with the baseline, and whether the score has reached the alarm level set in advance.

### Tab 4: The Cause (Steps 6 and 7)

![The Cause tab, showing Step 6 above the marked answers in date order and the activity log](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-2-1-4-the-cause.png)

You find the date the marks started to drop, check the activity log for what changed around that date, and write down the most likely cause. Then you decide who to speak to about it.

### Tab 5: My Answer

![The My Answer tab, showing the result built from the student's answers](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-2-1-5-my-answer.png)

You do not type anything here. This tab gathers your answers into one result. Anything you missed says which step to go back to. Click **Save as PDF** if you want a copy.

## Conclusion

In this lab you worked out which export can actually show answer quality, marked a sample against a written standard, read the Business Quality Score it produced, measured it against the baseline and an alarm level set in advance, traced the drop to its most likely cause, and decided who needed to hear about it. This is the periodic control test that produces evidence rather than reassurance. You have run it once here, with the standard and most of the sample supplied; what transfers to a workflow of your own is the method, not this single run. In Lab 2.2, the next month's review, the score drops again for a different reason, and you check all four possible causes before deciding who to tell.
