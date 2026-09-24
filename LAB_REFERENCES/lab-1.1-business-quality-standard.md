# Set the Business Quality Standard for a Deployed AI Workflow

## Lab Objective

**Take operational ownership of a deployed AI workflow and write the business quality standard that every later review will measure against.**

An AI workflow called PolicyPal is already running in production, answering employee HR policy questions, and today it becomes yours. Before you can tell whether it is doing a good job, you need three things: an understanding of what you have been handed, a clear split between the problems you own and the problems the platform team owns, and a written standard for what a good answer looks like. This lab walks through all three in the order you would actually do them on the day a workflow transfers to you. The standard you produce here is the yardstick for every measurement in the rest of the course.

In this lab, you will:
- Read a workflow intake record and identify its assigned risk tier, review cadence, and baseline sample size
- Sort a list of open issues into the ones you own and the ones the platform team owns
- Justify the ownership of two borderline issues
- Write a five-part business quality standard precise enough for a colleague to apply

By the end of this lab you will be able to produce a business quality standard for any AI workflow you are handed.

## In Plain Words

- **What you are doing:** A company has just handed you an AI assistant called PolicyPal and said "this is yours now". You will get to know it, sort out which of its problems are yours to fix, and then write the rulebook that says what a good answer from PolicyPal looks like.
- **Why it matters:** You cannot check whether something is doing a good job until you have written down what "a good job" means. This rulebook is what every later check in the course is measured against.
- **You do not have to:** download anything, open a spreadsheet, or worry about saving. Everything you need is in the workspace, and everything you type saves by itself.
- **If you feel lost:** in the workspace, every instruction is in a numbered orange box. Do the boxes in order, from the left-most tab to the right-most tab.

**Words you will see in this lab**
- **Business AI Owner:** that is you. The person on the business side who is responsible for whether the AI's answers are good enough.
- **Risk tier:** a rating (Low, Medium or High) of how much could go wrong with an AI tool. Someone else decides it. You only read it.
- **Review cadence:** how often the AI must be checked. Riskier tools are checked more often.
- **Baseline sample size:** how many of the AI's answers you must check each time.
- **Business Quality Standard:** the rulebook you will write. It says what a good answer looks like and what must never happen.
- **Platform team:** the technical people who run the computers and software behind the AI.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `1.1 Set the Business Quality Standard` in the left sidebar.
- Read the Required Reading section below first. Then do Step 1 to Step 9 in the workspace.

## Required Reading

![PolicyPal answering an employee's HR policy question in a chat window](https://static.alta3.com/courses/ai-governance/policypal-chat.png)

Read this before you start the procedure. Every lab in this course uses PolicyPal as its example, so what you read here applies all day.

**What PolicyPal is.** PolicyPal is a chat assistant that employees use to ask questions about HR policy. An employee types a question, such as "How many PTO days do I accrue in my second year?" or "What is the mileage reimbursement rate?", and PolicyPal replies with an answer and names the policy document it came from. It runs inside Microsoft Copilot, and about 1,900 employees use it each month.

**What it is for.** PolicyPal gives employees a fast, consistent answer to one question: "What does our policy say?" It covers five topics: paid time off (PTO), benefits, expenses, travel, and conduct. Employees get an answer in seconds instead of searching through policy documents or waiting on someone in HR.

**Where its answers come from.** PolicyPal reads only the HR Policy Library, the company's collection of official HR policy documents. It has no rules of its own. It repeats what those documents say, so if the library still holds an out-of-date document, PolicyPal can repeat the out-of-date rule.

**Who is involved.**
- **You** are the Business AI Owner. As of today, you are responsible for whether PolicyPal's answers are good enough for the business: correct, current, and appropriately cautious.
- **The platform team** runs the technology behind it, such as the AI model, sign-in, and system speed.
- **Five HR operations reviewers** spot-check answers that have been flagged. In Module 3 you will look at how well they do that job.

**Why it needs an owner.** PolicyPal is not broken on the day it launches. Problems show up later: an old policy stays in the library and keeps getting quoted, a vendor changes the AI model and the answers get vaguer, or a sensitive question gets answered when it should have gone to a person. Nothing raises an alarm when this happens, so someone has to be checking. That is the job you are taking over today.

## What You Will Do in the Workspace

Everything you do in this lab happens in the workspace. You do not need to keep this page open while you work.

- The workspace has four tabs. Start on the left-most tab and work to the right. You never need to go back to a tab you have finished.
- On each tab, work from top to bottom. Every instruction is in an orange box with a step number, from Step 1 to Step 9. Everything outside the orange boxes is the material you need for that step.
- If a step asks you to answer something, the answer box is inside the orange box.
- Stuck? Each orange box has hints you can open, and some have a **Show the answer** button.
- At the bottom of each tab, click **Go to the next tab** when you have finished every step on it.
- Everything you type saves by itself. The counter at the top right shows how many answers you have filled in.

### Tab 1: PolicyPal Basics (Steps 1 and 2)

![The PolicyPal Basics tab, showing Step 1 in an orange box above PolicyPal's intake record](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-1-1-1-policypal-basics.png)

You read PolicyPal's intake record, the fact sheet the previous owner left you. You write one sentence saying what PolicyPal is for. Then you look up its risk tier, and use the tier to find how often PolicyPal must be checked and how many of its answers to check each time.

### Tab 2: Open Issues (Steps 3 and 4)

![The Open Issues tab, showing Step 3 above the list of eight problems, each with an Owner drop-down](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-1-1-2-open-issues.png)

You read eight problems people have reported with PolicyPal. For each one, you choose who owns it: you, or the platform team. Then you explain the two choices that were hardest to make.

### Tab 3: Write the Standard (Steps 5 to 9)

![The Write the Standard tab, showing Step 5 above the two problems it asks about](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-1-1-3-write-the-standard.png)

You write the rulebook, one part per step. Each step shows the one or two problems it is about, right under the step. You write what a correct answer looks like, the rules PolicyPal must always follow, the errors that are never acceptable, when a person must take over, and how much two answers to the same question may differ.

### Tab 4: My Answer

![The My Answer tab, showing the finished Business Quality Standard built from the student's answers](https://static.alta3.com/courses/ai-governance/screenshots/LAB_REFERENCES-images-lab-1-1-4-my-answer.png)

You do not type anything here. This tab builds your finished Business Quality Standard from the answers you gave in the steps. Anything you missed says which step to go back to. Click **Save as PDF** if you want a copy.

## Conclusion

In this lab you took operational ownership of a deployed AI workflow, separated the problems you govern from the ones the platform team governs, and wrote a business quality standard precise enough for someone else to apply without asking you a question. That standard is the reference point for every quality audit, reviewer check, and evidence packet in the rest of this course, and it is the first thing to write or locate when any AI workflow becomes your responsibility.
