<div align="center">

# Resume Builder Skill

**[中文](README.md) | English**

A resume creation and optimization skill for Codex. It helps turn existing resumes, profile notes, interview records, learning history, work experience, or project material into a clearer HTML resume tailored to a target role.

</div>

## Overview

Resume Builder is a Codex skill for creating and improving resumes. It organizes resume content around a target role, sharpens the presentation, and produces an editable HTML resume that can be viewed in a browser and printed on A4 paper.

The `resume-builder/` directory includes:

- `SKILL.md`: Main skill entry with trigger scope, workflow, writing rules, layout rules, and validation requirements.
- `agents/`: Display configuration for Codex/OpenAI environments.
- `assets/`: Built-in style assets used by the skill.
- `examples/`: Pagination and HTML resume examples.
- `references/`: Workflow, template catalog, pagination rules, and profile schema references.
- `scripts/`: Helper scripts.

## What It Does

- Create resumes from scratch.
- Improve the structure, wording, keywords, and project presentation of an existing resume.
- Adjust content focus for different roles, industries, regions, and audiences.
- Turn scattered experience into work, project, practice, coursework, or portfolio sections.
- Help students, interns, beginners, and career changers express real experience in a credible way.
- Generate a paginated HTML resume suitable for browser reading and A4 printing.

## Principles

- When optimizing an existing resume, preserve its original substance by default; compress length or remove content only when the user explicitly asks for it.
- Organize resume structure, role focus, and evidence before polishing individual lines.
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
├── examples/
│   ├── pagination-stress-test.html
│   └── sample-resume-pagination.html
├── references/
│   ├── html-pagination.md
│   ├── resume-profile-schema.md
│   ├── resume-template-catalog.md
│   └── resume-workflow.md
└── scripts/
    └── create_profile_template.py
```

## Installation

Place the whole `resume-builder/` directory in your Codex skills directory. A common target is:

```text
$CODEX_HOME/skills/resume-builder
```

In PowerShell:

```powershell
$skillsDir = Join-Path $env:CODEX_HOME "skills"
New-Item -ItemType Directory -Force $skillsDir
Copy-Item -Recurse -Force .\resume-builder $skillsDir
```

After installation, restart Codex or refresh the available skills. Then mention `resume-builder` or `$resume-builder` in a conversation to trigger it.

You can also give this project URL to Codex or another AI assistant and say:

```text
Please install this resume-builder skill for me: https://github.com/INIT1996/resume-builder
```

## Usage

In Codex, start with a prompt like:

```text
Use resume-builder to help me create a resume.
```

The skill first asks whether the user already has a resume:

- If yes: provide the file or paste the content, then describe the optimization goal, target role, and template preference.
- If no: start with the target role and basic context, then progressively collect contact details, education, work experience, internships, coursework, practice projects, or campus experience.

By default, the workflow asks the user to choose a built-in template style before final HTML generation. If the user has no preference, it asks them to confirm the default `ats-clean` style.

## Built-In Templates

HTML resumes can use these built-in template styles:

| ID | Name | Best For |
| --- | --- | --- |
| `ats-clean` | Clean ATS | Conservative submissions, HR screening, traditional industries, and highly readable resumes |
| `project-focus` | Project Focus | Technology, product, design, engineering, and project-heavy profiles |
| `compact-sidebar` | Compact Sidebar | Candidates with many skills, certificates, or tools who still need a compact layout |
| `visual-editorial` | Visual Editorial | Interview handouts, referrals, operations, design, marketing, and expression-heavy scenarios |
| `ink-wash` | Ink Wash | Education, culture, public service, or formal Chinese-language contexts |
| `neon-portfolio` | Neon Portfolio | Visual design, new media, creative technology, and portfolio presentation |

Template selection and CSS usage rules are documented in `resume-builder/references/resume-template-catalog.md`.

## Print And Export PDF

The skill generates an HTML resume by default. To export a PDF, open the generated HTML file in a browser, press `Ctrl+P`, then choose “Save as PDF” or “Print to PDF”.

Use A4 paper settings when possible. Before saving, check:

- Page margins are visible and consistent.
- Text is not clipped.
- Sections do not overlap.
- Page breaks do not leave large blank gaps or orphaned headings.

## Local Preview

Open the examples under `resume-builder/examples/` to inspect the A4 pagination structure and print behavior.

## Maintenance Notes

- Keep the skill itself concise: put core workflow in `resume-builder/SKILL.md`, and detailed workflows and template guidance in `resume-builder/references/`.
- Keep the default user deliverable as HTML only unless the user explicitly asks for DOCX, PDF, Markdown, or another format.
- When adding templates, make the layout meaningfully different instead of changing only colors.
- When changing pagination logic, start from `resume-builder/references/html-pagination.md` and use `resume-builder/examples/pagination-stress-test.html` as a regression sample.
- Use UTF-8 for Chinese documentation. In PowerShell, read Chinese Markdown files with `-Encoding UTF8`.

## Local Checks

```powershell
Get-Content -Raw -Encoding UTF8 resume-builder\SKILL.md
Get-Content -Raw -Encoding UTF8 README.en-US.md
Test-Path resume-builder\examples\pagination-stress-test.html
```

These checks confirm that the skill instructions, English README, and pagination example exist and can be read.
