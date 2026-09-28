# Reviewer Metrics and Anomaly Detection

## Objectives

In this lab, you will read a human-review decision log for PolicyPal, an HR assistant, and judge whether the humans who are supposed to be checking its work are really checking it. You will use last quarter's 30-day log of reviewer decisions, broken down by reviewer, case type and week, to find the patterns that a single overall number hides.

By completing this lab, you will be able to explain why an overall override rate can hide a reviewer who is not really checking, flag reviewers whose patterns are anomalously low or high, rule out innocent explanations before naming anyone, tell an AI quality problem apart from a reviewing problem, and route a human-oversight finding to the correct owner.

## Background (Why This Matters)

Companies often say "a human checks the AI's work." That claim is only true if the human review is real. Human review is a control, and controls need monitoring, the same as anything else in the system.

```text
Reviewer decisions
       │
       ▼
Override rate, broken down by reviewer
       │
       ▼
Outliers (too low, too high)
       │
       ▼
Innocent explanations ruled out
       │
       ▼
Finding routed to the right owner
```

A reviewer who approves everything gives you the appearance of oversight with none of the substance. In this lab you see why the team's overall override rate proves little on its own, then break the numbers down by reviewer, by case type and by week until the anomalies become visible. That breakdown is the skill.

**Words you will see in this lab**
- **Flagged case:** an answer PolicyPal was not sure about, held back for a person to check.
- **Reviewer:** a person who checks the AI's work.
- **Override:** when a reviewer disagrees with the AI and does something different. Overriding is normal. A reviewer who never does it is suspicious.
- **Override rate:** out of every 100 decisions, how many the reviewer changed. It is shown as a percentage.
- **Outlier:** someone whose numbers are far away from everyone else's.
- **Duplicate case:** the same case, secretly given to the same reviewer twice on different days, to see whether they decide it the same way both times.

## Procedure

