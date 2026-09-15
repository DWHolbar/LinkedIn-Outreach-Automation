# LinkedIn outreach templates (10 variants)

No connection note. Aimfox sends the connection request blank, and the moment the candidate accepts, it fires the message below automatically. So the message itself has to do all the work: say who you are, what the role is, what they'd actually be doing, what they'd get, and ask if they're interested. Don't assume they remember why they connected, a lot of people accept invites without reading the note anyway (and here there isn't one).

## Placeholders to fill per role

- `{{first_name}}` — leave literal, filled per candidate (Aimfox merges this automatically)
- `{{role_title}}` — e.g. "Trade Operations Manager"
- `{{company}}`
- `{{key_skill}}` — the one skill that actually matters most for this role
- `{{skill_2}}` — a second differentiating skill or tool (optional, drop if you only have one)
- `{{location}}` — city, or "remote," or "remote within European timezones," etc, phrased so it reads naturally after "It's ___"
- `{{comp_type}}` — "salary," "salary plus equity," "salary plus token allocation," etc. Only fill this if the posting actually lists it. If there's no comp info, leave `{{comp_clause}}` empty (see below), don't guess a number or write something vague like "competitive pay."
- `{{comp_clause}}` — a small helper, not something you write directly. Fill it as `", {{comp_type}}"` when comp is listed, or leave it as an empty string when it isn't. This gets appended right after `{{location}}`.
- `{{hook}}` — one concrete, specific fact about the company, phrased so it reads naturally after "{{company}} is ___" (e.g. "building a proprietary trading desk from scratch," "live in 40k merchants' checkout flow," "backed by Sequoia and hiring fast"). Rewrite it into that shape even if the posting phrased it differently.
- `{{responsibilities}}` — a verb phrase (lowercase, no leading capital) summarizing 2-3 of the real day-to-day duties from the posting, written in plain language, not copy-pasted bullets. It slots into "Day to day, you'd {{responsibilities}}." Example: "own daily reconciliation across venues and custodians, monitor execution in real time, and act as first responder when something breaks."
- `{{benefits}}` — a comma-separated phrase naming 2-3 benefits that would actually matter to a candidate (comp already covered separately, so think remote flexibility, vacation days, equity/token upside if not already in comp_type, learning/career support). Skip filler benefits like "fun team" or "great culture." It slots into "On top of that, the role comes with {{benefits}}." Example: "flexible hours, 30 days of paid vacation, and support for career development."
- `{{achievement}}` — something specific from the candidate's profile (a project, post, or past role). Only use if you actually have this, don't fabricate it.
- `{{mutual_conn}}` — a real mutual connection or shared group, only if it exists

There's no character limit to work around here since there's no connection note, but don't let the message balloon into a wall of text either. Aim for roughly 80-130 words: enough to cover role, responsibilities, comp/location, and benefits in full sentences, not a bulleted dump. If a role genuinely needs more detail than that to make sense, that's fine, just keep every sentence doing real work.

---

## Variant 1 — Skills match

Hey {{first_name}}, thanks for connecting. I'm hiring a {{role_title}} at {{company}} and your background in {{key_skill}} looks like a strong fit. Day to day, you'd {{responsibilities}}. It's {{location}}{{comp_clause}}. On top of that, the role comes with {{benefits}}. Would you be interested in hearing more?

---

## Variant 2 — Company hook

Hey {{first_name}}, thanks for connecting. Quick context on why I reached out: {{company}} is {{hook}}, and we're hiring a {{role_title}} to help with that. Day to day, you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, and the role comes with {{benefits}}. Would you be interested in learning more?

---

## Variant 3 — Mutual interest / saw your profile

Hey {{first_name}}, thanks for accepting. I recruit for {{company}} and I'm filling a {{role_title}} role right now. Your experience with {{key_skill}} is close to what we need. Day to day, that means you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, plus {{benefits}}. Interested in hearing more?

---

## Variant 4 — Straight to it

Hey {{first_name}}, thanks for connecting. I'm hiring a {{role_title}} at {{company}}. Short version: you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, and the role comes with {{benefits}}. Would you be interested?

---

## Variant 5 — Direct role pitch

Hey {{first_name}}, thanks for connecting. Here's the role: {{role_title}} at {{company}}, {{location}}{{comp_clause}}. Main focus is {{key_skill}}, which in practice means you'd {{responsibilities}}. On top of that, {{benefits}}. Would you be open to hearing more?

---

## Variant 6 — Referral-style

Hey {{first_name}}, thanks for connecting. {{mutual_conn}} pointed me your way for a {{role_title}} role at {{company}}. Day to day, you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, plus {{benefits}}. Given your background in {{key_skill}}, thought it was worth reaching out. Interested in hearing more?

---

## Variant 7 — Casual

Hey {{first_name}}, thanks for connecting. So I'm filling a {{role_title}} role at {{company}} and your work with {{key_skill}} caught my eye. The job is basically {{responsibilities}}. It's {{location}}{{comp_clause}}, and you'd get {{benefits}}. No pressure either way, just curious if you'd be interested.

---

## Variant 8 — Value-prop

Hey {{first_name}}, thanks for connecting. The role is {{role_title}} at {{company}}. You'd be working mainly on {{key_skill}}{{skill_2_clause}}, which day to day means you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, and on top of that you get {{benefits}}. Would that be worth a closer look for you?

---

## Variant 9 — Question-led

Hey {{first_name}}, thanks for connecting. Are you actively looking, open to the right thing, or heads down where you are right now? Asking because I'm filling a {{role_title}} role at {{company}}. Day to day, that means you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, and it comes with {{benefits}}. Let me know if you'd like the details either way.

---

## Variant 10 — Specific achievement

Hey {{first_name}}, thanks for connecting. {{achievement}} is what made me reach out, it's directly relevant to a {{role_title}} opening at {{company}}. Day to day, you'd {{responsibilities}}. It's {{location}}{{comp_clause}}, plus {{benefits}}. Would you be interested in hearing more?

---

## Notes on filling these

- `{{skill_2_clause}}` in Variant 8 is a small helper: fill it as `" and {{skill_2}}"` if there's a second real skill, or leave it blank (and drop the "and") if not. Don't leave a literal `{{skill_2_clause}}` in the final text.
- Same logic for `{{comp_clause}}`: fill it or leave it empty, never leave the literal placeholder text in a sent message.
- If `{{achievement}}` or `{{mutual_conn}}` isn't available for a given candidate, skip Variant 10 or Variant 6 for that candidate rather than making something up. These two only work with real personalization.
- Every other variant works off role-level facts only, so they can be sent to an entire candidate list without per-candidate research.
- Every variant ends by asking directly if they're interested. Don't soften that into "let me know your thoughts" or drop it, that question is the actual point of the message, it's what gets you a reply you can act on.
