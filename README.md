# LinkedIn Recruiter Outreach (Claude Skill)

Give this skill a job URL or a pasted job description for **any role**, and it generates 10 different LinkedIn outreach messages built from that role's actual details. No two roles produce the same output, since every message is written from what's in the posting: the title, the responsibilities, comp, location, and benefits. There's nothing here tied to a specific role, company, or industry, the templates are all `{{placeholder}}` based and get filled fresh every time.

This is built around how the team actually sends messages today: connection requests go out **blank, with no note**, and Aimfox fires the first message automatically the moment a candidate accepts. So each of the 10 variants is one message that has to carry the whole pitch on its own, and ends by asking directly if the candidate is interested.

## What's in this folder

```
linkedin-recruiter-outreach/
├── SKILL.md                          the workflow Claude follows
├── README.md                         this file
├── references/
│   ├── message_templates.md          the 10 message templates (placeholders, no role baked in)
│   └── tracking_metrics.md           how to log and compare Aimfox results per variant
├── assets/
│   └── metrics_template.csv          the results log, one row per variant
└── scripts/
    └── fill_templates.py             optional: batch-fill templates from a JSON file
```

## How it works, step by step

1. **You give it a role.** A job URL, a pasted job description, or just the details typed into chat. It works the same way regardless of the role or industry, engineering, sales, ops, trading, whatever the posting actually is.
2. **It reads the posting and pulls out the real details**: role title, seniority, company, the 1-2 skills that actually matter, location, comp (only if listed), 2-3 real day-to-day responsibilities in plain language, and 2-3 benefits worth mentioning. If something isn't in the posting (like comp), it's left out rather than guessed.
3. **It fills all 10 templates** from `references/message_templates.md` with those details. Each template takes a different angle (skills match, company hook, casual, direct pitch, question-led, and so on), but all 10 cover the same ground: what the role is, what you'd actually be doing, what it pays and where it's based, what you'd get out of it, and a direct question at the end asking if you're interested.
4. **You get 10 ready-to-paste messages**, one per Aimfox campaign or segment, each labeled by variant number and angle.
5. **After you run the campaigns**, it helps you log results into `assets/metrics_template.csv` and tells you whether a gap between variants is real or just noise.

## Tutorial: running it end to end

### Step 1: Give it a role

Just paste a link or the job text into the chat. For example:

> "Write LinkedIn outreach for this role: [job URL]"

or

> "Here's a job description, write me outreach messages for it: [paste text]"

If the link can't be fetched (some job boards block automated access), it'll tell you and ask you to paste the text instead, rather than guessing at details.

### Step 2: Review the extracted details

Before writing anything, it should show you what it pulled out of the posting, something like:

> - Role: Senior Data Analyst
> - Company: Northwind
> - Key skill: SQL and dashboarding (Looker)
> - Location: Remote, US
> - Comp: $120k-$150k
> - Hook: analytics team of 3 supporting a product used by 2M people
> - Responsibilities: build and maintain reporting dashboards, partner with product on metrics definitions, run ad hoc analysis for leadership
> - Benefits: unlimited PTO, full remote, $1,500 annual learning budget

If anything looks wrong or you want it to weight a different skill or hook, say so here before it writes the messages, it's much cheaper to correct at this stage than after all 10 are written.

### Step 3: Get the 10 messages

You'll get all 10 variants, each one a complete message, something like:

> **Variant 1 — Skills match**
> Hey {{first_name}}, thanks for connecting. I'm hiring a Senior Data Analyst at Northwind and your background in SQL and dashboarding looks like a strong fit. Day to day, you'd build and maintain reporting dashboards, partner with product on metrics definitions, and run ad hoc analysis for leadership. It's remote, US, $120k-$150k. On top of that, the role comes with unlimited PTO and a $1,500 annual learning budget. Would you be interested in hearing more?

`{{first_name}}` is left as a literal placeholder on purpose, either fill it per candidate yourself or let Aimfox's own merge field handle it.

Two variants (referral-style and specific-achievement) only get filled in if you actually have a real mutual connection or something specific from a candidate's profile to reference. Otherwise they're skipped rather than faked, since a made-up mutual connection or achievement is worse than not sending that variant at all.

### Step 4: Set up the Aimfox campaigns

- Set connection requests to send with **no note**.
- Set the first message (fires on acceptance) to one of the 10 variants.
- Split your candidate list across variants roughly evenly, or run 3-4 at a time if your list is small. Keep the role and seniority constant across the test, so a variant's angle is the only thing that changes.

### Step 5: Log the results

Once campaigns have run for a while, pull the numbers from Aimfox's export and log them in `assets/metrics_template.csv`, one row per variant:

```
variant_id,variant_angle,role,date_sent,connections_sent,connections_accepted,connection_accept_rate,messages_sent,replies_received,reply_rate,positive_replies,positive_reply_rate,calls_booked,notes
1,skills match,Senior Data Analyst @ Northwind,2026-09-15,60,38,63%,38,14,37%,6,16%,3,
4,curiosity / short,Senior Data Analyst @ Northwind,2026-09-15,60,45,75%,45,21,47%,10,22%,5,higher accept and reply rate
```

You can ask the skill to do this fill-in for you too, just hand it the Aimfox export or the raw numbers and it'll produce the row.

### Step 6: Decide if there's a real winner

Read `references/tracking_metrics.md` for the full reasoning, but the short version: don't call a winner before **30-50 connection requests sent per variant**. A gap of a few percentage points at low volume is noise. A gap of **15+ points at 50+ sends per variant** is a real signal worth acting on, shift more of your candidate list to that variant, but keep 1-2 alternates running at low volume rather than going all-in permanently.

### Optional: batch-run it for several roles at once

If you're doing this for a handful of roles in one sitting, `scripts/fill_templates.py` will fill all 10 templates from a JSON file of role details without you needing to re-describe the rules each time:

```bash
python3 scripts/fill_templates.py my_role.json
```

Where `my_role.json` looks like:

```json
{
  "role_title": "Senior Data Analyst",
  "company": "Northwind",
  "key_skill": "SQL and dashboarding",
  "skill_2": "",
  "location": "remote, US",
  "comp_type": "$120k-$150k",
  "hook": "supporting a product used by 2M people with a 3-person analytics team",
  "responsibilities": "build and maintain reporting dashboards, partner with product on metrics definitions, and run ad hoc analysis for leadership",
  "benefits": "unlimited PTO, full remote, and a $1,500 annual learning budget",
  "achievement": "",
  "mutual_conn": ""
}
```

This is a convenience for volume, not a requirement. For a single role, it's just as easy to paste the job link into chat and let the skill walk through Steps 1-3 above directly.

## Notes

- Every message avoids em dashes and recruiter fluff (no "passionate," "synergy," "circle back," "excited to connect," etc) on purpose, the goal is to sound like a person messaging a candidate, not a company blasting a template.
- If a job posting doesn't list comp, the messages simply don't mention comp, they don't guess a number or insert a vague line like "competitive pay."
- This skill is role-agnostic. It was demoed here on an engineering role and a trading-ops role while building it, but nothing about it is specific to any one function, industry, or company, feed it any job posting and it works the same way.
