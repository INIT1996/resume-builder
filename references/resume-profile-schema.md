# Resume Profile Schema

Use this structure when creating or editing a reusable resume profile. It is intentionally plain JSON so it can feed Markdown, HTML, DOCX, or other renderers.

```json
{
  "target": {
    "role": "",
    "role_family": "",
    "seniority": "",
    "industry": "",
    "direction": "",
    "audience": "",
    "application_type": "",
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
      "type": "",
      "tech": [],
      "tools": [],
      "methods": [],
      "context": "",
      "bullets": [],
      "tags": []
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
- Keep `target.role_family` broad and practical, such as `technology`, `operations`, `sales`, `marketing`, `product`, `design`, `finance`, `administration`, `hr`, `customer_service`, `education`, `manufacturing`, or `general`.
- Keep `skills.items` factual and supported by work, projects, study, practice, or portfolio evidence.
- Use `projects` for conventional project work. Keep `tech` for technical resumes; use `tools` and `methods` for any role.
- Use `experience_blocks` for beginner-friendly or non-project material, such as simulated business tasks, coursework, portfolio cases, internships, part-time jobs, campus work, volunteer work, or role-fit practice.
- Label beginner items honestly through `type`, such as `个人练习项目`, `模拟业务项目`, `课程项目`, `作品集项目`, `校园经历`, or `志愿服务经历`.
- Keep `projects.context` and `experience_blocks.context` as internal drafting material; final resume may omit them.
- Use `privacy.shareable=false` unless the user explicitly says the profile can be reused as an example.