1. **Understand what the review log records.** When PolicyPal gets a question it is not sure about, the answer is flagged for a person to look at. For each flagged case, PolicyPal proposes one of three things:

    - **approve:** send the answer to the employee as it is
    - **reject:** do not send the answer
    - **route-to-human:** pass the question to a person in HR

    One of five HR operations reviewers (`R-A` to `R-E`) then makes the final call. The review tool keeps a log of every decision. Below is its export for last quarter's 30 days, 19 May to 17 June: 212 decisions in all.

    Each row shows what PolicyPal proposed (`ai_decision`), what the reviewer decided (`human_decision`), who the reviewer was, the week, and the type of case. The `override` column on the right has been filled in for you.

    | date | week | case_id | case_type | reviewer | ai_decision | human_decision | override |
    |---|---|---|---|---|---|---|---|
    | 2026-05-19 | W1 | RV-0002 | travel | R-A | approve | approve | 0 |
    | 2026-05-19 | W1 | RV-0008 | travel | R-A | approve | approve | 0 |
    | 2026-05-19 | W1 | RV-0041 | conduct | R-B | route-to-human | approve | 1 |
    | 2026-05-19 | W1 | RV-0043 | travel | R-B | approve | approve | 0 |
    | 2026-05-19 | W1 | RV-0045 | conduct | R-B | route-to-human | route-to-human | 0 |
    | 2026-05-19 | W1 | RV-0050 | expense | R-B | approve | approve | 0 |
    | 2026-05-19 | W1 | RV-0082 | benefits | R-C | approve | approve | 0 |
    | 2026-05-19 | W1 | RV-0121 | travel | R-D | approve | approve | 0 |
    | 2026-05-19 | W1 | RV-0124 | benefits | R-D | reject | reject | 0 |
    | 2026-05-19 | W1 | RV-0164 | travel | R-E | reject | reject | 0 |
    | 2026-05-20 | W1 | RV-0005 | conduct | R-A | approve | approve | 0 |
    | 2026-05-20 | W1 | RV-0049 | benefits | R-B | approve | approve | 0 |
    | 2026-05-20 | W1 | RV-0088 | travel | R-C | approve | approve | 0 |
    | 2026-05-20 | W1 | RV-0126 | pto | R-D | approve | approve | 0 |
    | 2026-05-20 | W1 | RV-0129 | expense | R-D | reject | reject | 0 |
    | 2026-05-20 | W1 | RV-0130 | pto | R-D | reject | reject | 0 |
    | 2026-05-20 | W1 | RV-0165 | pto | R-E | route-to-human | route-to-human | 0 |
    | 2026-05-20 | W1 | RV-0168 | benefits | R-E | approve | approve | 0 |
    | 2026-05-20 | W1 | RV-0169 | conduct | R-E | approve | reject | 1 |
    | 2026-05-21 | W1 | DUP-01a | pto | R-A | approve | approve | 0 |
    | 2026-05-21 | W1 | RV-0003 | benefits | R-A | approve | approve | 0 |
    | 2026-05-21 | W1 | RV-0006 | conduct | R-A | route-to-human | route-to-human | 0 |
    | 2026-05-21 | W1 | RV-0009 | conduct | R-A | approve | approve | 0 |
    | 2026-05-22 | W1 | RV-0201 | travel | R-D | reject | reject | 0 |
    | 2026-05-22 | W1 | RV-0086 | conduct | R-C | approve | approve | 0 |
    | 2026-05-22 | W1 | RV-0087 | expense | R-C | reject | reject | 0 |
    | 2026-05-22 | W1 | RV-0090 | pto | R-C | reject | reject | 0 |
    | 2026-05-22 | W1 | RV-0123 | travel | R-D | approve | approve | 0 |
    | 2026-05-22 | W1 | RV-0167 | benefits | R-E | route-to-human | route-to-human | 0 |
    | 2026-05-23 | W1 | DUP-02a | expense | R-B | approve | reject | 1 |
    | 2026-05-23 | W1 | RV-0007 | benefits | R-A | reject | reject | 0 |
    | 2026-05-23 | W1 | RV-0046 | travel | R-B | reject | approve | 1 |
    | 2026-05-23 | W1 | RV-0047 | travel | R-B | approve | approve | 0 |
    | 2026-05-23 | W1 | RV-0048 | pto | R-B | approve | approve | 0 |
    | 2026-05-23 | W1 | RV-0083 | pto | R-C | approve | approve | 0 |
    | 2026-05-23 | W1 | RV-0085 | expense | R-C | approve | approve | 0 |
    | 2026-05-23 | W1 | RV-0127 | pto | R-D | approve | approve | 0 |
    | 2026-05-23 | W1 | RV-0162 | pto | R-E | approve | approve | 0 |
    | 2026-05-23 | W1 | RV-0170 | expense | R-E | reject | reject | 0 |
    | 2026-05-24 | W1 | DUP-03a | benefits | R-C | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0010 | travel | R-A | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0044 | pto | R-B | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0081 | benefits | R-C | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0084 | pto | R-C | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0089 | travel | R-C | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0128 | conduct | R-D | approve | approve | 0 |
    | 2026-05-24 | W1 | RV-0163 | pto | R-E | approve | approve | 0 |
    | 2026-05-25 | W1 | DUP-05a | benefits | R-E | approve | approve | 0 |
    | 2026-05-25 | W1 | RV-0001 | travel | R-A | approve | approve | 0 |
    | 2026-05-25 | W1 | RV-0004 | conduct | R-A | approve | approve | 0 |
    | 2026-05-25 | W1 | RV-0042 | pto | R-B | approve | reject | 1 |
    | 2026-05-25 | W1 | RV-0122 | pto | R-D | approve | approve | 0 |
    | 2026-05-25 | W1 | RV-0125 | pto | R-D | approve | reject | 1 |
    | 2026-05-25 | W1 | RV-0161 | travel | R-E | route-to-human | route-to-human | 0 |
    | 2026-05-25 | W1 | RV-0166 | travel | R-E | approve | approve | 0 |
    | 2026-05-26 | W2 | RV-0015 | travel | R-A | approve | approve | 0 |
    | 2026-05-26 | W2 | RV-0055 | conduct | R-B | approve | route-to-human | 1 |
    | 2026-05-26 | W2 | RV-0059 | travel | R-B | reject | route-to-human | 1 |
    | 2026-05-26 | W2 | RV-0096 | expense | R-C | approve | approve | 0 |
    | 2026-05-26 | W2 | RV-0138 | conduct | R-D | route-to-human | route-to-human | 0 |
    | 2026-05-27 | W2 | DUP-04a | conduct | R-D | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0016 | benefits | R-A | route-to-human | route-to-human | 0 |
    | 2026-05-27 | W2 | RV-0019 | benefits | R-A | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0051 | travel | R-B | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0056 | pto | R-B | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0091 | travel | R-C | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0092 | travel | R-C | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0097 | travel | R-C | reject | reject | 0 |
    | 2026-05-27 | W2 | RV-0134 | travel | R-D | reject | reject | 0 |
    | 2026-05-27 | W2 | RV-0172 | travel | R-E | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0173 | expense | R-E | approve | approve | 0 |
    | 2026-05-27 | W2 | RV-0178 | expense | R-E | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0058 | travel | R-B | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0094 | travel | R-C | reject | reject | 0 |
    | 2026-05-28 | W2 | RV-0095 | benefits | R-C | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0099 | expense | R-C | approve | route-to-human | 1 |
    | 2026-05-28 | W2 | RV-0100 | expense | R-C | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0131 | benefits | R-D | approve | route-to-human | 1 |
    | 2026-05-28 | W2 | RV-0132 | expense | R-D | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0133 | expense | R-D | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0135 | pto | R-D | approve | approve | 0 |
    | 2026-05-28 | W2 | RV-0176 | expense | R-E | approve | approve | 0 |
    | 2026-05-29 | W2 | RV-0012 | travel | R-A | approve | approve | 0 |
    | 2026-05-29 | W2 | RV-0013 | travel | R-A | route-to-human | route-to-human | 0 |
    | 2026-05-29 | W2 | RV-0014 | travel | R-A | approve | approve | 0 |
    | 2026-05-29 | W2 | RV-0018 | conduct | R-A | approve | approve | 0 |
    | 2026-05-29 | W2 | RV-0020 | conduct | R-A | reject | reject | 0 |
    | 2026-05-29 | W2 | RV-0054 | travel | R-B | approve | approve | 0 |
    | 2026-05-29 | W2 | RV-0140 | pto | R-D | approve | approve | 0 |
    | 2026-05-29 | W2 | RV-0180 | travel | R-E | approve | approve | 0 |
    | 2026-05-30 | W2 | RV-0011 | travel | R-A | reject | reject | 0 |
    | 2026-05-30 | W2 | RV-0017 | benefits | R-A | reject | reject | 0 |
    | 2026-05-30 | W2 | RV-0052 | expense | R-B | approve | approve | 0 |
    | 2026-05-30 | W2 | RV-0137 | pto | R-D | approve | route-to-human | 1 |
    | 2026-05-30 | W2 | RV-0171 | travel | R-E | reject | approve | 1 |
    | 2026-05-30 | W2 | RV-0177 | pto | R-E | approve | approve | 0 |
    | 2026-05-31 | W2 | RV-0098 | conduct | R-C | reject | reject | 0 |
    | 2026-05-31 | W2 | RV-0136 | conduct | R-D | approve | approve | 0 |
    | 2026-05-31 | W2 | RV-0175 | benefits | R-E | approve | approve | 0 |
    | 2026-06-01 | W2 | RV-0053 | expense | R-B | approve | approve | 0 |
    | 2026-06-01 | W2 | RV-0057 | conduct | R-B | approve | reject | 1 |
    | 2026-06-01 | W2 | RV-0060 | benefits | R-B | reject | approve | 1 |
    | 2026-06-01 | W2 | RV-0093 | travel | R-C | reject | reject | 0 |
    | 2026-06-01 | W2 | RV-0139 | travel | R-D | approve | approve | 0 |
    | 2026-06-01 | W2 | RV-0174 | travel | R-E | approve | approve | 0 |
    | 2026-06-01 | W2 | RV-0179 | expense | R-E | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0202 | travel | R-D | reject | reject | 0 |
    | 2026-06-02 | W3 | RV-0022 | expense | R-A | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0029 | conduct | R-A | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0067 | conduct | R-B | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0106 | benefits | R-C | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0108 | conduct | R-C | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0110 | benefits | R-C | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0150 | expense | R-D | approve | reject | 1 |
    | 2026-06-02 | W3 | RV-0183 | benefits | R-E | approve | approve | 0 |
    | 2026-06-02 | W3 | RV-0185 | expense | R-E | approve | approve | 0 |
    | 2026-06-03 | W3 | RV-0021 | pto | R-A | reject | approve | 1 |
    | 2026-06-03 | W3 | RV-0063 | benefits | R-B | approve | approve | 0 |
    | 2026-06-03 | W3 | RV-0149 | travel | R-D | reject | reject | 0 |
    | 2026-06-03 | W3 | RV-0181 | pto | R-E | approve | approve | 0 |
    | 2026-06-03 | W3 | RV-0188 | expense | R-E | approve | approve | 0 |
    | 2026-06-04 | W3 | DUP-01b | pto | R-A | approve | approve | 0 |
    | 2026-06-04 | W3 | RV-0025 | conduct | R-A | approve | approve | 0 |
    | 2026-06-04 | W3 | RV-0028 | conduct | R-A | route-to-human | route-to-human | 0 |
    | 2026-06-04 | W3 | RV-0064 | travel | R-B | reject | reject | 0 |
    | 2026-06-04 | W3 | RV-0102 | travel | R-C | reject | reject | 0 |
    | 2026-06-04 | W3 | RV-0104 | pto | R-C | approve | approve | 0 |
    | 2026-06-04 | W3 | RV-0105 | expense | R-C | reject | reject | 0 |
    | 2026-06-04 | W3 | RV-0148 | benefits | R-D | approve | approve | 0 |
    | 2026-06-05 | W3 | RV-0024 | pto | R-A | route-to-human | route-to-human | 0 |
    | 2026-06-05 | W3 | RV-0143 | pto | R-D | approve | approve | 0 |
    | 2026-06-05 | W3 | RV-0187 | expense | R-E | reject | approve | 1 |
    | 2026-06-05 | W3 | RV-0189 | expense | R-E | approve | route-to-human | 1 |
    | 2026-06-06 | W3 | RV-0023 | conduct | R-A | reject | reject | 0 |
    | 2026-06-06 | W3 | RV-0027 | benefits | R-A | reject | reject | 0 |
    | 2026-06-06 | W3 | RV-0070 | pto | R-B | approve | reject | 1 |
    | 2026-06-06 | W3 | RV-0109 | expense | R-C | route-to-human | route-to-human | 0 |
    | 2026-06-06 | W3 | RV-0141 | travel | R-D | approve | approve | 0 |
    | 2026-06-06 | W3 | RV-0147 | pto | R-D | approve | approve | 0 |
    | 2026-06-06 | W3 | RV-0182 | benefits | R-E | approve | approve | 0 |
    | 2026-06-07 | W3 | DUP-02b | expense | R-B | approve | reject | 1 |
    | 2026-06-07 | W3 | RV-0062 | travel | R-B | reject | reject | 0 |
    | 2026-06-07 | W3 | RV-0065 | expense | R-B | approve | route-to-human | 1 |
    | 2026-06-07 | W3 | RV-0066 | travel | R-B | approve | route-to-human | 1 |
    | 2026-06-07 | W3 | RV-0068 | benefits | R-B | reject | reject | 0 |
    | 2026-06-07 | W3 | RV-0069 | expense | R-B | approve | reject | 1 |
    | 2026-06-07 | W3 | RV-0101 | conduct | R-C | approve | reject | 1 |
    | 2026-06-07 | W3 | RV-0145 | pto | R-D | approve | approve | 0 |
    | 2026-06-07 | W3 | RV-0190 | conduct | R-E | approve | approve | 0 |
    | 2026-06-08 | W3 | RV-0026 | conduct | R-A | reject | reject | 0 |
    | 2026-06-08 | W3 | RV-0030 | travel | R-A | approve | approve | 0 |
    | 2026-06-08 | W3 | RV-0061 | expense | R-B | approve | approve | 0 |
    | 2026-06-08 | W3 | RV-0103 | benefits | R-C | approve | reject | 1 |
    | 2026-06-08 | W3 | RV-0107 | travel | R-C | approve | approve | 0 |
    | 2026-06-08 | W3 | RV-0142 | conduct | R-D | reject | reject | 0 |
    | 2026-06-08 | W3 | RV-0144 | expense | R-D | approve | approve | 0 |
    | 2026-06-08 | W3 | RV-0146 | expense | R-D | reject | reject | 0 |
    | 2026-06-08 | W3 | RV-0184 | pto | R-E | approve | approve | 0 |
    | 2026-06-08 | W3 | RV-0186 | benefits | R-E | approve | approve | 0 |
    | 2026-06-09 | W4 | RV-0032 | benefits | R-A | approve | approve | 0 |
    | 2026-06-09 | W4 | RV-0035 | travel | R-A | route-to-human | route-to-human | 0 |
    | 2026-06-09 | W4 | RV-0072 | pto | R-B | approve | approve | 0 |
    | 2026-06-09 | W4 | RV-0075 | conduct | R-B | approve | reject | 1 |
    | 2026-06-09 | W4 | RV-0079 | conduct | R-B | reject | reject | 0 |
    | 2026-06-09 | W4 | RV-0152 | expense | R-D | approve | approve | 0 |
    | 2026-06-09 | W4 | RV-0194 | travel | R-E | route-to-human | route-to-human | 0 |
    | 2026-06-10 | W4 | DUP-03b | benefits | R-C | approve | approve | 0 |
    | 2026-06-10 | W4 | RV-0077 | pto | R-B | reject | reject | 0 |
    | 2026-06-10 | W4 | RV-0151 | benefits | R-D | approve | route-to-human | 1 |
    | 2026-06-11 | W4 | DUP-04b | conduct | R-D | approve | reject | 1 |
    | 2026-06-11 | W4 | RV-0040 | expense | R-A | reject | reject | 0 |
    | 2026-06-11 | W4 | RV-0112 | conduct | R-C | approve | reject | 1 |
    | 2026-06-11 | W4 | RV-0115 | pto | R-C | approve | approve | 0 |
    | 2026-06-11 | W4 | RV-0116 | benefits | R-C | route-to-human | approve | 1 |
    | 2026-06-11 | W4 | RV-0192 | benefits | R-E | approve | approve | 0 |
    | 2026-06-11 | W4 | RV-0199 | travel | R-E | approve | approve | 0 |
    | 2026-06-12 | W4 | RV-0031 | conduct | R-A | approve | approve | 0 |
    | 2026-06-12 | W4 | RV-0034 | expense | R-A | approve | approve | 0 |
    | 2026-06-12 | W4 | RV-0119 | expense | R-C | approve | approve | 0 |
    | 2026-06-12 | W4 | RV-0191 | benefits | R-E | reject | route-to-human | 1 |
    | 2026-06-13 | W4 | DUP-05b | benefits | R-E | approve | approve | 0 |
    | 2026-06-13 | W4 | RV-0078 | conduct | R-B | approve | route-to-human | 1 |
    | 2026-06-13 | W4 | RV-0080 | pto | R-B | approve | reject | 1 |
    | 2026-06-13 | W4 | RV-0111 | travel | R-C | approve | approve | 0 |
    | 2026-06-13 | W4 | RV-0195 | pto | R-E | reject | reject | 0 |
    | 2026-06-14 | W4 | RV-0036 | expense | R-A | approve | approve | 0 |
    | 2026-06-14 | W4 | RV-0074 | conduct | R-B | approve | approve | 0 |
    | 2026-06-14 | W4 | RV-0117 | benefits | R-C | approve | reject | 1 |
    | 2026-06-14 | W4 | RV-0120 | conduct | R-C | approve | approve | 0 |
    | 2026-06-14 | W4 | RV-0155 | travel | R-D | approve | route-to-human | 1 |
    | 2026-06-14 | W4 | RV-0156 | pto | R-D | approve | approve | 0 |
    | 2026-06-14 | W4 | RV-0158 | pto | R-D | reject | reject | 0 |
    | 2026-06-14 | W4 | RV-0200 | conduct | R-E | approve | approve | 0 |
    | 2026-06-15 | W4 | RV-0071 | benefits | R-B | approve | reject | 1 |
    | 2026-06-15 | W4 | RV-0193 | expense | R-E | route-to-human | reject | 1 |
    | 2026-06-15 | W4 | RV-0196 | benefits | R-E | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0037 | expense | R-A | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0038 | travel | R-A | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0076 | conduct | R-B | route-to-human | route-to-human | 0 |
    | 2026-06-16 | W4 | RV-0113 | conduct | R-C | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0154 | pto | R-D | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0157 | expense | R-D | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0159 | expense | R-D | approve | approve | 0 |
    | 2026-06-16 | W4 | RV-0197 | pto | R-E | reject | reject | 0 |
    | 2026-06-16 | W4 | RV-0198 | expense | R-E | approve | approve | 0 |
    | 2026-06-17 | W4 | RV-0033 | benefits | R-A | approve | approve | 0 |
    | 2026-06-17 | W4 | RV-0039 | pto | R-A | approve | approve | 0 |
    | 2026-06-17 | W4 | RV-0073 | travel | R-B | route-to-human | reject | 1 |
    | 2026-06-17 | W4 | RV-0114 | expense | R-C | reject | approve | 1 |
    | 2026-06-17 | W4 | RV-0118 | expense | R-C | approve | approve | 0 |
    | 2026-06-17 | W4 | RV-0153 | expense | R-D | route-to-human | route-to-human | 0 |
    | 2026-06-17 | W4 | RV-0160 | conduct | R-D | approve | approve | 0 |

    Read a few rows, then answer:

    ***What does override = 1 mean?***

    - The reviewer agreed with PolicyPal
    - The reviewer made a different call from PolicyPal
    - The case was passed to a person in HR

    <details><summary>Show the answer</summary>

    `The reviewer made a different call from PolicyPal`. `1` means `human_decision` is different from `ai_decision`. `0` means the reviewer agreed. Overriding is normal: PolicyPal is not always right. A reviewer who never overrides is the worry.

    </details>

