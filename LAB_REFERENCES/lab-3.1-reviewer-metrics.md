# Reviewer Metrics and Anomaly Detection

## Lab Objective

**Read human-oversight metrics from a reviewer decision log, flag the reviewers whose patterns warrant a closer look, test the innocent explanations before naming anyone, and route the finding to the right owner.**

Human review is a control, and controls need monitoring. A reviewer who approves everything gives you the appearance of oversight with none of the substance. In this lab you take last quarter's 30-day log of human review decisions on PolicyPal and see why the team's overall override rate proves little on its own. Then you break the numbers down by reviewer, by case type and by week. The anomalies only become visible once the numbers are broken down, and that breakdown is the skill.

In this lab, you will:
- Explain what the reviewer log records and why an overall override rate can hide problems
- Flag a reviewer whose override rate is anomalously low, and rule out the "easy pile" explanation
- Flag a reviewer whose rate is anomalously high, and decide whether it is the reviewer or the AI
- Read a week-over-week override trend and check it against the AI's quality for the same period
- Check seeded repeat cases for reviewer consistency
- Route the most serious finding to the owner of the review process

By the end of this lab you will be able to audit whether human oversight of an AI workflow is real.

## In Plain Words

- **What you are doing:** Companies often say "a human checks the AI's work". You will look at a list of what five human checkers actually did, and spot any who may not be doing the job properly.
- **Why it matters:** A human check only protects anyone if the human is really checking. Someone who clicks "approve" on everything makes it look safe when it is not.
- **You do not have to:** download anything, open a spreadsheet, or do any maths. The workspace adds up the numbers for you, and nearly every answer is a drop-down menu.
- **If you feel lost:** in the workspace, every instruction is in a numbered orange box. Do the boxes in order, from the left-most tab to the right-most tab.

**Words you will see in this lab**
- **Flagged case:** an answer PolicyPal was not sure about, held back for a person to check.
- **Reviewer:** a person who checks the AI's work.
- **Override:** when a reviewer disagrees with the AI and does something different. Overriding is normal. A reviewer who never does it is suspicious.
- **Override rate:** out of every 100 decisions, how many the reviewer changed. It is shown as a percentage.
- **Outlier:** someone whose numbers are far away from everyone else's.
- **Duplicate case:** the same case, secretly given to the same reviewer twice on different days, to see whether they decide it the same way both times.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `3.1 Reviewer Metrics and Anomaly Detection` in the left sidebar.
- Then do Step 1 to Step 8 in the workspace. You do not need to keep this page open while you work.

## What You Will Do in the Workspace

Everything you do in this lab happens in the workspace.

- The workspace has five tabs. Start on the left-most tab and work to the right. You never need to go back to a tab you have finished.
- On each tab, work from top to bottom. Every instruction is in an orange box with a step number, from Step 1 to Step 8. Everything outside the orange boxes is the material you need for that step.
- If a step asks you to answer something, the answer box is inside the orange box.
- Stuck? Each orange box has hints you can open, and most have a **Show the answer** button.
- At the bottom of each tab, click **Go to the next tab** when you have finished every step on it.
- Everything you type saves by itself. The counter at the top right shows how many answers you have filled in.
- Every table opens already grouped the way its step needs. You can still change the **Group by** and **Split by** menus to explore.
<!-- challenge section
- The last tab, Challenges, is optional. It does not count towards the counter.
end challenge section -->

### Tab 1: The Log (Steps 1 and 2)

![The Log tab, showing Step 1 above the reviewer log](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-3-1-1-the-log.png)

You learn what the reviewer log records and what an override is. Then you see why the team's overall override rate cannot prove, on its own, that every reviewer is really checking.

### Tab 2: The Reviewers (Steps 3 to 5)

![The Reviewers tab, showing Step 3 above the override rate for each reviewer](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-3-1-2-the-reviewers.png)

You spot the reviewer who almost never disagrees with PolicyPal and rule out the innocent explanation, that they just had easy cases. Then you spot the reviewer who disagrees the most, and work out whether it is the reviewer or PolicyPal. Every table opens already broken down the way its step needs.

### Tab 3: Trend and Repeats (Steps 6 and 7)

![The Trend and Repeats tab, showing Step 6 above the override rate for each week](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-3-1-3-trend-and-repeats.png)

You read how the override rate changed week by week and check PolicyPal's quality for the same period, to tell whether the AI or the reviewers changed. Then you check the secret repeat cases to see who decided the same case two different ways.

### Tab 4: Next Step (Step 8)

![The Next Step tab, showing Step 8 above the student's earlier answers about R-A](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-3-1-4-next-step.png)

You decide who owns fixing the most serious finding. Lab 3.2 is where you write the plan.

### Tab 5: My Findings

![The My Findings tab, showing the findings built from the student's answers](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-3-1-5-my-findings.png)

You do not type anything here. This tab gathers your answers into one set of findings. Anything you missed says which step to go back to. Click **Save as PDF** if you want a copy.

<!-- challenge section
### Tab 6: Challenges (optional, Steps 9 to 11)

![The Challenges tab, showing the Bronze challenge above the override rate for each reviewer](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-3-1-6-challenges.png)

Three extra challenges for anyone who finishes early:

- **Bronze:** work out the overall rate with R-A left out.
- **Silver:** find the reviewer whose own rate is climbing week by week.
- **Gold:** suggest one number to watch every week that would have shown the rise earlier.
end challenge section -->

## Conclusion

In this lab you saw why a team's overall override rate proves little on its own, broke the numbers down by reviewer, case type and week, flagged one reviewer who almost never disagrees and one who disagrees far more than the rest, ruled out the innocent explanations before naming either, checked a rising trend against the AI's own quality, and routed the most serious finding to the owner of the review process. The metrics point you to who to examine and what to check next; they do not hand you a verdict. This is how you check whether human oversight of an AI workflow is doing real work.
