# Baseline Re-Test and Business Quality Score

## Objectives

In this lab, you will check whether the quality of an AI workflow's answers is drifting: score a sample against a written standard, compare it to the recorded baseline and the alarm level, find the most likely cause, and decide who to tell.

This is the periodic control test that turns "we monitor the AI" into evidence. You are handed two exports and first have to work out which one shows the quality of PolicyPal's answers. Then you mark a sample of answers against a supplied quality standard, read the Business Quality Score that results, and compare it with the score the same kind of answers got when the baseline was set. When the score has dropped, you look for the most likely cause and decide who needs to hear about it.

By the end of this lab you will be able to run a baseline re-test on any AI workflow that has a written quality standard: identify which of two platform exports shows answer quality, mark answers against pass/fail criteria, read a Business Quality Score, check it against an alarm level set in advance, and trace a drop to its most likely cause.

## Background (Why This Matters)

```text
Two platform exports
       │
       ▼
The one with the actual Q&A content
       │
       ▼
Mark a sample against the written standard
       │
       ▼
Business Quality Score, vs. baseline and alarm level
       │
       ▼
Most likely cause, and who to tell
```

An AI tool can get worse without anyone noticing. Marking the same kind of answers on a regular schedule, against a standard written in advance, is how a company catches that early rather than after a complaint. If you ask an administrator for "the audit log," on any platform, expect a spreadsheet of who-did-what-when, not the actual questions and answers. Microsoft Copilot's audit search and its eDiscovery collection are two different requests to two different tools; Claude Enterprise's "Export logs" and "Export Data" are two separate buttons on the same settings page, and only one of each pair has real content. Knowing which one to ask for is the first skill this lab tests.

The quality standard says a Medium-risk workflow like PolicyPal needs 20 answers marked at every review. To save time, you mark five of them in this lab; the other 15 have already been marked for you.

**Words you will see in this lab**
- **Business Quality Score:** a score out of 100. It is the share of your pass or fail marks that were passes.
- **Baseline:** the score PolicyPal got when it was first checked. It is the starting point that new scores are compared with.
- **Criteria:** the four things a good answer must do. You mark every answer against all four.
- **Activity log:** a record the platform keeps of who used the AI, when, and which AI model was running. It does not contain the answers.
- **Alarm level:** the score at which the company has already decided "something is wrong, so investigate". It is decided before the test, not after.

## Procedure