0. **Check whether the overall rate proves the checking is real.** The table below is grouped by reviewer: one row per reviewer, and an All row at the bottom for the whole team. The Rate column is the override rate: out of every 100 decisions, how many the reviewer changed.

    | reviewer | Rows | overrides | Rate |
    |---|---|---|---|
    | R-A | 42 | 1 | 2% |
    | R-B | 42 | 18 | 43% |
    | R-C | 42 | 7 | 17% |
    | R-D | 44 | 7 | 16% |
    | R-E | 42 | 6 | 14% |
    | All | 212 | 39 | 18% |

    Look at the All row. Across the team, reviewers override PolicyPal on 18% of cases.

    ***Does that one number tell you that every reviewer is really checking?***

    - Yes: 18% looks healthy, so the checking is fine
    - No: an average can hide a reviewer who never disagrees and another who disagrees far too often

    <details><summary>Show the answer</summary>

    `No`. The 18% is an average of five people. One reviewer who approves everything and another who overrides everything can still average out to a normal-looking number. That is why the rest of this lab breaks the numbers down.

    </details>

0. **Spot the reviewer who almost never disagrees.** A reviewer whose rate is far below everyone else's might be clicking "approve" without reading. At this point that is only a reason to look closer, not proof.

    | reviewer | Rows | overrides | Rate |
    |---|---|---|---|
    | R-A | 42 | 1 | 2% |
    | R-B | 42 | 18 | 43% |
    | R-C | 42 | 7 | 17% |
    | R-D | 44 | 7 | 16% |
    | R-E | 42 | 6 | 14% |
    | All | 212 | 39 | 18% |

    Compare the Rate for each reviewer above.

    ***Which reviewer almost never disagrees with PolicyPal?***

    - R-A
    - R-B
    - R-C
    - R-D
    - R-E

    <details><summary>Show the answer</summary>

    `R-A`, at 2%, when the team average is 18%. The other four are between 14% and 43%.

    </details>

