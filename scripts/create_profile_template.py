#!/usr/bin/env python3
"""Create a blank JSON resume profile skeleton."""

from __future__ import annotations

import json
import sys
from pathlib import Path


TEMPLATE = {
    "target": {
        "language": "",
        "role": "",
        "role_family": "",
        "seniority": "",
        "industry": "",
        "direction": "",
        "audience": "",
        "application_type": "",
        "notes": [],
    },
    "profile": {
        "name": "",
        "headline": "",
        "city": "",
        "phone": "",
        "email": "",
        "links": [],
        "summary": [],
    },
    "skills": [{"group": "", "items": []}],
    "work": [{"company": "", "role": "", "date": "", "bullets": []}],
    "projects": [
        {
            "name": "",
            "date": "",
            "role": "",
            "type": "",
            "tech": [],
            "tools": [],
            "methods": [],
            "context": "",
            "bullets": [],
            "tags": [],
        }
    ],
    "experience_blocks": [
        {
            "title": "",
            "type": "",
            "date": "",
            "context": "",
            "tools": [],
            "bullets": [],
            "evidence": [],
            "tags": [],
        }
    ],
    "education": [
        {"school": "", "degree": "", "major": "", "date": "", "notes": []}
    ],
    "certifications": [],
    "growth": [],
    "privacy": {"shareable": False, "redact_contact_in_examples": True},
}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: create_profile_template.py <output.json>", file=sys.stderr)
        return 2

    out = Path(sys.argv[1])
    if out.exists():
        print(f"Refusing to overwrite existing file: {out}", file=sys.stderr)
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(TEMPLATE, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
