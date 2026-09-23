# Set the Business Quality Standard for a Deployed AI Workflow

## Lab Objective

**Take operational ownership of a deployed AI workflow and write the business quality standard that every later review will measure against.**

An AI workflow called PolicyPal is already running in production, answering employee HR policy questions, and today it becomes yours. Before you can tell whether it is doing a good job, you need three things: an understanding of what you have been handed, a clear split between the problems you own and the problems the platform team owns, and a written standard for what a good answer looks like. This lab walks through all three in the order you would actually do them on the day a workflow transfers to you. The standard you produce here is the yardstick for every measurement in the rest of the course.

In this lab, you will:
- Read a workflow intake record and identify its assigned risk tier, review cadence, and baseline sample size
- Sort a list of open issues into the ones you own and the ones the platform team owns
- Justify the ownership of two borderline issues
- Write a five-part business quality standard precise enough for a colleague to apply
- Pressure-test the standard from the point of view of someone who has to use it without you

By the end of this lab you will be able to produce a business quality standard for any AI workflow you are handed.

## In Plain Words

- **What you are doing:** A company has just handed you an AI assistant called PolicyPal and said "this is yours now". You will get to know it, sort out which of its problems are yours to fix, and then write the rulebook that says what a good answer from PolicyPal looks like.
- **Why it matters:** You cannot check whether something is doing a good job until you have written down what "a good job" means. This rulebook is what every later check in the course is measured against.
- **You do not have to:** download anything, open a spreadsheet, or worry about saving. Everything you need is in the workspace, and everything you type saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

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

## Procedure

1. **Open the first tab, titled `Intake Record`.** The responsibility for governing the PolicyPal AI application is now yours, and the intake record contains everything the previous owner and the platform team know about it. You cannot look after something until you know the basics about it.
    - Read the `Intake Record` from top to bottom before doing anything else.

0. **Update the Business Quality Standard report.** In this scenario, you are building the documentation required to govern this application properly. The Business Quality Standard report is the first step in that documentation. It describes the purpose, risks, assessment criteria, rules, and standards for the AI tools you are responsible for.
    - Click the `My Answer` tab.
    - In the first field, under `1. Workflow and purpose`, describe PolicyPal's purpose in one sentence. See the **Required Reading** section above for context.

    <details><summary>Unsure? Click here for an example answer.</summary>

    `PolicyPal answers employee questions about company HR policy (PTO, benefits, expense, travel, conduct), grounded on the HR Policy Library.`

    </details>

0. **Find the risk tier, review cadence, and baseline sample size.** You do not assess risk and you do not set the tier; Risk & InfoSec did that with HR before deployment.

    - Open the `Intake Record` tab. Find the **Assigned risk tier** row and note the value.
    - Open the `Review Cadence` tab. Find the row for the tier you just noted. Note how often your team must review this workflow (the review cadence) and how many responses it must score in each baseline review (the baseline sample size).
    - Open the `My Answer` tab. In section **2. Risk tier, review cadence, and sample size**, enter the risk tier, the review cadence, and the baseline sample size.

    <details><summary>ANSWER:</summary>

    - Risk tier: `Medium`
    - Review cadence: `Monthly`
    - Baseline sample size: `20 responses`

    </details>

0. **Review the existing issues with PolicyPal.** Your predecessor has written down a list of problems that need to be dealt with at some point. Some are yours to fix and some are not, and you need to see the whole list before you can tell which.
    - Click the `Open Issues` tab.
    - Read the whole list first, without doing anything else.

0. **Mark each issue as yours or the platform team's.** If you send a problem to the wrong person, nobody fixes it. Next to each issue there is a drop-down. Use it to choose either `Business AI Owner` (you) or `Platform / technical owner` (the technical team). Use these rules to decide:
    - **Business AI Owner:** Choose this if fixing the issue requires changing business rules, content, or a human process.
    - **Platform / technical owner:** Choose this if the issue requires changing infrastructure, the model, or code.

0. **Justify the two issues that look like one owner and are the other.** Some issues are hard to place, because they could belong to either side. Pick the two issues where you found it hardest to decide. Click the `My Answer` tab. In section **2b. Justify the two borderline issues**, write each issue's number and one line explaining what makes your assignment correct.

    <details><summary>Example answers:</summary>

    - Issue 1 (the assistant cites an old policy version) is arguable: the old document sitting in the source is a content problem, but deciding the rule about what the assistant may cite is yours.
    - Issue 8 (users want a new drafting feature) is a build request for whoever owns the agent configuration, not a quality problem.

    </details>