0. **Rule out an easy pile of cases for R-A.** Before you suspect anyone, check the innocent explanation. Maybe R-A simply got easy cases that did not need changing. If so, the other reviewers would not change those kinds of case either.

    The two tables below break the numbers down. Each box shows overrides out of decisions: `1/11` means 1 override out of 11 decisions.

    Each reviewer, split by case type:

    | reviewer \ case_type | benefits | conduct | expense | pto | travel | All |
    |---|---|---|---|---|---|---|
    | R-A | 0/8 (0%) | 0/12 (0%) | 0/5 (0%) | 1/5 (20%) | 0/12 (0%) | 1/42 (2%) |
    | R-B | 2/5 (40%) | 5/10 (50%) | 4/8 (50%) | 3/8 (38%) | 4/11 (36%) | 18/42 (43%) |
    | R-C | 3/10 (30%) | 2/7 (29%) | 2/10 (20%) | 0/5 (0%) | 0/10 (0%) | 7/42 (17%) |
    | R-D | 2/4 (50%) | 1/7 (14%) | 1/10 (10%) | 2/14 (14%) | 1/9 (11%) | 7/44 (16%) |
    | R-E | 1/11 (9%) | 1/3 (33%) | 3/11 (27%) | 0/8 (0%) | 1/9 (11%) | 6/42 (14%) |
    | All | 8/38 (21%) | 9/39 (23%) | 10/44 (23%) | 6/40 (15%) | 6/51 (12%) | 39/212 (18%) |

    Each reviewer, split by week:

    | reviewer \ week | W1 | W2 | W3 | W4 | All |
    |---|---|---|---|---|---|
    | R-A | 0/11 (0%) | 0/10 (0%) | 1/11 (9%) | 0/10 (0%) | 1/42 (2%) |
    | R-B | 4/11 (36%) | 4/10 (40%) | 5/11 (45%) | 5/10 (50%) | 18/42 (43%) |
    | R-C | 0/11 (0%) | 1/10 (10%) | 2/10 (20%) | 4/11 (36%) | 7/42 (17%) |
    | R-D | 1/11 (9%) | 2/11 (18%) | 1/11 (9%) | 3/11 (27%) | 7/44 (16%) |
    | R-E | 1/11 (9%) | 1/10 (10%) | 2/10 (20%) | 2/11 (18%) | 6/42 (14%) |
    | All | 6/55 (11%) | 8/51 (16%) | 11/53 (21%) | 14/53 (26%) | 39/212 (18%) |

    - In the first table, in the case types where R-A overrides nothing, do the other reviewers override?
    - In the second table, does R-A override in some weeks and not others?

    ***Could an easy pile of cases explain R-A's 2%?***

    - Yes: R-A's cases are the kind nobody overrides
    - No: other reviewers override the same kinds of case regularly, and R-A almost never does, in any week

    ***What one check would settle whether R-A is really reviewing?***

    - A second reviewer re-marks a sample of R-A's approvals
    - Ask R-A whether they are checking properly
    - Move R-A to a different team
    - Wait another month and look again

    <details><summary>Show the answer</summary>

    - `No`. R-A overrides nothing in four of the five case types (benefits, conduct, expense and travel), yet in each of those types most of the other reviewers override at least one case, and R-B overrides 5 of 10 conduct cases. R-A's rate is zero in three of the four weeks. The one exception is a single `pto` override in week 3: mention it, do not explain it away.
    - `A second reviewer re-marks a sample of R-A's approvals`. It tests the approvals directly, instead of relying on R-A's word or on waiting.

    </details>

