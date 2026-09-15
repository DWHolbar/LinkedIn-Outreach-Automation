#!/usr/bin/env python3
"""
Fill the 10 LinkedIn outreach templates with real role details.

Usage:
    python fill_templates.py role.json [--templates ../references/message_templates.md] [--out filled.md]

role.json example:
{
    "role_title": "Senior Backend Engineer",
    "company": "Acme",
    "key_skill": "distributed systems",
    "skill_2": "Go",
    "location": "remote",
    "comp_type": "salary + equity",
    "hook": "shipped their payments API to 40k merchants last quarter",
    "achievement": "",
    "mutual_conn": "",
    "recruiter_name": "Sam"
}

Leave a field as "" (empty string) to skip variants that need it (achievement, mutual_conn),
or to drop optional clauses (skill_2). Required fields (role_title, company, key_skill) should
always be filled in, since most variants depend on them.

This does plain {{placeholder}} substitution and reports the character count of every
connection note, flagging any that go over LinkedIn's 300-character invite limit.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ["role_title", "company", "key_skill"]
OPTIONAL_FIELDS = [
    "skill_2", "location", "comp_type", "hook",
    "achievement", "mutual_conn", "recruiter_name",
]


def load_role(path):
    with open(path) as f:
        data = json.load(f)
    missing = [f for f in REQUIRED_FIELDS if not data.get(f)]
    if missing:
        print(f"Warning: missing required fields: {', '.join(missing)}. "
              "Variants using them will keep the raw placeholder.", file=sys.stderr)
    for f in OPTIONAL_FIELDS:
        data.setdefault(f, "")
    return data


def build_skill2_clause(role):
    return f" and {role['skill_2']}" if role.get("skill_2") else ""


def fill(text, role):
    text = text.replace("{{skill_2_clause}}", build_skill2_clause(role))
    # {{first_name}} is intentionally left for per-candidate merge, not filled here.
    for key, value in role.items():
        if key == "first_name":
            continue
        text = text.replace("{{" + key + "}}", value)
    return text


def extract_variants(template_md):
    """Split message_templates.md into (heading, connection_note, first_message) tuples."""
    blocks = re.split(r"\n---\n", template_md)
    variants = []
    for block in blocks:
        heading_match = re.search(r"^##\s*(Variant.+)$", block, re.MULTILINE)
        note_match = re.search(
            r"\*\*Connection note:\*\*\n(.+?)\n\n\*\*First message:\*\*", block, re.DOTALL
        )
        msg_match = re.search(r"\*\*First message:\*\*\n(.+?)\s*$", block, re.DOTALL)
        if heading_match and note_match and msg_match:
            variants.append((
                heading_match.group(1).strip(),
                note_match.group(1).strip(),
                msg_match.group(1).strip(),
            ))
    return variants


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("role_json", help="Path to a JSON file with role details")
    default_templates = Path(__file__).parent.parent / "references" / "message_templates.md"
    parser.add_argument("--templates", default=str(default_templates), help="Path to message_templates.md")
    parser.add_argument("--out", default=None, help="Write filled output to this file instead of stdout")
    args = parser.parse_args()

    role = load_role(args.role_json)
    template_md = Path(args.templates).read_text()
    variants = extract_variants(template_md)
    if not variants:
        print("Could not parse any variants out of the templates file.", file=sys.stderr)
        sys.exit(1)

    lines = []
    for heading, note, message in variants:
        filled_note = fill(note, role)
        filled_message = fill(message, role)
        char_count = len(filled_note)
        flag = "  <-- OVER 300 CHAR LIMIT" if char_count > 300 else ""
        lines.append(f"### {heading}")
        lines.append(f"**Connection note** ({char_count} chars){flag}:")
        lines.append(filled_note)
        lines.append("")
        lines.append("**First message:**")
        lines.append(filled_message)
        lines.append("")
        lines.append("---")
        lines.append("")

    output = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(output)
        print(f"Wrote filled templates to {args.out}")
    else:
        print(output)


if __name__ == "__main__":
    main()
