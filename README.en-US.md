# Resume Builder Skill

[中文](README.md) | English

Resume Builder is a Codex skill for creating, rewriting, tailoring, laying out, and localizing resumes. It turns an existing resume, basic profile information, interview notes, learning records, work history, or project material into a clearer resume that better fits a target role.

By default, the skill writes resumes in Chinese and produces one editable HTML file. It can use English or another language when the user asks for it.

## What It Does

- Create resumes from scratch.
- Improve the structure, wording, keywords, and project presentation of an existing resume.
- Tailor resume versions for different roles, industries, regions, and audiences.
- Turn scattered experience into work, project, practice, or portfolio sections.
- Help students, beginners, interns, and career changers organize coursework, practice projects, simulated business projects, or portfolio work.
- Generate a single browser-readable and A4-printable HTML resume.

## Principles

- Improve the user's real material without adding unsupported experience, data, or skills.
- When optimizing an existing resume, preserve its original substance by default; compress length or remove content only when the user explicitly asks for it.
- Organize resume structure and role focus before polishing individual lines.
- Keep skills, tools, and project descriptions grounded in experience, coursework, portfolio work, or actual outputs.
- Prioritize clarity, readability, submission quality, and print quality before visual decoration.
- Keep contact details and private information only in final private deliverables, not in reusable examples or public templates.

## Project Structure

```text
resume-builder/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── builtin-template-styles.css
├── references/
│   ├── resume-profile-schema.md
│   ├── resume-template-catalog.md
│   └── resume-workflow.md
└── scripts/
    └── create_profile_template.py
```

## Files

- `resume-builder/SKILL.md`: Main skill entry with trigger scope, workflow, writing rules, layout rules, and validation requirements.
- `resume-builder/references/resume-workflow.md`: Full workflow for intake, strategy, rewriting, artifact generation, and final review.
- `resume-builder/references/resume-template-catalog.md`: Built-in HTML template catalog and selection guidance.
- `resume-builder/assets/builtin-template-styles.css`: Built-in style system for HTML resumes.
- `resume-builder/agents/openai.yaml`: Display metadata for Codex/OpenAI environments.

## Installation

Place the whole `resume-builder/` directory in your Codex skills directory. A common target is `$CODEX_HOME/skills/resume-builder`.

You can also give this project URL, [INIT1996/resume-builder](https://github.com/INIT1996/resume-builder), to Codex or another AI assistant and say:

```text
Please install this resume-builder skill for me: https://github.com/INIT1996/resume-builder
```

If the assistant can access local files or fetch the project, it can copy the `resume-builder/` directory into the right skills directory for you.

In PowerShell:

```powershell
$skillsDir = Join-Path $env:CODEX_HOME "skills"
New-Item -ItemType Directory -Force $skillsDir
Copy-Item -Recurse -Force .\resume-builder $skillsDir
```

After installation, restart Codex or refresh the available skills. Then mention `resume-builder` or `$resume-builder` in a conversation.

## Usage

In Codex, trigger the skill with:

```text
Use $resume-builder to ask whether I already have a resume, then create or optimize a Chinese HTML resume.
```

The skill first asks whether the user already has a resume, then produces one HTML file by default:

- If yes: provide the file or paste the content, then describe the optimization goal and template preference.
- If no: start with the target role and basic context, then progressively collect contact details, education, work, internship, coursework, practice projects, or campus experience.

## Print And Export PDF

The skill generates an HTML resume by default. To export a PDF, open the generated HTML file in a browser, press `Ctrl+P`, then choose “Save as PDF” or “Print to PDF”.

Use A4 paper settings when possible. Keep the default scale first, check that the preview has no clipped or overlapping text, then save the PDF.

## Built-In Templates

HTML resumes can use these built-in template styles:

| ID | Best For |
| --- | --- |
| `ats-clean` | Conservative submissions, HR screening, traditional industries, and highly readable resumes |
| `project-focus` | Technology, product, design, engineering, and project-heavy profiles |
| `compact-sidebar` | Candidates with many skills, certificates, or tools who still need a compact layout |
| `visual-editorial` | Interview handouts, referrals, operations, design, marketing, and expression-heavy scenarios |
| `ink-wash` | Education, culture, public service, or formal Chinese-language contexts |
| `neon-portfolio` | Visual design, new media, creative technology, and portfolio presentation |

If the user has no preference, choose the safest role-fit template.

## Local Check

```powershell
Get-Content -Raw -Encoding UTF8 resume-builder\SKILL.md
Test-Path resume.html
```

This confirms that the skill instructions are readable and that the repository includes an HTML example.

## Maintenance Notes

- Keep the skill itself concise: put core workflow in `SKILL.md`, and detailed workflows and template guidance in `references/`.
- Do not add README files, installation guides, or extra auxiliary documents inside the `resume-builder/` folder.
- Keep the default user deliverable as HTML only.
- When adding templates, make the layout meaningfully different instead of changing only colors.
- Use UTF-8 for Chinese documentation. In PowerShell, read Chinese Markdown files with `-Encoding UTF8`.