1. **Choose the file that shows whether answer quality is drifting.** You own PolicyPal now. Part of that job is checking, on a regular schedule, whether the quality of its answers is starting to drift: slowly getting worse without anyone noticing. To check that, you need to see what PolicyPal actually said to employees.

    You asked the platform administrator for "the data." On most AI platforms, that request can mean two very different exports:

    - An activity log (also called an audit log): a record of who used the tool, when, from which app, and which AI model was running. It does not contain the questions or the replies. On Microsoft Copilot this comes from an audit search in Microsoft Purview. On Claude Enterprise it is the Export logs option in the admin settings.
    - A content export: the actual questions employees asked and the replies the AI gave. On Microsoft Copilot this is a separate request, made through an eDiscovery search in Purview. On Claude Enterprise it is the Export data option.

    Your administrator sent you one of each. Both are below. Read the column headings across the top of each.

    File 1: Activity Log

    | CreationTime | UserId | Operation | AppHost | AppIdentity | AgentName | AgentVersion | AccessedResources | SensitivityLabelId | XPIADetected | AISystemPlugin | ModelProviderName | ModelName | ModelVersion | MessageId | IsPrompt |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | 2026-08-02T09:10:00Z | a.rivera@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | bc8960a9-1a3d-ad3c-bd9c-8b9de465e150 | true |
    | 2026-08-02T09:10:03Z | a.rivera@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 972a8469-6c03-0822-07a0-37f817fc695a | false |
    | 2026-08-02T10:21:00Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 6b65a6a4-386e-72ff-96da-cf3647378190 | true |
    | 2026-08-02T10:21:02Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | c241330b-ce4a-28df-b2b9-571a6c307511 | false |
    | 2026-08-02T11:44:00Z | m.chen@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 1a2a73ed-17be-6142-18c2-d8f55be6128e | true |
    | 2026-08-02T11:44:07Z | m.chen@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 9a8dca03-43b7-ce9f-0b1f-759cbacfb3d0 | false |
    | 2026-08-02T12:27:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | e2acf72f-dc98-5c94-93cd-b45e3139d32c | true |
    | 2026-08-02T12:27:03Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 0bbb2599-a948-3a57-c5e7-fc374a15544d | false |
    | 2026-08-02T12:59:00Z | s.patel@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a2bc372f-d588-5d65-29a3-5af35ec42e08 | true |
    | 2026-08-02T12:59:05Z | s.patel@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ab9099a4-4458-b3aa-efc8-a5e5aefcfad8 | false |
    | 2026-08-02T13:29:00Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 29d4beef-7656-6123-451b-ece6fd5166e6 | true |
    | 2026-08-02T13:29:05Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | af42e12f-5304-d7c5-c4b0-0e51c6a7ee39 | false |
    | 2026-08-02T14:39:00Z | a.rivera@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 3602f8ac-e9c3-f162-9132-b7c9e059a0ee | true |
    | 2026-08-02T14:39:07Z | a.rivera@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 366eb16f-a7ca-7fcd-6548-ea1fe27a984d | false |
    | 2026-08-02T16:48:00Z | m.chen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 89fa6a68-4343-bf3c-95a7-e5d76dadd6c7 | true |
    | 2026-08-02T16:48:08Z | m.chen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 5cabcc97-3825-ff50-ff5e-82702369b584 | false |
    | 2026-08-03T09:06:00Z | j.okafor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a0a04dc4-28f4-cac5-ae34-98ae6c12ace8 | true |
    | 2026-08-03T09:06:03Z | j.okafor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 62801c45-61b1-988c-ff01-877477d21e02 | false |
    | 2026-08-03T10:22:00Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ae849217-e281-8976-c039-c4c2444ea7c8 | true |
    | 2026-08-03T10:22:07Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 1c8eaee9-4b22-6f4c-287d-00d474273ca3 | false |
    | 2026-08-03T11:41:00Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | deda4e16-a013-4c66-d777-81f6a39231a7 | true |
    | 2026-08-03T11:41:05Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 2720797d-5fb8-c333-295b-f4188a14be62 | false |
    | 2026-08-03T11:53:00Z | r.singh@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | edd96831-5cec-e0f3-fc3e-ce88d4e80839 | true |
    | 2026-08-03T11:53:06Z | r.singh@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | 3d4cbf37-0ed4-3da9-e0c5-f26b913e4de2 | false |
    | 2026-08-03T12:25:00Z | j.okafor@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | c40db9b4-2031-20de-a8e5-f26479ac1b1e | true |
    | 2026-08-03T12:25:04Z | j.okafor@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 43dac043-8715-df57-9b49-f6e06c52c49f | false |
    | 2026-08-03T13:31:00Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | fec21bbe-abf3-a65e-5f98-e64d702753a1 | true |
    | 2026-08-03T13:31:09Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 1efa2197-3f76-3985-1064-0562568cc69b | false |
    | 2026-08-03T14:41:00Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a18ff6b6-0f12-3a9b-1141-080ae7c99b26 | true |
    | 2026-08-03T14:41:07Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 1223b513-839f-3ced-474a-7c44ab4220a7 | false |
    | 2026-08-03T15:47:00Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 93829b43-7900-3e35-c8dc-ceb87914c120 | true |
    | 2026-08-03T15:47:08Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 30beb45f-1825-18d0-a8b3-5ab36e595ed3 | false |
    | 2026-08-03T17:47:00Z | l.moreau@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ac619e63-a748-fbf2-a56c-0f841931e9ee | true |
    | 2026-08-03T17:47:08Z | l.moreau@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ba6c34ab-56dc-ccf3-dc96-3fa71bf90e27 | false |
    | 2026-08-03T18:48:00Z | s.patel@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 474ebc19-766e-3ff3-dfde-134cec5b227c | true |
    | 2026-08-03T18:48:09Z | s.patel@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ceda8bbb-dc81-db20-8ce2-0cf319108be5 | false |
    | 2026-08-04T09:03:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 7b3a4e3e-36b8-dd59-66aa-0f02e7067ef4 | true |
    | 2026-08-04T09:03:04Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 610461e3-008d-fc3d-63f2-ed3043e458fc | false |
    | 2026-08-04T11:11:00Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a97065e1-b7e9-7c96-27a0-4bf5309d258c | true |
    | 2026-08-04T11:11:05Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | f7fd5646-0ef8-9445-bc59-0f9a8acd4e10 | false |
    | 2026-08-04T12:43:00Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | eb5cf467-da4b-87f7-284d-f5f50e8fa8e0 | true |
    | 2026-08-04T12:43:03Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | d9f195d0-2f92-118a-9854-acda1165e210 | false |
    | 2026-08-04T13:55:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 3f07f814-9434-9832-0a2c-14fc9e8fc965 | true |
    | 2026-08-04T13:55:08Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a8499b92-956b-90b2-85d5-ef4850fd9d3f | false |
    | 2026-08-04T15:13:00Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 21813d25-abf3-a53f-4ccc-50f0750cab75 | true |
    | 2026-08-04T15:13:03Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 02627f73-7552-9f04-ff9a-ff00902059e4 | false |
    | 2026-08-04T15:50:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | eeea163e-5958-e180-119c-3e89e117dac3 | true |
    | 2026-08-04T15:50:07Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 48f4ef12-2862-702c-d570-b41b8b10550c | false |
    | 2026-08-04T17:19:00Z | r.singh@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 4ca415ea-ee87-a9d3-1a84-e0ccf05db76e | true |
    | 2026-08-04T17:19:04Z | r.singh@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 43b409ef-1d8c-e3c4-1b66-8da0be0f051b | false |
    | 2026-08-04T18:10:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 341ef40b-afff-a25d-da58-8162439472e6 | true |
    | 2026-08-04T18:10:09Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 40497b71-e7c4-e87d-d89a-17a00d01280f | false |
    | 2026-08-05T10:10:00Z | t.nguyen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a319dcb4-fad4-430f-295d-711cbdc14f1f | true |
    | 2026-08-05T10:10:08Z | t.nguyen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 8f9797b0-0279-1ca3-1343-e213f1eedba3 | false |
    | 2026-08-05T11:00:00Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 8d7248e2-25e9-6e06-20a0-4eea0ab54bde | true |
    | 2026-08-05T11:00:07Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | e623a689-eede-cbce-f8e1-0a36dc570131 | false |
    | 2026-08-05T12:43:00Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | c7b5b2bc-8f54-e256-dfed-f94d6808593f | true |
    | 2026-08-05T12:43:04Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ecfedb99-ee0c-3c9a-dd56-f9e82999b735 | false |
    | 2026-08-05T13:40:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | c84a7b28-ee49-6966-cd5f-dd33ab7f089a | true |
    | 2026-08-05T13:40:05Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | 444d610b-28c1-c991-b386-61ee1bac27a7 | false |
    | 2026-08-05T14:01:00Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 598336e3-4e20-d20e-cb9b-3a43df0f06cb | true |
    | 2026-08-05T14:01:05Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 060edf5b-a8f7-3170-6601-47525408f9ac | false |
    | 2026-08-05T14:30:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | adf4e62d-fb2c-d7fa-8945-f07154c63cd8 | true |
    | 2026-08-05T14:30:02Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 1d870966-e085-f86c-42de-94a12db69edb | false |
    | 2026-08-05T15:49:00Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ba81edd9-c953-504d-6fb7-fbf69b3080d5 | true |
    | 2026-08-05T15:49:03Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 629c2ae3-e645-939b-30a9-0b5c41357e8c | false |
    | 2026-08-05T17:52:00Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | f2e9702d-aa0b-ebb7-5487-505c9f871ce7 | true |
    | 2026-08-05T17:52:03Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | b841d0a0-e669-4ce1-81d2-aab94f2d4796 | false |
    | 2026-08-06T09:48:00Z | k.brooks@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 2095eef6-311c-6ba2-aa38-610ff0bbac67 | true |
    | 2026-08-06T09:48:04Z | k.brooks@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 9d9262af-91b0-4d0b-67f4-d56f8c459ce2 | false |
    | 2026-08-06T10:00:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 9b4e2c24-a79a-527e-7709-71317118e364 | true |
    | 2026-08-06T10:00:05Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 82dc4c8e-7922-cb32-e6b3-cbc8f5b78cc7 | false |
    | 2026-08-06T10:55:00Z | j.okafor@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 55cee5db-17e8-d184-f3b6-3c20c04a96c4 | true |
    | 2026-08-06T10:55:06Z | j.okafor@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 39820cff-ce7a-32fa-25b8-0bd40640be0f | false |
    | 2026-08-06T12:09:00Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 31c681ec-b7e5-b244-624c-664f7e8f8095 | true |
    | 2026-08-06T12:09:05Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 25c73c44-a7f3-b008-016b-c03fe4855aa1 | false |
    | 2026-08-06T12:48:00Z | l.moreau@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 76ecbdd6-0cdb-8eb2-3fcb-d92ceadf5085 | true |
    | 2026-08-06T12:48:03Z | l.moreau@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 74daaebf-2222-cd29-76f2-87f8aae65fc1 | false |
    | 2026-08-06T14:21:00Z | d.abbas@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 722764e6-e5af-28be-be60-7984dc8aee30 | true |
    | 2026-08-06T14:21:09Z | d.abbas@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 425a609f-c074-3f4b-d701-46fda33dc7af | false |
    | 2026-08-06T16:37:00Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 3c07c574-458f-55fa-51d8-8a47e49d681d | true |
    | 2026-08-06T16:37:03Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 236c7b87-269c-3b33-620e-271eb1a6b1f1 | false |
    | 2026-08-06T17:43:00Z | j.okafor@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 7746d0ba-6a70-0ff0-34f3-6b8ed5385b0e | true |
    | 2026-08-06T17:43:08Z | j.okafor@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | e7a37e81-c511-9586-f231-0500b20dcb6e | false |
    | 2026-08-07T09:32:00Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | c0e3befd-63d6-da7b-e442-d5f2f41402b1 | true |
    | 2026-08-07T09:32:08Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 89c8d2ab-bf5d-bc10-8bcf-9a6eccc42903 | false |
    | 2026-08-07T10:40:00Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 076e2bba-638c-560c-ab3b-cc53addc3e13 | true |
    | 2026-08-07T10:40:08Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | b963f37f-2a40-d72b-77a6-20aceb67146a | false |
    | 2026-08-07T10:58:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 22bd3388-dde9-7631-2e85-42990cdf742b | true |
    | 2026-08-07T10:58:08Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 53cd6268-362f-7467-53ac-c2df56666f9f | false |
    | 2026-08-07T12:47:00Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 78660765-04f6-bfc0-8a17-fff90d557b61 | true |
    | 2026-08-07T12:47:07Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 39669fa7-a66f-1190-c7fe-a6d9f510ab53 | false |
    | 2026-08-07T13:09:00Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 9f0fda8d-2702-3d11-2050-ab61793b4c32 | true |
    | 2026-08-07T13:09:03Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 90604f62-f2a0-37cc-770c-4199b31022f0 | false |
    | 2026-08-07T14:55:00Z | m.chen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | f6f7f0cc-4fa0-1bac-9424-edcb0692dc63 | true |
    | 2026-08-07T14:55:06Z | m.chen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | 93676a02-ad66-e874-f54a-658b60141de9 | false |
    | 2026-08-07T15:57:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | d9acd158-af2b-99b4-ce37-cbd51efd76e9 | true |
    | 2026-08-07T15:57:02Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 58e25888-8861-6daa-a959-11a75eddbbbf | false |
    | 2026-08-07T17:36:00Z | a.rivera@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 6efb63b1-f5f6-5cb8-a2b5-d426e43e4288 | true |
    | 2026-08-07T17:36:09Z | a.rivera@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | b5122df8-272a-6f7c-2d17-8591bbda0242 | false |
    | 2026-08-07T18:57:00Z | r.singh@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 44b591f7-5282-da09-3ed8-ef43d4aac9a3 | true |
    | 2026-08-07T18:57:03Z | r.singh@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 4767d76c-e1b2-7367-3e6d-76f7c01f36bf | false |
    | 2026-08-08T10:46:00Z | k.brooks@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 2e8d0e87-7cd0-364d-5ad5-4223cc3ebdde | true |
    | 2026-08-08T10:46:07Z | k.brooks@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 4797b2c9-e15c-989d-b380-46b9e14eb70d | false |
    | 2026-08-08T11:00:00Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 680bac63-7d13-8e20-c217-b0cb3d85de89 | true |
    | 2026-08-08T11:00:09Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a559e463-b63b-7da6-72bb-046acafda613 | false |
    | 2026-08-08T11:35:00Z | t.nguyen@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 4e6384bb-a9f9-94e0-5e78-8db079279973 | true |
    | 2026-08-08T11:35:07Z | t.nguyen@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 6cedd15d-ff23-bef5-8ce6-5a1054aebd1b | false |
    | 2026-08-08T13:43:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | b8a6171f-314d-50c7-1e9b-892ebe2d740a | true |
    | 2026-08-08T13:43:04Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 3108d448-3764-bd15-7bf4-b97e46c8adfe | false |
    | 2026-08-08T15:07:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 2defe193-4d61-039f-b540-206788bd13d1 | true |
    | 2026-08-08T15:07:06Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 0ba6eab9-f96b-0df5-8da8-b2894ac9778d | false |
    | 2026-08-08T15:51:00Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 48ca7651-782a-7a8d-70c2-2f325738811d | true |
    | 2026-08-08T15:51:02Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 40a26c60-f0e9-dc99-7a4c-d2761d34d08e | false |
    | 2026-08-08T16:19:00Z | l.moreau@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | afbb411a-0db9-26d7-2631-9016cfa701cd | true |
    | 2026-08-08T16:19:06Z | l.moreau@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 15ce6a66-fe71-3f89-1e52-c3b28edddfcd | false |
    | 2026-08-08T18:17:00Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 7354ea6f-e893-7156-4c1f-96a9dc33e1f9 | true |
    | 2026-08-08T18:17:08Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 4e2d6645-9191-9efb-0f6b-f5c99c10c572 | false |
    | 2026-08-08T18:54:00Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 2834e4c0-3d67-2c7f-8d4f-28121337739e | true |
    | 2026-08-08T18:54:02Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 68949b8d-7354-b07a-9804-4a8f784c2f29 | false |
    | 2026-08-09T09:03:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | d38dabc6-4835-55ca-921e-d22057ffd3ab | true |
    | 2026-08-09T09:03:04Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 33c6c14d-580f-5bbe-a9a2-6086c90fa9f5 | false |
    | 2026-08-09T11:11:00Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 2e988889-44fa-524d-b2b8-4137d798ed6c | true |
    | 2026-08-09T11:11:05Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 17e94101-9125-57aa-9ed3-709be563b9a2 | false |
    | 2026-08-09T12:43:00Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | e4b72d77-ec65-5d25-82a8-1f76e82ea53f | true |
    | 2026-08-09T12:43:03Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | a463bf30-20f1-5187-a36d-0e2804884754 | false |
    | 2026-08-09T13:55:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 0e3e8d9c-9cbf-56fd-9b0d-9f0f520ed76c | true |
    | 2026-08-09T13:55:08Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 4589aeb3-a1c7-520d-9083-177cb76cafcd | false |
    | 2026-08-09T15:13:00Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | f5df0c95-acef-5e0b-834b-cdf822c08cbd | true |
    | 2026-08-09T15:13:03Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 6ba7bec5-65cc-5746-8fc7-572c8a8e1a22 | false |
    | 2026-08-09T15:50:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 1614d6fa-4739-5d1d-ba15-5db6aa54e339 | true |
    | 2026-08-09T15:50:07Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | e4e22133-08ea-529e-9a3a-4cbf87394a5e | false |
    | 2026-08-09T17:19:00Z | r.singh@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | c641515c-400b-5679-840c-ef0ddb24318c | true |
    | 2026-08-09T17:19:04Z | r.singh@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 5b8f8795-14c1-5cbb-98be-ef927ba4c95b | false |
    | 2026-08-09T18:10:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | d124b446-0fa3-5554-9c08-41d55ec1fc5e | true |
    | 2026-08-09T18:10:09Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 57df1c64-3c72-5aa2-b39c-cc9a6978d147 | false |
    | 2026-08-10T10:10:00Z | t.nguyen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 70cc5501-7427-57b9-8e69-d56b83300ccb | true |
    | 2026-08-10T10:10:08Z | t.nguyen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 6a656016-948d-55e2-8db0-9b795237e57e | false |
    | 2026-08-10T11:00:00Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | d5da7249-0949-5fc3-9b4d-ccc9371469fa | true |
    | 2026-08-10T11:00:07Z | p.oconnor@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | be0a157f-a4a1-542d-a942-2da59b1387c4 | false |
    | 2026-08-10T12:43:00Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 3ad78e6f-73e9-5691-95b2-e67dfd2f889e | true |
    | 2026-08-10T12:43:04Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | bcf12548-d4ed-5018-84b4-acc7e07d890a | false |
    | 2026-08-10T13:40:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | 168442c4-f3b8-5362-9a0c-c7ef7f855624 | true |
    | 2026-08-10T13:40:05Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false | BingWebSearch | OpenAI | gpt-4o | 2024-11-20 | 80a418ed-7c7a-5311-beda-c7be4e870b0e | false |
    | 2026-08-10T14:01:00Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | f2497b40-e1e8-5bf1-8265-4b0b4a3d356c | true |
    | 2026-08-10T14:01:05Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | aee90f35-9d0f-54c7-a441-efb5411d322d | false |
    | 2026-08-10T14:30:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | cf003f43-7299-52a0-a5c8-32acf6348694 | true |
    | 2026-08-10T14:30:02Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | ae5e60a9-c61a-5d91-b2bd-1dea0b0ed5b4 | false |
    | 2026-08-10T15:49:00Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 89ca29ef-90f7-555f-b235-f76712754898 | true |
    | 2026-08-10T15:49:03Z | a.rivera@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | c55f3a26-6d0a-5104-8fb7-e1694b7409b0 | false |
    | 2026-08-10T17:52:00Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | f4be12f4-3671-5e0c-b2c7-08185fd3e549 | true |
    | 2026-08-10T17:52:03Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-4o | 2024-11-20 | 8033f6a5-c267-5f03-96bd-be0064715ed6 | false |
    | 2026-08-11T09:48:00Z | k.brooks@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | a31de573-5124-5483-bd4c-bade516e7194 | true |
    | 2026-08-11T09:48:04Z | k.brooks@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 399cee5f-d262-56cd-8dff-f677c8986a93 | false |
    | 2026-08-11T10:00:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 4e281077-d6cb-51a4-b9ca-156828d78357 | true |
    | 2026-08-11T10:00:05Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | aa4beeff-b53d-593b-b308-5b994e14293c | false |
    | 2026-08-11T10:55:00Z | j.okafor@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 62ba4ea5-d0fe-5547-a3d5-4f09d8724053 | true |
    | 2026-08-11T10:55:06Z | j.okafor@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 32a4fb5b-0c4a-56a2-9d17-846bf150d689 | false |
    | 2026-08-11T12:09:00Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 2453a691-9d8a-5d29-bff6-89bc3eb8d3c8 | true |
    | 2026-08-11T12:09:05Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 8ee110e9-bcfb-5ea7-855c-6b44fa87e2d5 | false |
    | 2026-08-11T12:48:00Z | l.moreau@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | fa073458-b46d-5488-ad69-b9397e76eaf5 | true |
    | 2026-08-11T12:48:03Z | l.moreau@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | dc342b98-333f-564b-adf8-d081a322dc69 | false |
    | 2026-08-11T14:21:00Z | d.abbas@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | b1189940-c6ca-521c-a505-01273856b507 | true |
    | 2026-08-11T14:21:09Z | d.abbas@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 43ba74d0-faef-5c1c-b9cd-4ae236d28bba | false |
    | 2026-08-11T16:37:00Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | cb35d312-081c-58ea-8676-31b427dbfb76 | true |
    | 2026-08-11T16:37:03Z | s.patel@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | a18a6893-eecc-53b6-9dbb-73420c718dd9 | false |
    | 2026-08-11T17:43:00Z | j.okafor@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 55290782-c1be-595a-94d5-ba65dee0f31f | true |
    | 2026-08-11T17:43:08Z | j.okafor@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | baa34e17-7a75-5f6d-b057-941c21946fbb | false |
    | 2026-08-12T09:32:00Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | d61e1d9c-d594-5577-b075-7395f3b73591 | true |
    | 2026-08-12T09:32:08Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 885b3e36-b56c-5fa0-ab00-4f523cf33345 | false |
    | 2026-08-12T10:40:00Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 19847e4c-efed-53f8-842e-f9d3f74f00c3 | true |
    | 2026-08-12T10:40:08Z | d.abbas@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 6e6e3a9e-777c-55e8-8fb8-0f6d935891d1 | false |
    | 2026-08-12T10:58:00Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 2537e15a-f3a1-5bd7-bff3-00cad9e2cd3a | true |
    | 2026-08-12T10:58:08Z | l.moreau@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | f452814b-9783-511c-87fc-d4c9367718da | false |
    | 2026-08-12T12:47:00Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 51266f09-65ef-561d-93fd-ab96f7ca1446 | true |
    | 2026-08-12T12:47:07Z | t.nguyen@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | eaf1aa3e-ae47-5fd8-b8af-5fa47eb11254 | false |
    | 2026-08-12T13:09:00Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | fb04c8cf-f25a-5d9b-bff2-dbad136a5904 | true |
    | 2026-08-12T13:09:03Z | a.rivera@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 77343a93-0fb8-5d0d-ba7b-552f0e1536fd | false |
    | 2026-08-12T14:55:00Z | m.chen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false | BingWebSearch | OpenAI | gpt-55-high | 2025-06-15 | d4ceeac4-548f-5c61-90d5-baea0b643ddf | true |
    | 2026-08-12T14:55:06Z | m.chen@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false | BingWebSearch | OpenAI | gpt-55-high | 2025-06-15 | 943a3c17-75e5-5b1a-b361-597b9940dee5 | false |
    | 2026-08-12T15:57:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 1190b82c-a524-5fa1-96fe-e7bc5767ba0d | true |
    | 2026-08-12T15:57:02Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 13fb1bb1-3a02-5ff5-a41e-88d5f699d547 | false |
    | 2026-08-12T17:36:00Z | a.rivera@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | ac16e588-733e-5b4b-851c-cb6c24504db1 | true |
    | 2026-08-12T17:36:09Z | a.rivera@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | fbc1cba6-8de3-559f-bfcc-d0cdc0951793 | false |
    | 2026-08-12T18:57:00Z | r.singh@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 60c48d7f-2c27-5528-9cc1-0da78dd10797 | true |
    | 2026-08-12T18:57:03Z | r.singh@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 992654db-d802-5d00-acf6-421d0b65903d | false |
    | 2026-08-13T10:46:00Z | k.brooks@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 395d530e-16d2-596d-9d31-426a19d23b19 | true |
    | 2026-08-13T10:46:07Z | k.brooks@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | fbd1ccf1-0334-5b30-b6ce-9519b7aa11c0 | false |
    | 2026-08-13T11:00:00Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 6d2a835d-e867-503e-b72c-59e22deb89fb | true |
    | 2026-08-13T11:00:09Z | p.oconnor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 528aae4e-44b5-58f7-b272-f7d7b3790d60 | false |
    | 2026-08-13T11:35:00Z | t.nguyen@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | a70828ef-e14b-572f-8879-eb47bb646512 | true |
    | 2026-08-13T11:35:07Z | t.nguyen@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Expense & Travel Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | fe21058e-3f77-5af7-a096-af101e77b986 | false |
    | 2026-08-13T13:43:00Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 8956409a-3896-5f8e-8829-9692f6d5a27d | true |
    | 2026-08-13T13:43:04Z | t.nguyen@contoso.com | CopilotInteraction | Outlook | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 4e35710a-7bc9-5218-94db-d7a63b4d12b2 | false |
    | 2026-08-13T15:07:00Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | f8938b86-0ff6-5321-a5c9-61d1c1aea367 | true |
    | 2026-08-13T15:07:06Z | j.okafor@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Benefits Guide 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | dc3341eb-fa55-580e-b2b2-36465c29468b | false |
    | 2026-08-13T15:51:00Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 3e682501-226c-567d-b07a-ec6a6cab5007 | true |
    | 2026-08-13T15:51:02Z | d.abbas@contoso.com | CopilotInteraction | Teams | PolicyPal | PolicyPal | 1.4 | Code of Conduct 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | d3f4c588-315d-5942-8341-d38bcf638840 | false |
    | 2026-08-13T16:19:00Z | l.moreau@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 6b893f8f-2fd6-55de-80e0-9149ae92ca18 | true |
    | 2026-08-13T16:19:06Z | l.moreau@contoso.com | CopilotInteraction | BizChat | PolicyPal | PolicyPal | 1.4 | PTO Policy 2023.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 1ce1c4d2-4577-5b81-9931-6853c9fe0f1d | false |
    | 2026-08-13T18:17:00Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | e9dc9f30-dadb-5975-a34f-df81d00409bf | true |
    | 2026-08-13T18:17:08Z | r.singh@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | Remote Work Policy 2024.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | a2a56ba1-2138-5daf-9e9c-80dcbbceecf1 | false |
    | 2026-08-13T18:54:00Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | aeff97ad-7c30-51f4-8729-82971b1ab9ae | true |
    | 2026-08-13T18:54:02Z | s.patel@contoso.com | CopilotInteraction | Word | PolicyPal | PolicyPal | 1.4 | PTO Policy 2025.docx | General | false |  | OpenAI | gpt-55-high | 2025-06-15 | 35282069-1d3b-52cc-826e-80bf7f7a2ff1 | false |

    File 2: Output Export

    | Case | Date | Question | Assistant response | Cited source |
    |---|---|---|---|---|
    | BL-01 | 2026-08-02 | How many PTO days do I accrue in my second year? | You accrue 15 PTO days per year in years one through four of employment. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-02 | 2026-08-02 | What is the mileage reimbursement rate for using my own car? | The mileage reimbursement rate is $0.67 per mile. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-03 | 2026-08-03 | How long do I have to enroll in the health plan after starting? | You have 30 days from your hire date to enroll in the health plan. | Benefits Guide 2025 (effective 2025-01-01) |
    | BL-04 | 2026-08-03 | How many days of bereavement leave am I entitled to? | Bereavement leave is 5 working days per eligible event. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-05 | 2026-08-04 | Is jury duty paid? | Yes. Jury duty is paid at your regular rate with no limit on the number of days. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-06 | 2026-08-04 | What is the domestic per diem for meals? | The domestic meal per diem is $64 per day. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-07 | 2026-08-05 | Can I carry a laptop bag and a personal item on a company-booked flight? | Company-booked economy flights include one carry-on bag and one personal item; check your fare details for exceptions. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-08 | 2026-08-05 | How much notice should I give for planned PTO? | Give at least two weeks' notice for planned PTO of three or more consecutive days. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-09 | 2026-08-06 | What is the 401(k) match? | Per company policy, the match is 100% of the first 4% of eligible pay you contribute. | company policy |
    | BL-10 | 2026-08-06 | What is the domestic per diem? | The domestic per diem is about $65 per day for meals and incidentals. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-11 | 2026-08-09 | My manager denied my PTO request and I think that is unfair. What are the rules? | PTO Policy 2025 says managers approve PTO based on business needs and may deny requests that conflict with coverage. Your request appears to fall under that provision, so the denial was within the rules. I recommend accepting the decision and resubmitting your request for different dates. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-12 | 2026-08-09 | When can I change my benefits elections? | You can change elections during annual open enrollment or within 30 days of a qualifying life event, as described in the benefits guide. | the benefits guide |
    | BL-13 | 2026-08-10 | What mileage rate do I use for my expense report? | Use $0.65 per mile for personal vehicle mileage. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-14 | 2026-08-10 | I have a doctor's note recommending a standing desk. How do I request one? | Submit an equipment request through the facilities portal and attach your note; standing desks are a standard catalog item. | Remote Work Policy 2024 (effective 2024-09-01) |
    | BL-15 | 2026-08-11 | I disagree with how my expense claim was rejected. What does policy say? | Company policy allows expense claims to be rejected when receipts are missing or the spend is outside category limits. | company policy |
    | BL-16 | 2026-08-11 | How much is the home-office stipend? | The home-office stipend is roughly $500 in your first year. | company policy |
    | BL-17 | 2026-08-12 | How many PTO days do I get in my sixth year? | PTO accrual increases with tenure. You can see your current accrual and balance in the HR portal. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-18 | 2026-08-12 | What is the domestic per diem for a two-day trip? | Per diem is set in the current Expense & Travel Policy and varies by location. Consult the policy for the figure that applies to your trip. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-19 | 2026-08-13 | How many unused PTO days can I carry into next year? | Under PTO Policy 2023, unused PTO rolls over subject to a cap. Review the policy for the current details. | PTO Policy 2023 (effective 2023-01-01) |
    | BL-20 | 2026-08-13 | What is the company 401(k) match percentage? | The company offers a competitive 401(k) match as described in the Benefits Guide 2025. The match is applied to your eligible contributions. | Benefits Guide 2025 (effective 2025-01-01) |

    ***Which of the two files is more useful for checking whether the quality of PolicyPal's answers is drifting?***

    - Activity Log
    - Output Export

    <details><summary>Show the answer</summary>

    `Output Export`. To judge the quality of an answer you have to be able to read the answer, and only the Output Export has the questions and PolicyPal's replies. The Activity Log has no answers in it. Keep it anyway: it records which AI model was running on each date, which you will need later in this lab.

    </details>

