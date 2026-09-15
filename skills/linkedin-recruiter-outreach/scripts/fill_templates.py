#!/usr/bin/env python3
"""
Fill the 10 LinkedIn outreach templates with real role details.

Usage:
    python fill_templates.py role.json [--templates ../references/message_templates.md] [--out filled.md]

role.json example:
{
    "role_title": "Trade Operations Manager",
    "company": "Staking Facilities",
    "key_skill": "trade lifecycle operations",
    "skill_2": "SQL and Excel for reporting",
    "location": "remote within European timezones",
    "comp_type": "",
    "hook": "building a proprietary crypto trading desk from scratch",
    "responsibilities": "own daily reconciliation across venues and custodians, monitor execution in real time, and act as first responder when something breaks",
    "benefits": "flexible hours, 30 days of paid vacation, and support for career development",
    "achievement": "",
    "mutual_conn": ""
}

Leave a field as "" (empty string) to skip variants that need it (achievement, mutual_conn),
or to drop optional clauses (skill_2, comp_type). Required fields (role_title, company,
key_skill, responsibilities, benefits) should always be filled in, since every variant
depends on them, per SKILL.md.

These templates have no connection note, each variant is one message Aimfox fires
automatically once the candidate accepts a blank connection request. This script does
plain {{placeholder}} substitution and reports a word count for each filled message,
flagging any that run well past the ~130-word range the templates are written for.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ["role_title", "company", "key_skill", "responsibilities", "benefits"]
OPTIONAL_FIELDS = ["skill_2", "location", "comp_type", "hook", "achievement", "mutual_conn"]

WORD_COUNT_WARN_ABOVE = 160


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


def build_clauses(role):
    role["skill_2_clause"] = f" and {role['skill_2']}" if role.get("skill_2") else ""
    role["comp_clause"] = f", {role['comp_type']}" if role.get("comp_type") else ""
    return role


def fill(text, role):
    # {{first_name}} is intentionally left for per-candidate merge, not filled here.
    for key, value in role.items():
        if key == "first_name":
            continue
        text = text.replace("{{" + key + "}}", value)
    return text


def extract_variants(template_md):
    """Split message_templates.md into (heading, message) pairs, one per variant."""
    blocks = re.split(r"\n---\n", template_md)
    variants = []
    for block in blocks:
        heading_match = re.search(r"^##\s*(Variant.+)$", block, re.MULTILINE)
        if not heading_match:
            continue
        body = block[heading_match.end():].strip()
        if not body or body.lower().startswith("## notes"):
            continue
        variants.append((heading_match.group(1).strip(), body))
    return variants


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("role_json", help="Path to a JSON file with role details")
    default_templates = Path(__file__).parent.parent / "references" / "message_templates.md"
    parser.add_argument("--templates", default=str(default_templates), help="Path to message_templates.md")
    parser.add_argument("--out", default=None, help="Write filled output to this file instead of stdout")
    args = parser.parse_args()

    role = load_role(args.role_json)
    role = build_clauses(role)
    template_md = Path(args.templates).read_text()
    variants = extract_variants(template_md)
    if not variants:
        print("Could not parse any variants out of the templates file.", file=sys.stderr)
        sys.exit(1)

    skip_needs = {
        "achievement": "achievement",
        "mutual_conn": "mutual_conn",
    }

    lines = []
    for heading, message in variants:
        needed = [field for field, key in skip_needs.items() if "{{" + key + "}}" in message]
        missing = [f for f in needed if not role.get(f)]
        if missing:
            lines.append(f"### {heading}")
            lines.append(f"(skipped, needs real {', '.join(missing)} for this candidate, not filled in)")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue

        filled = fill(message, role)
        word_count = len(filled.split())
        flag = "  <-- longer than the ~130-word target, consider trimming" if word_count > WORD_COUNT_WARN_ABOVE else ""
        lines.append(f"### {heading}")
        lines.append(f"({word_count} words{flag})")
        lines.append(filled)
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