0. **Find the reviewer who disagrees the most.** The opposite pattern is worth checking too. A reviewer who overrides far more than everyone else might be the problem, or PolicyPal might be doing worse on the cases they happen to get.

    | reviewer | Rows | overrides | Rate |
    |---|---|---|---|
    | R-A | 42 | 1 | 2% |
    | R-B | 42 | 18 | 43% |
    | R-C | 42 | 7 | 17% |
    | R-D | 44 | 7 | 16% |
    | R-E | 42 | 6 | 14% |
    | All | 212 | 39 | 18% |

    Each reviewer, split by case type:

    | reviewer \ case_type | benefits | conduct | expense | pto | travel | All |
    |---|---|---|---|---|---|---|
    | R-A | 0/8 (0%) | 0/12 (0%) | 0/5 (0%) | 1/5 (20%) | 0/12 (0%) | 1/42 (2%) |
    | R-B | 2/5 (40%) | 5/10 (50%) | 4/8 (50%) | 3/8 (38%) | 4/11 (36%) | 18/42 (43%) |
    | R-C | 3/10 (30%) | 2/7 (29%) | 2/10 (20%) | 0/5 (0%) | 0/10 (0%) | 7/42 (17%) |
    | R-D | 2/4 (50%) | 1/7 (14%) | 1/10 (10%) | 2/14 (14%) | 1/9 (11%) | 7/44 (16%) |
    | R-E | 1/11 (9%) | 1/3 (33%) | 3/11 (27%) | 0/8 (0%) | 1/9 (11%) | 6/42 (14%) |
    | All | 8/38 (21%) | 9/39 (23%) | 10/44 (23%) | 6/40 (15%) | 6/51 (12%) | 39/212 (18%) |

    Each reviewer, split by what PolicyPal proposed:

    | reviewer \ ai_decision | approve | reject | route-to-human | All |
    |---|---|---|---|---|
    | R-A | 0/27 (0%) | 1/9 (11%) | 0/6 (0%) | 1/42 (2%) |
    | R-B | 13/30 (43%) | 3/8 (38%) | 2/4 (50%) | 18/42 (43%) |
    | R-C | 5/31 (16%) | 1/9 (11%) | 1/2 (50%) | 7/42 (17%) |
    | R-D | 7/32 (22%) | 0/10 (0%) | 0/2 (0%) | 7/44 (16%) |
    | R-E | 2/30 (7%) | 3/7 (43%) | 1/5 (20%) | 6/42 (14%) |
    | All | 27/150 (18%) | 8/43 (19%) | 4/19 (21%) | 39/212 (18%) |

    First find the reviewer with the highest rate in the first table. Then, in the next two tables, compare that reviewer's number of decisions (the number after the slash) with everyone else's. Do they get the same kinds of case, and the same mix of PolicyPal proposals?

    ***Which reviewer disagrees the most?***

    - R-A
    - R-B
    - R-C
    - R-D
    - R-E

    ***Is the high rate about the reviewer or about PolicyPal?***

    - PolicyPal: this reviewer gets a harder mix of cases
    - The reviewer: they get the same mix of cases and proposals as everyone else

    <details><summary>Show the answer</summary>

    - `R-B`, at 43%.
    - `The reviewer`. R-B's case types and PolicyPal proposals are spread much like everyone else's (for example 30 approvals, 8 rejections and 4 routings, against 27 to 32, 7 to 10 and 2 to 6 for the others). Same work, very different decisions: the difference is the reviewer.

    </details>

