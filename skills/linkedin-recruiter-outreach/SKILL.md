---
name: linkedin-recruiter-outreach
description: Generate 10 distinct LinkedIn outreach message variants (connection note + first message) for a recruiter sourcing candidates for a specific role, ready to load into Aimfox as an A/B test. Use this whenever the user wants recruiter outreach copy for LinkedIn, wants to pull a role from a job board URL (including talent.superteam.fun/jobs) and turn it into candidate messages, wants to test which LinkedIn message performs best, or wants to log/compare Aimfox campaign results (connection accept rate, reply rate, positive reply rate) across message variants. Trigger even if the user just pastes a job link or a role description and says something like "write outreach for this role" or "help me message candidates for this."
---

# LinkedIn Recruiter Outreach

Turn one open role into 10 different, human-sounding LinkedIn outreach variants a recruiter can run as an A/B test in Aimfox, then track which one actually gets replies.

## When to use this

Use this skill any time the user gives you a role (a job URL, a pasted job description, or just role details in chat) and wants candidate-facing LinkedIn copy, or wants to record/compare how variants performed. This covers both halves of the job: **writing** the messages and **tracking** the results.

## Step 1: Get the role details

If the user gives a URL (especially from `talent.superteam.fun/jobs/...`), fetch it and pull out:

- Role title and seniority (junior / mid / senior / lead)
- Company name
- 1-2 concrete must-have skills (not a laundry list, pick the ones that actually differentiate a fit candidate)
- Location / remote setup
- Comp type: salary, equity, token allocation, or a mix, plus range if listed
- One standout hook: something specific about the company or role a stranger would find worth knowing (funding, live product, user numbers, what the team is actually shipping). Avoid generic mission-statement language ("we're passionate about...") even if the posting uses it, rewrite it as a plain fact.

If the user pastes a job description or types the details directly, extract the same fields from that instead. If something is missing (e.g. no comp listed), leave it out of the messages rather than guessing or writing a placeholder like "[comp]" into the final output.

If the URL can't be fetched, tell the user and ask them to paste the job description text instead. Don't invent role details.

## Step 2: Fill the 10 templates

Read `references/message_templates.md`. It has 10 templates, each with a different angle (skills match, company hook, casual, direct pitch, question-led, etc). Fill in the `{{placeholders}}` with the real role details from Step 1.

Rules for every message, no exceptions:

- **No em dashes.** Use a period, comma, or just break into two sentences.
- **No recruiter fluff.** Never use words like passionate, rockstar, synergy, circle back, touch base, leverage, excited to connect, thought leader, growth mindset, or "hope this finds you well." If a sentence sounds like it came from a template, rewrite it plainer.
- **Sound like a person typing a message, not a company sending a blast.** Short sentences. Contractions are fine. No exclamation-point stacking.
- **Be specific to the role**, not generic. A message that could apply to any job at any company means the extraction in Step 1 didn't go deep enough, go back and find one real detail to anchor it.
- **Connection note stays under 300 characters** (LinkedIn's hard limit on invite notes). Check the character count before finalizing each one.
- Leave `{{first_name}}` as a literal placeholder in the final output (the recruiter fills this per-candidate when sending, or Aimfox merges it automatically), don't guess a name.
- If a template calls for something you don't have (mutual connection, candidate's specific achievement), either drop that line or note it needs manual personalization per candidate. Don't fabricate a mutual connection or a fake achievement.

## Step 3: Output format

Present all 10 variants in one place, ready to copy into Aimfox. Use this structure for each:

```
### Variant N — [angle name]
**Connection note** (X chars):
[text]

**First message** (sent after they accept):
[text]
```

After the 10 variants, remind the user: stagger which variants go to which candidate segment (e.g. split your candidate list roughly evenly across variants, or run 3-4 at a time if the list is small) so the comparison is fair, and keep the role and seniority constant across the test, only the message angle should differ.

## Step 4: Tracking results

When the user wants to log or compare how variants did, use `references/tracking_metrics.md` for the full explanation, and `assets/metrics_template.csv` as the actual log file to fill in or hand to the user.

Quick version: for each variant, pull from Aimfox's campaign export:
- connections sent, connections accepted → accept rate
- messages sent, replies received → reply rate
- of the replies, how many were positive (interested, asked a question, booked time) → positive reply rate

Don't call a winner off small numbers. Aimfox rate limits mean a variant might only get 20-30 sends before you can compare, and at that volume a 40% vs 55% reply rate can easily be noise. Wait for at least ~30-50 connection requests sent per variant before drawing conclusions, and even then treat a lead of a few points as "worth watching," not proof. A gap of 15+ points at 50+ sends per variant is a real signal.

## Optional: merging fields with a script

For bulk use (many roles, or re-running the same template set often), `scripts/fill_templates.py` does simple `{{placeholder}}` substitution against `references/message_templates.md` given a JSON file of role fields. This is optional, doing it inline in the conversation works fine for one-off requests. Use the script when the user wants to batch-generate messages for several roles at once.
