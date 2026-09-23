# The Auditor's Read

## Lab Objective

**Read an evidence packet the way an auditor would and write up its defects, ranked by severity.**

Knowing what auditors expect is tested by whether you can spot its absence, not by whether you can recite the list. In this lab you receive a completed evidence packet submitted by someone else. It looks competent. It has three real defects: a component that is there in name only because the substance that should fill it is missing, quality scores that cannot be interpreted, and evidence that will not survive its own retention requirement. You find them, explain why each one matters to an auditor, say what would fix it, and rank them.

In this lab, you will:
- Check a packet section by section against the six required components
- Identify a component present in name only, uninterpretable scores, and a retention failure
- Explain why platform-only retention fails a multi-year requirement
- Write three findings and rank them by severity

By the end of this lab you will be able to review an AI evidence packet against what an auditor actually needs.

## In Plain Words

- **What you are doing:** This time you are the auditor. Someone else has built an evidence packet, and it looks good at first glance. You will read it like someone who does not trust it yet, and write down what is wrong.
- **Why it matters:** The best way to learn what a good packet needs is to spot what a bad one is missing. Noticing what is absent is much harder than noticing what is there.
- **You do not have to:** download anything, open a spreadsheet, or fix the packet. You only read it and write down the problems. Nearly everything is a drop-down menu, and everything you type saves by itself.
- **If you feel lost:** every tab starts with a blue box that says what the tab is and what to do there. Read that box first.

**Words you will see in this lab**
- **Auditor:** a person whose job is to check that a company really did what it says it did.
- **Finding:** a problem that an auditor writes down. A good finding says what is wrong, why it matters, and what would fix it.
- **Severity:** how serious a problem is. You rank your findings from the worst to the least bad.
- **Retention:** where the company keeps its records, and for how long.
- **Quality standard:** the rulebook that a quality score was marked against. A score means nothing without it.

## Resources

- If you haven't already done so, click the `WEB PORTS` dropdown in your classroom environment. From that menu click `aux1:2224`.
- On the page that opens in your browser, click `5.2 The Auditor's Read` in the left sidebar.

## Procedure

1. **Read the packet, all the way through.** Do not judge anything yet. The question an auditor asks is not "is this neat?". It is "is there enough here to believe that the company really watched over its AI?"
    - Click the tab called `Submitted Packet`. It is probably already open.
    - Read the whole packet from top to bottom.

0. **Check each of the six sections.** Every packet must have six sections. A section can look fine because it has a heading and an entry, and still fail to prove what the section is for.
    - Click the `Auditor Findings` tab.
    - In the section **Check each of the six required components**, use the drop-down next to each one.
    - Pick **Present in substance** if it really proves what it should. Pick **Present in name only** if it is there but does not prove it. Pick **Missing** if it is not there at all.

    <details><summary>ANSWER:</summary>

    Sections 1, 2, 5, and 6 are present in substance. Sections 3 and 4 are present in name only. Section 3 gives a quality score that nobody can interpret, and section 4 gives numbers for the reviewers but no judgement on whether they were doing their job.

    </details>

0. **Find the first problem.** Section 4 is about whether the human checking was real. Ask what in that section tells an auditor that the checkers were doing their job properly.
    - Click the `Auditor Findings` tab.
    - In the section **Finding 1**, use the drop-down to pick where in the packet the problem is.
    - In the box below, write what is wrong, why an auditor would care, and what would fix it.

    <details><summary>Hint 1: where to look</summary>

    Look again at section 4. It gives override rates for each reviewer. Ask: what in that section tells an auditor whether the reviewers themselves are doing real checking?

    </details>

    <details><summary>Hint 2: a sentence to start from</summary>

    Fill in the blanks: "Section ______ gives ______ but contains no ______, so an auditor cannot tell whether ______. Fix: add ______."

    </details>

    <details><summary>ANSWER:</summary>

    Section 4 gives override rates for each reviewer but has no assessment of the reviewers themselves. Nothing tells the auditor whether the reviewers are really checking. The table of rates does not show that anyone looked into R-A's 2%. The fix is to add the assessment of the reviewers.

    </details>

0. **Look at the quality score.** Section 3 has a Business Quality Score. A number by itself only means something if you know what it was measured against.
    - Click the `Submitted Packet` tab and find the entry in section 3.
    - Ask: can I tell what this number means?

