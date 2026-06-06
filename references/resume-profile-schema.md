# Resume Profile Schema

Use this structure when creating or editing a reusable resume profile. It is intentionally plain JSON so it can feed Markdown, HTML, DOCX, or other renderers.

```json
{
  "target": {
    "role": "",
    "seniority": "",
    "direction": "",
    "audience": "",
    "notes": []
  },
  "profile": {
    "name": "",
    "headline": "",
    "city": "",
    "phone": "",
    "email": "",
    "links": [],
    "summary": []
  },
  "skills": [
    {
      "group": "",
      "items": []
    }
  ],
  "work": [
    {
      "company": "",
      "role": "",
      "date": "",
      "bullets": []
    }
  ],
  "projects": [
    {
      "name": "",
      "date": "",
      "role": "",
      "tech": [],
      "context": "",
      "bullets": [],
      "tags": []
    }
  ],
  "education": [
    {
      "school": "",
      "degree": "",
      "major": "",
      "date": "",
      "notes": []
    }
  ],
  "certifications": [],
  "growth": [],
  "privacy": {
    "shareable": false,
    "redact_contact_in_examples": true
  }
}
```

Guidelines:

- Keep `summary` as 2-4 bullet-like sentences, not a long paragraph.
- Keep `skills.items` factual and supported by projects.
- Keep `projects.context` as internal drafting material; final resume may omit it.
- Use `privacy.shareable=false` unless the user explicitly says the profile can be reused as an example.
