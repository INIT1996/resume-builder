# Resume Profile Schema

Use this structure when creating or editing a reusable resume profile. It is intentionally plain JSON so it can feed Markdown, HTML, DOCX, or other renderers.

```json
{
  "target": {
    "language": "zh-CN",
    "output_format": "html",
    "role": "",
    "role_family": "",
    "seniority": "",
    "industry": "",
    "direction": "",
    "template_style": "",
    "expected_salary": "",
    "audience": "",
    "application_type": "",
    "notes": []
  },
  "profile": {
    "name": "",
    "age": "",
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

- Keep `target.language` explicit. Use `zh-CN` by default unless the user requests another language, such as `en-US`, `en-GB`, `ja-JP`, `fr-FR`, or a plain language name supplied by the user.
- Keep `target.output_format` as `html` by default unless the user requests DOCX, PDF, Markdown, or another format.
- Use `target.direction` for the optimization focus, such as highlighting key projects, ATS keywords, wording polish, target-role change, or user-requested length compression. If the user has no direction, infer it from the resume's target role and strongest evidence, but do not infer length compression unless the user explicitly asks for a shorter version or a page limit.
- Use `target.template_style` for the requested or inferred built-in style ID: `ats-clean`, `project-focus`, `compact-sidebar`, `visual-editorial`, `ink-wash`, or `neon-portfolio`.
- Use `target.expected_salary` when the user provides a salary expectation. Omit it from the final resume if it would weaken the application or the local convention does not call for it.
- Use `profile.age` only when the user provides it or the target market convention makes it useful. Treat it as private information.
- Keep `summary` as 2-4 bullet-like sentences, not a long paragraph.
- Keep `target.role_family` broad and practical, such as `technology`, `operations`, `sales`, `marketing`, `product`, `design`, `finance`, `administration`, `hr`, `customer_service`, `education`, `manufacturing`, or `general`.
- Keep `skills.items` factual and supported by work, projects, study, practice, or portfolio evidence. Skills can be manually supplied by the user or extracted from `projects.tech`, `projects.tools`, `projects.methods`, `projects.bullets`, `experience_blocks.tools`, and `experience_blocks.bullets`.
- For technical resumes, derive the tech stack primarily from project experience, then group and deduplicate it in `skills`; do not list unsupported frameworks or tools only because they match the target job.
- Use `projects` for conventional project work. Keep `tech` for technical resumes; use `tools` and `methods` for any role.
- Use `experience_blocks` for beginner-friendly or non-project material, such as simulated business tasks, coursework, portfolio cases, internships, part-time jobs, campus work, volunteer work, or role-fit practice.
- Label beginner items honestly through `type`, such as `个人练习项目`, `模拟业务项目`, `课程项目`, `作品集项目`, `校园经历`, or `志愿服务经历`.
- Keep `projects.context` and `experience_blocks.context` as internal drafting material; final resume may omit them.
- Use `privacy.shareable=false` unless the user explicitly says the profile can be reused as an example.