0. **Check whether the override rate is changing, and who is responsible.** The table below is grouped by week. Read the rate for W1 to W4.

    | week | Rows | overrides | Rate |
    |---|---|---|---|
    | W1 | 55 | 6 | 11% |
    | W2 | 51 | 8 | 16% |
    | W3 | 53 | 11 | 21% |
    | W4 | 53 | 14 | 26% |
    | All | 212 | 39 | 18% |

    A rising override rate can mean two very different things: PolicyPal is getting worse, so reviewers have more to fix, or the reviewers are getting stricter. To tell them apart, check PolicyPal's quality for the same period, below.

    | Period | Answers marked | Business Quality Score | Alarm floor | Drop from baseline |
    |---|---|---|---|---|
    | April to June 2026 | 12 | 92 | 85 | None |

    ***Which way is the override rate moving?***

    - Going up
    - Going down
    - Staying about the same

    ***Is PolicyPal getting worse?***

    - Yes: the rising rate shows PolicyPal's answers are getting worse
    - No: PolicyPal's quality held steady, so the change is in how the reviewers are deciding

    <details><summary>Show the answer</summary>

    - `Going up`: from 11% in week 1 to 26% in week 4.
    - `No`. The quality review for the same quarter scored 92, above the alarm floor and with no drop. PolicyPal's answers did not get worse, so the rise comes from the reviewers. Worth watching, but not a problem with PolicyPal.

    </details>

