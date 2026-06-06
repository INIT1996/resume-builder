---
name: resume-builder
description: Create, rewrite, tailor, lay out, and export resumes in the user's target language for any role or industry from interview notes, existing resumes, work histories, learning records, portfolio projects, or career-positioning conversations. Use when the user asks to make a resume/CV, optimize resume wording, package a resume-making workflow, produce HTML/DOCX/PDF resume versions, compare visual resume templates, localize a resume across languages, or adapt a resume for role families such as technology, operations, sales, marketing, product, design, finance, administration, education, customer service, manufacturing, or career-change scenarios.
---

# Resume Builder

## Overview

Use this skill to turn raw career material into a polished, position-aware resume in the user's target language for any practical job target. Preserve the user's real experience, improve expression and structure, localize wording where needed, and produce practical artifacts such as Markdown drafts, HTML previews, DOCX, PDF, and template variants when useful.

## Workflow

1. Clarify the target: output language, role, role family, seniority, city/remote preference, country/region if relevant, industry, resume audience, and whether the resume should emphasize execution, service, sales conversion, operations, analysis, creativity, compliance, coordination, management potential, or technical delivery.
2. Inventory the source material: existing resume, work history, project notes, learning records, internships, part-time jobs, campus activities, volunteer work, portfolio pieces, skills, education, certifications, links, and any constraints about privacy or length.
3. Build structured resume data before polishing prose. If starting from scratch, run `scripts/create_profile_template.py` to create a JSON skeleton, then fill it from the conversation and files.
4. Shape the strategy: choose the resume headline, summary, section order, which projects to feature, what to compress, and what to omit.
5. If the user is an industry beginner without formal projects, create truthful role-fit experience blocks from learning projects, simulated business tasks, case studies, portfolio work, coursework, certifications, internships, part-time jobs, club work, or volunteer scenarios. Label them honestly, such as "个人练习项目", "模拟业务项目", "课程项目", "作品集项目", or "校园/志愿经历"; do not fabricate employers, clients, production launches, revenue, user scale, or senior ownership.
6. Rewrite content with evidence: turn vague duties into concrete actions, tools/methods used, task context, collaboration, deliverables, service quality, process improvement, business impact, or user/customer outcomes. Do not invent metrics or responsibilities.
7. Produce the primary version first. Use the user's requested language and local resume conventions where known; prefer one clean DOCX/PDF version and optionally one HTML visual version for review.
8. Create variants only when they serve a real use case: ATS/plain, visual/interview handout, role-specific version, industry-specific version, campus recruitment version, career-change version, or bilingual version.
9. Verify final artifacts: spelling, dates, consistency, private data, print layout, text overflow, page count, and exported PDF readability.

## Writing Rules

- Write in the user's requested language. If no language is specified, match the user's conversation language; when preparing a resume for a specific country or company, adapt terminology, section names, date formats, and tone to that context.
- Use strong but truthful action verbs that match the language and role. For Chinese, examples include "负责", "参与", "跟进", "梳理", "协调", "执行", "分析", "维护", "优化", "设计", "整理", "交付", "复盘", "推动", "支持", "转化", "服务", and "落地". For English, examples include "managed", "coordinated", "analyzed", "delivered", "improved", "supported", "designed", "documented", "resolved", and "launched".
- Keep professional terms in the language that is standard for the target role or industry, such as CRM, Excel, SQL, Photoshop, Figma, ERP, SOP, KPI, ROI, Vue3, TypeScript, or ECharts.
- Prefer result-oriented bullets with this shape: action + role/industry context + method/tool/process + delivered output/impact.
- Avoid empty claims such as strong learning ability, responsibility, or familiarity with development processes unless tied to concrete evidence.
- Keep experience bullets scannable. Usually 3-5 bullets for featured work/projects and 1-2 lines for secondary items.
- Do not fabricate numbers. If impact is qualitative, state the delivered workflow, supported scenario, reuse value, stability improvement, or collaboration outcome.
- For non-IT roles, replace "项目经历" with a more natural section title when appropriate, such as "实践经历", "运营案例", "销售实践", "作品集项目", "校园经历", "服务经历", "行政支持经历", or "培训/课程项目".
- Treat personal information as sensitive. Do not place phone, email, address, ID numbers, or private links into reusable templates or public examples.

## Layout Rules

- For job applications, optimize clarity before decoration. A restrained visual style is better than a complex design that hurts scanning or printing.
- Keep the resume printable on the target market's common page size, usually A4 or Letter. Check margins, section spacing, heading hierarchy, bullet density, and whether mixed-language or long unbroken strings wrap cleanly.
- For HTML resumes, make a real resume page, not a landing page. Use stable A4 or Letter dimensions for print previews and responsive fallbacks for browser review.
- For DOCX resumes, prefer standard fonts available on Windows/macOS and test export to PDF.
- When generating multiple templates, vary layout meaningfully: concise ATS, editorial visual, sidebar compact, or project-focused. Do not create color-only duplicates.

## Resources

- Read `references/resume-workflow.md` when you need the full interview-to-artifact process.
- Read `references/resume-profile-schema.md` when you need to structure resume data or generate a JSON profile.
- Run `scripts/create_profile_template.py <output.json>` to create a blank profile skeleton for a new resume project.

## Validation

Before finishing, perform the smallest reliable checks available:

- If files were generated, confirm they exist and can be opened or rendered.
- If HTML/CSS changed, open it in a browser or use a rendering/screenshot check when possible.
- If DOCX/PDF changed, render or export and inspect page count, text overflow, and obvious encoding issues.
- Report any checks that could not be run and why.