0. **Find the second problem.** The score has no rulebook attached to it. Nothing in the packet says which standard it was marked against, and there is no version, no list of rules, and no link.
    - Click the `Auditor Findings` tab.
    - In the section **Finding 2**, use the drop-down to pick where in the packet the problem is.
    - In the box below, write what is wrong, why an auditor would care, and what would fix it.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "The Business Quality Score of ______ has no ______ attached, so an auditor cannot tell what it ______. Fix: attach ______."

    </details>

    <details><summary>ANSWER:</summary>

    "Business Quality Score: 82" means nothing unless you know the rulebook it was marked against. A different rulebook would give a different number. The fix is to attach the quality standard, with its version.

    </details>

0. **Look at where the records are kept.** Records need to be kept somewhere that will still exist when an auditor comes. The packet has a column that says where each paper is kept.
    - Click the `Submitted Packet` tab.
    - Look at the last column of the packet, the one about where each item is kept. Read it for every row.

0. **Find the third problem.** Several papers are recorded as being kept inside the AI platform itself. The AI platforms only keep their records for about 180 days, and then they delete them.
    - Click the `Auditor Findings` tab.
    - In the section **Finding 3**, use the drop-down to pick where in the packet the problem is.
    - In the box below, write what is wrong, why an auditor would care, and what would fix it.
    - Link it to how long records must be kept.

    <details><summary>Hint 1: a sentence to start from</summary>

    Fill in the blanks: "______ of ______ index rows are retained in ______, which keeps only about ______ days, so the evidence is ______. Fix: ______."

    </details>

    <details><summary>ANSWER:</summary>

    Four of the nine rows say the papers are kept in "Copilot audit log" or "Purview". Those are parts of the AI platform itself, and they keep about 180 days of records. If a company has to keep records for several years, this evidence is gone in about seven months, and the packet cannot be rebuilt when it is really needed. The fix is to copy the evidence into a named system that belongs to the company.

    </details>

0. **Say which problem is the worst.** You have found three problems. Some can be fixed on paper, and some cannot be undone. The unfixable one is the most serious.
    - Click the `Auditor Findings` tab.
    - In the section **Rank by severity**, use the drop-down to pick the worst finding.

    <details><summary>ANSWER:</summary>

    The records problem is probably the worst. The other two can be fixed by writing something down, but this evidence will really disappear.

    </details>

0. **Decide whether you would accept the packet.** An auditor's job is to give a clear answer. You either accept it, or you do not accept it yet.
    - In the section **Your decision**, use the drop-down to pick your answer.
    - In the box below, write one line saying why, and what it still needs.

    <details><summary>ANSWER:</summary>

    No, do not accept it yet. It needs the assessment of the reviewers, the quality standard, and copies of the evidence kept somewhere that will last.

    </details>

0. **Check that you have finished.** The workspace keeps count of the boxes you have filled in.
    - Look at the top right of the workspace. It says something like `X of Y answers filled in`.
    - When X is the same as Y, you are done.
    - Your answers save automatically as you type, so there is nothing to save or send.
    - If you would like a copy for yourself, click the `Save as PDF` button on the `Auditor Findings` tab.

## Challenges

These are optional. Your answers to them are saved on the `Challenges` tab.

**🥉 Bronze:** There is a fourth, smaller weakness. The packet says it covers April to September 2026, but look at what actually proves each part of that time. There is one marked sample, from April to June, and all the incidents are from July onwards. A tool that is reviewed once a month should have many more review records than this over six months. Work out how many it should have, and how many this packet has. Write the finding, and say why it is less serious than the three main ones.

**🥈 Silver:** For each of your three findings, say which of the six sections it belongs to and which of an auditor's questions it fails to answer.

**🥇 Gold:** Rewrite your findings as a one-page memo from an auditor. It should say what is wrong, how serious it is, what you recommend, and have a line for the company's reply.

## Conclusion

In this lab you read a peer's evidence packet as an auditor, found a component present in name only, uninterpretable quality scores, and evidence that will not survive its own retention requirement, and wrote defensible findings ranked by severity. Spotting what is absent is the real test of knowing what auditors expect.