0. **Check the secret repeat cases.** To test whether reviewers are really reading, the company slipped some cases in twice. The same case went to the same reviewer two times, on two different days, a week or two apart. The reviewer did not know it was a repeat.

    A careful reviewer makes the same decision both times. A reviewer who is not really reading may not.

    The table below has one row for each repeated case, one for each reviewer. First look is the date the reviewer first saw the case and what they decided; second look is the date they saw the same case again and what they decided that time.

    | Case | Reviewer | Case type | PolicyPal proposed | First look (date) | First decision | Second look (date) | Second decision |
    |---|---|---|---|---|---|---|---|
    | DUP-01 | R-A | pto | approve | 2026-05-21 | approve | 2026-06-04 | approve |
    | DUP-02 | R-B | expense | approve | 2026-05-23 | reject | 2026-06-07 | reject |
    | DUP-03 | R-C | benefits | approve | 2026-05-24 | approve | 2026-06-10 | approve |
    | DUP-04 | R-D | conduct | approve | 2026-05-27 | approve | 2026-06-11 | reject |
    | DUP-05 | R-E | benefits | approve | 2026-05-25 | approve | 2026-06-13 | approve |

    For each row, compare the First decision with the Second decision.

    ***Which reviewer decided the same case two different ways?***

    - R-A
    - R-B
    - R-C
    - R-D
    - R-E
    - None of them

    <details><summary>Show the answer</summary>

    `R-D`, on case `DUP-04`: approve on 27 May, reject on 11 June. Everyone else made the same decision both times. Note that R-A was consistent too: consistency alone does not prove someone is reading, because approving everything is also consistent.

    </details>

