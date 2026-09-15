# Tracking outreach performance

Use `assets/metrics_template.csv` as the log. One row per variant per campaign (a "campaign" is one role, one time period, e.g. "Senior Backend Engineer @ Acme, Sept 2026"). If you run the same variant again later for a different role, that's a new row.

## Columns

| Column | What it means | Where it comes from |
|---|---|---|
| `variant_id` | Which of the 10 templates (1-10) | You, when setting up the Aimfox campaign |
| `variant_angle` | Short label, e.g. "skills match," "casual" | From `message_templates.md` |
| `role` | Role title + company | The job you're sourcing for |
| `date_sent` | Date the batch went out | When you launch that variant in Aimfox |
| `connections_sent` | Blank invite requests sent for that variant's candidate segment | Aimfox campaign export |
| `connections_accepted` | Invites accepted | Aimfox campaign export |
| `connection_accept_rate` | accepted / sent | Calculated |
| `messages_sent` | First messages sent (to accepted connections) | Aimfox campaign export |
| `replies_received` | Any reply at all | Aimfox campaign export |
| `reply_rate` | replies / messages_sent | Calculated |
| `positive_replies` | Replies that were interested, asked a follow-up, or booked time (not a flat "not interested" or no engagement) | You, reading the replies |
| `positive_reply_rate` | positive_replies / messages_sent | Calculated |
| `calls_booked` | Actual screening calls scheduled | Your ATS or calendar |
| `notes` | Anything qualitative, e.g. "several said comp too low," "one flagged wrong seniority" | You |

## Pulling from Aimfox

Aimfox's campaign dashboard/export gives you sent, accepted, and reply counts per campaign. Since connection requests go out blank and the message fires automatically on acceptance, the variant lives entirely in which message template a campaign is set to send. If you're running each variant as its own campaign (recommended, keeps the numbers clean), the export maps 1:1 to a row. If you're running multiple variants inside one campaign, you'll need to split the export by which message template each contact received before filling the row.

## How to actually compare variants

1. **Don't compare until there's enough volume.** LinkedIn/Aimfox rate limits mean you're often sending 15-25 connection requests a day per sender. At fewer than ~30 sends for a variant, a 40% vs 55% reply rate is well within normal noise, not a real difference. Wait for **at least 30-50 connection requests sent per variant** before drawing any conclusion, more if the rates are close.
2. **Hold everything else constant.** Same role, same seniority, same candidate pool quality, same time window. If one variant went out to more senior candidates or a different geography, the comparison isn't clean, note that in `notes` instead of treating the result as conclusive.
3. **Look at reply rate and positive reply rate together, not just replies.** A variant with a high reply rate but mostly "not interested, please remove me" is worse than a variant with a lower reply rate but higher positive replies. Positive reply rate is the number that actually matters for filling the role.
4. **A real signal looks like this:** a gap of roughly 15 percentage points or more in reply rate or positive reply rate, at 50+ sends per variant. A gap of a few points, or a gap seen after fewer than 30 sends, is "keep watching," not "declare a winner."
5. **Once you have a winner, don't just stop testing.** Roll the losing variants' remaining candidate pool onto the winner, but keep 1-2 alternate variants running at low volume so you're not permanently locked into one message if the market or role changes.

## Example

| variant_id | variant_angle | role | date_sent | connections_sent | connections_accepted | connection_accept_rate | messages_sent | replies_received | reply_rate | positive_replies | positive_reply_rate | calls_booked | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | skills match | Senior Backend Engineer @ Acme | 2026-09-01 | 60 | 34 | 57% | 34 | 12 | 35% | 5 | 15% | 2 | |
| 4 | curiosity / short | Senior Backend Engineer @ Acme | 2026-09-01 | 60 | 41 | 68% | 41 | 19 | 46% | 9 | 22% | 4 | higher accept rate too, worth scaling |

Variant 4 shows a real gap here (both accept rate and positive reply rate meaningfully higher, at 60 sends each), so it's a reasonable call to shift more volume to it.