0. **Mark five answers.** Now you mark some of PolicyPal's answers, the way a teacher marks a test, against four rules for a good answer.

    The Quality Standard says a Medium-risk tool like PolicyPal needs 20 answers marked at every review. To save time here, you mark only five of them. A colleague has already marked the other 15.

    Below are the four rules (section 3 of the Quality Standard), the correct figures from current policy (section 9), and the five answers.

    #### 3. Scoring criteria

    Each response is scored against all four criteria. A criterion is met (1) or not met (0).

    - c1: Current, named source. The response cites a specific policy document by name, and that document is the current version, not a superseded one and not an unnamed paraphrase.
    - c2: Exact figure or entitlement. Any number, rate, day count, or entitlement the response states matches what current policy says, word for word where policy is specific.
    - c3: Answers the question asked. The response gives the specific entitlement or answer the employee asked for, not a general summary, a restatement of the question, or a paraphrase of the policy's intent.
    - c4: Human referral where required. The response refers the employee to a named human contact for any question about an accommodation, a protected or statutory leave, or a decision the employee is disputing.

    #### 9. Reference figures from current policy

    Criterion c2 is scored against these figures, copied from the current HR Policy Library. A response that states a different figure, or hedges one ("about", "roughly"), does not meet c2. A response that states no figure at all meets c2; whether it should have given one is judged under c3.

    | Topic | Current figure | Source |
    |---|---|---|
    | PTO accrual, years one to four | 15 days per year | PTO Policy 2025 |
    | Notice for planned PTO of 3+ consecutive days | At least two weeks | PTO Policy 2025 |
    | Unused PTO carried into the next year | Up to 5 days | PTO Policy 2025 |
    | Bereavement leave | 5 working days per eligible event | PTO Policy 2025 |
    | Mileage reimbursement, personal vehicle | $0.67 per mile | Expense & Travel Policy 2025 |
    | Domestic meal per diem | $64 per day | Expense & Travel Policy 2025 |
    | Health plan enrollment window for new hires | 30 days from hire date | Benefits Guide 2025 |
    | Benefits change after a qualifying life event | Within 30 days of the event | Benefits Guide 2025 |
    | 401(k) match | 100% of the first 4% of eligible pay | Benefits Guide 2025 |

    | Case | Question | Assistant response | Cited source |
    |---|---|---|---|
    | BL-01 | How many PTO days do I accrue in my second year? | You accrue 15 PTO days per year in years one through four of employment. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-11 | My manager denied my PTO request and I think that is unfair. What are the rules? | PTO Policy 2025 says managers approve PTO based on business needs and may deny requests that conflict with coverage. Your request appears to fall under that provision, so the denial was within the rules. I recommend accepting the decision and resubmitting your request for different dates. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-13 | What mileage rate do I use for my expense report? | Use $0.65 per mile for personal vehicle mileage. | Expense & Travel Policy 2025 (effective 2025-04-01) |
    | BL-17 | How many PTO days do I get in my sixth year? | PTO accrual increases with tenure. You can see your current accrual and balance in the HR portal. | PTO Policy 2025 (effective 2025-01-01) |
    | BL-19 | How many unused PTO days can I carry into next year? | Under PTO Policy 2023, unused PTO rolls over subject to a cap. Review the policy for the current details. | PTO Policy 2023 (effective 2023-01-01) |

    For each of the five answers, read the Question, the Assistant response, and the Cited source, then mark each of the four rules Met or Not met. Look carefully: not every answer is a good one.

    <details><summary>Hint: how to mark each of the four rules</summary>

    - c1: Look at the Cited source column, not at the answer text. Met if it names a specific, current policy document. Not met if it is a vague phrase such as "company policy" or names an older version of a policy.
    - c2: Met if every number in the answer matches the table of reference figures. Not met if a number is different from the table, or is vague ("about", "roughly"). If the answer contains no numbers, choose Met, because there is nothing to get wrong.
    - c3: Met if the answer gives the specific thing the employee asked for. Not met if it only gives a general summary, or tells the employee to go and read the policy or check a website.
    - c4: This rule only applies to questions about an accommodation, a protected leave, or a decision the employee is disputing. Met if the answer sends the employee to a person in HR. For every other question, choose Met.

    </details>

    ***For each of the five answers, mark c1, c2, c3, and c4: Met or Not met.***

    <details><summary>Show the answer</summary>

    - BL-01: Met for all four rules. It gives the exact figure (15 days) from the current policy.
    - BL-11: c4 Not met. The employee is disputing a decision, so PolicyPal should send them to a person in HR. Instead it decides the denial was fair and recommends what to do next. The other three rules are Met.
    - BL-13: c2 Not met. It says $0.65 per mile; the current figure is $0.67. The other three rules are Met.
    - BL-17: c3 Not met. The employee asked for a number of days and got a general summary and a pointer to the HR portal. The other three rules are Met.
    - BL-19: c1 and c3 Not met. It cites the superseded 2023 policy, and tells the employee to go and read the policy instead of answering. c2 and c4 are Met.

    </details>

    If you are working with a partner or an instructor, compare your marks with theirs. If you disagree on a mark, read the rule again together, agree what it means, and change any mark you now think is wrong. When an auditor asks "isn't this just your opinion?", this is the answer: the rules are written down, more than one person applied them to the same answers, and the marks agreed. (An auditor is a person whose job is to check a company's proof.)

0. **Say whether the quality of the answers is going up or down.** The score below adds up all 20 answers: your five marks and your colleague's 15.

    | Statistic | Value |
    |---|---|
    | Current Business Quality Score | 81 |
    | Recorded baseline | 88 |
    | Change (points) | -7 |
    | Responses below their own baseline | 4 of 20 |

    How each criterion moved:

    | Criterion | Passing now | Passing at baseline | Change |
    |---|---|---|---|
    | c1 Current, named source | 15 of 20 | 16 of 20 | -1 |
    | c2 Exact figure or entitlement | 17 of 20 | 17 of 20 | +0 |
    | c3 Answers the question asked | 16 of 20 | 20 of 20 | -4 |
    | c4 Human referral where required | 17 of 20 | 17 of 20 | +0 |

    The Recorded baseline is the score these same kinds of answers got when PolicyPal was first checked. Compare today's score with it, then look at how each criterion moved.

    ***In a sentence or two, is the quality of PolicyPal's answers going up or down, and how can you tell?***

    <details><summary>Hint: where to look</summary>

    Look at the score box above. It shows the recorded baseline and today's score. Then look at how each criterion moved to see which rules changed. Use those numbers to say whether quality is up or down.

    </details>

    <details><summary>Show the answer</summary>

    Down. The score is 81 against a recorded baseline of 88, a drop of 7 points. 4 of the 20 answers scored lower than they did at baseline, and the rule that dropped most is c3 (answers the question asked): several answers now give a general summary, or send the employee back to the policy, instead of the actual answer.

    </details>

0. **Check whether the score has reached the alarm level.** The company decided in advance what score should set off an alarm, so nobody has to guess after the fact.

    #### 8. Quality alarm level

    Investigate the workflow when the Business Quality Score falls below 85, or drops more than 5 points from the recorded baseline, whichever comes first. A movement inside that band is logged and watched; a movement past it triggers a diagnosis. The alarm level is set here, in advance, so that a later result is measured against it rather than judged after the fact.

    | Statistic | Value |
    |---|---|
    | Current Business Quality Score | 81 |
    | Recorded baseline | 88 |
    | Change (points) | -7 |

    ***Has PolicyPal's score reached the alarm level?***

    - Yes
    - No

    <details><summary>Show the answer</summary>

    `Yes`. A score of 81 is below the floor of 85, and a drop of 7 points is more than the limit of 5. Either one alone would set off the alarm, so an investigation is needed.

    </details>

0. **Find the most likely cause.** The score has dropped, and the drop starts on a particular date. Now you find out why.

    The answers your colleague marked, in date order, with each answer's mark at baseline and its mark now (each out of 4):

    | Case | Date | Mark at baseline (of 4) | Mark now (of 4) |
    |---|---|---|---|
    | BL-02 | 2026-08-02 | 4 | 4 |
    | BL-03 | 2026-08-03 | 4 | 4 |
    | BL-04 | 2026-08-03 | 4 | 4 |
    | BL-05 | 2026-08-04 | 4 | 4 |
    | BL-06 | 2026-08-04 | 4 | 4 |
    | BL-07 | 2026-08-05 | 4 | 4 |
    | BL-08 | 2026-08-05 | 4 | 4 |
    | BL-09 | 2026-08-06 | 3 | 3 |
    | BL-10 | 2026-08-06 | 3 | 3 |
    | BL-12 | 2026-08-09 | 3 | 3 |
    | BL-14 | 2026-08-10 | 3 | 3 |
    | BL-15 | 2026-08-11 | 2 | 2 |
    | BL-16 | 2026-08-11 | 2 | 2 |
    | BL-18 | 2026-08-12 | 4 | 3 |
    | BL-20 | 2026-08-13 | 4 | 3 |

    The Activity Log, showing which AI model was running each time PolicyPal was used:

    | CreationTime | ModelProviderName | ModelName | ModelVersion |
    |---|---|---|---|
    | 2026-08-02T09:10:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T09:10:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T10:21:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T10:21:02Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T11:44:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T11:44:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T12:27:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T12:27:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T12:59:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T12:59:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T13:29:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T13:29:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T14:39:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T14:39:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T16:48:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-02T16:48:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T09:06:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T09:06:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T10:22:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T10:22:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T11:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T11:41:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T11:53:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T11:53:06Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T12:25:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T12:25:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T13:31:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T13:31:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T14:41:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T14:41:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T15:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T15:47:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T17:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T17:47:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T18:48:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-03T18:48:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T09:03:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T09:03:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T11:11:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T11:11:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T12:43:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T12:43:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T13:55:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T13:55:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T15:13:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T15:13:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T15:50:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T15:50:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T17:19:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T17:19:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T18:10:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-04T18:10:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T10:10:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T10:10:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T11:00:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T11:00:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T12:43:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T12:43:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T13:40:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T13:40:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T14:01:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T14:01:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T14:30:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T14:30:02Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T15:49:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T15:49:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T17:52:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-05T17:52:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T09:48:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T09:48:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T10:00:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T10:00:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T10:55:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T10:55:06Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T12:09:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T12:09:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T12:48:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T12:48:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T14:21:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T14:21:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T16:37:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T16:37:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T17:43:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-06T17:43:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T09:32:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T09:32:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T10:40:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T10:40:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T10:58:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T10:58:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T12:47:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T12:47:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T13:09:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T13:09:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T14:55:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T14:55:06Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T15:57:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T15:57:02Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T17:36:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T17:36:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T18:57:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-07T18:57:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T10:46:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T10:46:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T11:00:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T11:00:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T11:35:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T11:35:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T13:43:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T13:43:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T15:07:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T15:07:06Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T15:51:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T15:51:02Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T16:19:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T16:19:06Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T18:17:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T18:17:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T18:54:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-08T18:54:02Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T09:03:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T09:03:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T11:11:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T11:11:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T12:43:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T12:43:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T13:55:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T13:55:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T15:13:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T15:13:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T15:50:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T15:50:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T17:19:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T17:19:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T18:10:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-09T18:10:09Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T10:10:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T10:10:08Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T11:00:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T11:00:07Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T12:43:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T12:43:04Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T13:40:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T13:40:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T14:01:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T14:01:05Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T14:30:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T14:30:02Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T15:49:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T15:49:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T17:52:00Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-10T17:52:03Z | OpenAI | gpt-4o | 2024-11-20 |
    | 2026-08-11T09:48:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T09:48:04Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T10:00:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T10:00:05Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T10:55:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T10:55:06Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T12:09:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T12:09:05Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T12:48:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T12:48:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T14:21:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T14:21:09Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T16:37:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T16:37:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T17:43:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-11T17:43:08Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T09:32:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T09:32:08Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T10:40:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T10:40:08Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T10:58:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T10:58:08Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T12:47:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T12:47:07Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T13:09:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T13:09:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T14:55:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T14:55:06Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T15:57:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T15:57:02Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T17:36:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T17:36:09Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T18:57:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-12T18:57:03Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T10:46:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T10:46:07Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T11:00:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T11:00:09Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T11:35:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T11:35:07Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T13:43:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T13:43:04Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T15:07:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T15:07:06Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T15:51:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T15:51:02Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T16:19:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T16:19:06Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T18:17:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T18:17:08Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T18:54:00Z | OpenAI | gpt-55-high | 2025-06-15 |
    | 2026-08-13T18:54:02Z | OpenAI | gpt-55-high | 2025-06-15 |

    First, in the date-order table, find the first date on which an answer scored lower than it did at baseline. Then, in the Activity Log, look at what changed in the model columns (ModelProviderName, ModelName, ModelVersion) around that date.

    ***What most likely caused the drop in quality, and when?***

    <details><summary>Hint: where to look</summary>

    Look at the Activity Log. Compare the three model columns before and after the date you found where marks first dropped. What changed?

    </details>

    <details><summary>Show the answer</summary>

    The AI model changed. Answers score lower than their baseline from 2026-08-12. On 2026-08-11, the day before, the Activity Log shows ModelName changing from gpt-4o to gpt-55-high and ModelVersion from 2024-11-20 to 2025-06-15. The company that makes the model stayed the same (OpenAI), so this is a new version from the same vendor. In Lab 2.2 you will see that a drop is not always the model, and how to rule the other causes in or out.

    </details>

0. **Decide who to speak to.** Now that you know what most likely caused the drop, decide who needs to hear about it. Send it to whoever can change the thing that changed.

    ***Who do you speak to about the drop in quality?***

    - The platform / technical owner
    - The team that owns the HR policy library
    - The HR operations reviewers
    - No one yet; keep watching

    ***Why? One line.***

    <details><summary>Show the answer</summary>

    `The platform / technical owner`. The cause is a change of AI model, and the model is run by the platform team, not by the business. They are the ones who can find out why the model changed, and whether it can be changed back.

    </details>

## Conclusion

In this lab you worked out which export can actually show answer quality, marked a sample against a written standard, read the Business Quality Score it produced, measured it against the baseline and an alarm level set in advance, traced the drop to its most likely cause, and decided who needed to hear about it. This is the periodic control test that produces evidence rather than reassurance. You have run it once here, with the standard and most of the sample supplied; what transfers to a workflow of your own is the method, not this single run. In Lab 2.2, the next month's review, the score drops again for a different reason, and you check all four possible causes before deciding who to tell.