0. **Decide who owns fixing the R-A finding.** R-A's pattern is the most serious finding. In plain words: R-A's approvals are not getting a real, independent check, and you have already ruled out the innocent explanation (an easy pile of cases).

    The fix will be a change to how reviewing is done. For example, a second reviewer could check a sample of R-A's approvals, or R-A could be re-trained on the review standard. So the finding goes to whoever runs the review process, not to whoever runs the AI.

    | Owner | What they are responsible for |
    |---|---|
    | The function that runs the human review process for PolicyPal | The five reviewers and how they work: who reviews which cases, their training on the review standard, and extra checks such as a second reviewer |
    | The platform / technical owner | The technology behind PolicyPal: the AI model, the software, sign-in, and speed |
    | The team that owns the HR policy library | The HR policy documents PolicyPal reads from, and keeping them current |

    Keep in mind what you found about R-A: which reviewer almost never disagrees, and whether an easy pile of cases explains it. Choose who owns the fix, and write one line saying why. Lab 3.2 is where you write the plan.

    ***Who owns fixing the R-A finding?***

    - The function that runs the human review process for PolicyPal
    - The platform / technical owner
    - The team that owns the HR policy library
    - No one yet: 2% could just be an easy pile

    ***Why? One line.***

    <details><summary>Show the answer</summary>

    `The function that runs the human review process for PolicyPal`. It is the only one of the four that can change how reviewing is done: who reviews, how, and whether a second reviewer checks. The platform team runs the AI and the HR policy team writes the policies; neither manages the reviewers. And the easy-pile explanation was ruled out above.

    </details>

## Conclusion

In this lab you saw why a team's overall override rate proves little on its own, broke the numbers down by reviewer, case type and week, flagged one reviewer who almost never disagrees and one who disagrees far more than the rest, ruled out the innocent explanations before naming either, checked a rising trend against the AI's own quality, and routed the most serious finding to the owner of the review process. The metrics point you to who to examine and what to check next; they do not hand you a verdict. This is how you check whether human oversight of an AI workflow is doing real work.