0. **Write what a correct PolicyPal answer looks like.** A correct answer is one a reviewer could mark as pass or fail. Two of the open issues show what goes wrong when the answer is not correct: 
    - **Issue 1** (an old policy version was cited) and **Issue 3** (two employees were given different figures for the same question).
    - Click the `My Answer` tab. In section **3. What a correct answer looks like**, write one criterion that would have caught each issue.
    - Each criterion must be something a reviewer could mark yes or no, not a feeling.

    <details><summary>Hint 1: sentences to start from</summary>

    Fill in the blanks:

    - "The answer cites a ______ policy document."
    - "Every ______ in the answer matches ______."

    </details>

    <details><summary>Hint 2: example answers</summary>

    - "Cites a named, current policy document."
    - "Every claim in the answer matches the entitlement or figure exactly as written in policy."

    </details>

0. **Write the business rules that must always hold.** A rule is an absolute: something the assistant must never do, or must always do.
    - Two open issues point to rules that were missing: **Issue 3** (different per-diem figures) and **Issue 7** (legal detail about maternity leave).
    - In section **4. Business rules that must always hold**, write one rule that would have prevented each issue.

    <details><summary>Hint 1: sentences to start from</summary>

    Fill in the blanks:

    - "Never state a ______ that is not written in ______."
    - "Never give ______ advice; send those questions to ______."

    </details>

    <details><summary>Hint 2: example answers</summary>

    - "Never state a dollar figure or day count that is not written in current policy."
    - "Never give legal or interpretation advice; send those questions to HR."

    </details>

0. **Write the errors that are unacceptable.** An unacceptable error is a failure that is never tolerable, no matter how rarely it happens.
    - **Issue 1** (an old policy version was cited) and **Issue 7** (legal detail about maternity leave) each describe one.
    - In section **5. Errors that are unacceptable**, write the error that each issue shows.

    <details><summary>Hint 1: sentences to start from</summary>

    Fill in the blanks:

    - "Citing a ______ policy as if it were ______."
    - "Answering a ______ question with detail instead of ______."

    </details>

    <details><summary>Hint 2: example answers</summary>

    - "Citing an obsolete policy as if it were current."
    - "Answering a protected or statutory leave question with detail instead of referring it to HR."

    </details>

0. **Write when a human must intervene.** A trigger is a situation where the assistant should stop and route the employee to a person.
    - **Issue 2** (accommodation and protected-leave questions answered directly) and **Issue 1** (an old version of a policy still in the library next to the current one) each point to one.
    - In section **6. When a human must intervene**, write one trigger for each issue.

    <details><summary>Hint 1: sentences to start from</summary>

    Fill in the blanks:

    - "Any question about ______ or ______."
    - "Any question where two ______ of the same policy ______."

    </details>

    <details><summary>Hint 2: example answers</summary>

    - "Any question about an accommodation or leave."
    - "Any question where two versions of a policy conflict, so it is unclear which one is current."

    </details>

0. **State how much inconsistency is tolerable.**
    - **Issue 3** describes two employees who asked the same expense question and got different per-diem figures. Some difference in wording between two answers is normal. A difference in the figure is not.
    - In section **7. Tolerable inconsistency**, write one threshold: how much difference is acceptable between two answers to the same question. State it in plain language or as a percentage.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "Two employees who ask the same ______ must get the same ________."

    </details>

    <details><summary>Hint 2: example answer</summary>

    "Two employees who ask the same question must get the same entitlement figure, every time."

    </details>

0. **Run the colleague test.** A rulebook is only useful if someone else can use it. Imagine a colleague has to use your rulebook tomorrow, and you are on holiday and cannot be asked anything.
    - Scroll back through the whole `My Answer` tab and read your answers as if you had never seen them before.
    - Find any that are vague, meaning two people could read them in different ways.
    - Make them clearer by typing in that box.

0. **Confirm that your standard is complete.** Check the counter at the top of the workspace. It will read `X of Y answers filled in`. Your answers save automatically as you type, so there is nothing to save or submit. This standard is the one that Module 2 scores PolicyPal against and that Module 5 files in the evidence packet. If you want a copy to keep, click `Save as PDF` on the `My Answer` tab.

## Conclusion

In this lab you took operational ownership of a deployed AI workflow, separated the problems you govern from the ones the platform team governs, and wrote a business quality standard precise enough for someone else to apply without asking you a question. That standard is the reference point for every quality audit, reviewer check, and evidence packet in the rest of this course, and it is the first thing to write or locate when any AI workflow becomes your responsibility.
