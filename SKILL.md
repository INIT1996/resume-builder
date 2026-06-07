---
name: resume-builder
description: Create, rewrite, tailor, lay out, and export Chinese-first HTML resumes for any role or industry from existing resumes, interview notes, work histories, learning records, portfolio projects, or career-positioning conversations. Use when the user asks to make a resume/CV, optimize resume wording, highlight key projects, choose a resume template style, package a resume-making workflow, produce a single editable HTML resume, localize resume content across languages, or adapt a resume for role families such as technology, operations, sales, marketing, product, design, finance, administration, education, customer service, manufacturing, or career-change scenarios.
---

# Resume Builder

## Overview

Use this skill to turn raw career material into a polished, position-aware resume for any practical job target. Preserve the user's real experience, improve expression and structure, localize wording where needed, and produce one practical resume artifact. Unless the user explicitly specifies otherwise, write the resume in Chinese and deliver a single editable HTML file. Do not create JSON, DOCX, PDF, Markdown, or other side artifacts by default.

## Workflow

1. Start by asking whether the user already has a resume. Keep intake conversational: ask one question at a time, or at most 2-3 closely related questions, so the user never feels they must fill a long form before progress starts.
2. If the user has a resume, ask them to provide the file or paste the content first. After reading it, ask for the optimization direction; ask for template style later only when visual direction matters. Optimization directions can include highlighting key projects, strengthening role-fit keywords, improving ATS readability, polishing wording, changing target roles, or making a more visual interview handout. Only compress length, remove sections, or reduce bullets when the user explicitly asks for compression, a page limit, or a shorter version. If the user has no clear direction, infer the optimization strategy from the target role or job-seeking information already present in the resume; if the target role is missing, ask only for the target role.
3. If the user does not have a resume, collect information progressively instead of asking for all fields at once. Start with the target role and one or two essential profile details, then continue in small steps: contact details, city/region, education, expected salary if relevant, links/certificates, and experience material. Ask whether they have work experience only after the basic direction is clear; if yes, let them summarize it in one sentence and expand it truthfully. If no, ask one category at a time for internships, part-time work, campus activities, coursework, practice projects, portfolio pieces, or learning records that can become honest experience blocks.
4. Default to Chinese language and a single HTML output unless the user asks for another language. Before final HTML generation, present the built-in template styles and ask the user to choose the resume style. Do not choose the visual style on the user's behalf. If the user says they have no preference, ask them to confirm the default `ats-clean` style instead of inferring a role-fit style.
5. Organize the resume structure internally before polishing prose. Do not generate or deliver a JSON profile unless the user explicitly asks for one.
6. Extract role-fit skills from evidence before writing the skills section. For technical resumes, derive the tech stack from project names, `projects.tech`, tools, methods, responsibilities, bullets, and deliverables; for non-technical resumes, derive tools, methods, domain knowledge, and soft skills from work/practice evidence. Keep only skills that can be supported by at least one experience item.
7. Shape the strategy: choose the resume headline, summary, section order, and which projects or experience blocks to feature. When optimizing an existing resume, deliberately identify the strongest 1-3 projects or experiences and make them more prominent while preserving the original substance by default. Do not compress, omit, or substantially shorten existing content unless the user explicitly requests it or approves that tradeoff.
8. If the user is an industry beginner without formal projects, create truthful role-fit experience blocks from learning projects, simulated business tasks, case studies, portfolio work, coursework, certifications, internships, part-time jobs, club work, or volunteer scenarios. Label them honestly, such as "个人练习项目", "模拟业务项目", "课程项目", "作品集项目", or "校园/志愿经历"; do not fabricate employers, clients, production launches, revenue, user scale, or senior ownership.
9. Rewrite content with evidence: turn vague duties into concrete actions, tools/methods used, task context, collaboration, deliverables, service quality, process improvement, business impact, or user/customer outcomes. Do not invent metrics or responsibilities.
10. Produce one editable HTML resume as the final deliverable. Do not create DOCX/PDF, ATS/plain, role-specific, industry-specific, campus recruitment, career-change, bilingual, JSON, or additional visual variants unless the user explicitly asks for them.
11. Verify the final HTML artifact: spelling, dates, consistency, private data, browser readability, print layout, text overflow, and A4 page behavior.

## Writing Rules

- Write in the user's requested language. If no language is specified, default to Chinese; when preparing a resume for a specific country or company, adapt terminology, section names, date formats, and tone to that context.
- Use strong but truthful action verbs that match the language and role. For Chinese, examples include "负责", "参与", "跟进", "梳理", "协调", "执行", "分析", "维护", "优化", "设计", "整理", "交付", "复盘", "推动", "支持", "转化", "服务", and "落地". For English, examples include "managed", "coordinated", "analyzed", "delivered", "improved", "supported", "designed", "documented", "resolved", and "launched".
- Keep professional terms in the language that is standard for the target role or industry, such as CRM, Excel, SQL, Photoshop, Figma, ERP, SOP, KPI, ROI, Vue3, TypeScript, or ECharts.
- Prefer result-oriented bullets with this shape: action + role/industry context + method/tool/process + delivered output/impact.
- Avoid empty claims such as strong learning ability, responsibility, or familiarity with development processes unless tied to concrete evidence.
- Do not list a skill or tech stack item just because it sounds relevant. Prefer skills extracted from project/work evidence, and remove unsupported items unless the user explicitly confirms real proficiency.
- Keep experience bullets scannable. Usually 3-5 bullets for featured work/projects and 1-2 lines for secondary items.
- Do not fabricate numbers. If impact is qualitative, state the delivered workflow, supported scenario, reuse value, stability improvement, or collaboration outcome.
- For non-IT roles, replace "项目经历" with a more natural section title when appropriate, such as "实践经历", "运营案例", "销售实践", "作品集项目", "校园经历", "服务经历", "行政支持经历", or "培训/课程项目".
- Treat personal information as sensitive. Do not place phone, email, address, ID numbers, or private links into reusable templates or public examples.

## Layout Rules

- For job applications, optimize clarity before decoration. A restrained visual style is better than a complex design that hurts scanning or printing.
- HTML resume output must be free of typos, wrong characters, obvious grammar mistakes, and accidental encoding artifacts. Carefully proofread names, company/project names, dates, role titles, section headings, and technical terms.
- Keep text spacing and module spacing visually even. Line height, paragraph spacing, bullet spacing, card padding, section gaps, and page margins should follow a consistent rhythm; avoid layouts where some areas feel overly loose while others look cramped.
- Strictly size the default HTML print layout for A4 paper unless the user explicitly requests another paper size. Use A4 dimensions for print CSS (`@page size: A4`) and page simulation, then check margins, section spacing, heading hierarchy, bullet density, and whether mixed-language or long unbroken strings wrap cleanly within that A4 frame.
- For HTML resumes, make a real resume page, not a landing page. Use stable A4 dimensions for print previews and responsive fallbacks for browser review. HTML is the default and only normal output format.
- For resumes that may exceed one A4 page, use JavaScript-assisted pagination after rendering: measure the actual rendered content height, compare it with the available A4 content height after page padding, then split content into separate `.resume-page` elements before final review. Do not only calculate large modules. If a large card or section does not fit but the current page still has useful space, split the next module by the current page's remaining height and move only the amount that actually fits upward. If the remaining height can only fit one line, split the first text item by measured height, move that one line upward, and keep the rest of the text plus the remaining module content as one continuation block. Split fragments must preserve the original visual system, including card border/background, accent edge, bullet indentation, spacing rhythm, and continuation styling; do not output bare text fragments. Avoid repeatedly splitting the same header or generating multiple continuation labels for one module. If the first fragment narrowly does not fit, try a compact page-fragment style before opening a new page.
- Avoid visible page-break gaps in HTML print output. Do not make large resume sections, project lists, or oversized cards fully unbreakable if doing so leaves a large blank area at the bottom of a page. Apply `break-inside: avoid` only to small units that should stay together, such as a heading with its first bullet, a short experience item, or a compact tag row. If a project/experience block is too tall for the remaining page space, split it naturally, adjust spacing, or move only the heading-safe portion so the printed pages stay visually continuous. For existing resumes, do not shorten bullets or remove content to fix pagination unless the user explicitly requests or approves content compression.
- Add natural breathing room around HTML page breaks. In print preview or paged-screen simulation, content should not sit flush against the top or bottom page edge. Use page padding/margins, section spacing, `break-before`/`break-after` adjustments, or small continuation spacing so headings, company names, project titles, and first bullets do not appear cramped at a page boundary.
- When generating multiple templates, vary layout meaningfully: concise ATS, editorial visual, sidebar compact, or project-focused. Do not create color-only duplicates.

## Resources

- Read `references/resume-workflow.md` when you need the full interview-to-artifact process.
- Read `references/resume-template-catalog.md` when presenting built-in template styles for the user to choose.
- Read `references/html-pagination.md` when building or fixing multi-page HTML resumes, page-break gaps, missing page margins, content clipping, repeated continuation headers, inconsistent split-fragment formatting, or A4 print behavior.
- Use `examples/pagination-stress-test.html` as a local regression sample when changing the pagination logic.
- Use `assets/builtin-template-styles.css` as the built-in CSS source for HTML resume templates. Apply one of these modifier classes on `.resume-template`: `resume-template--ats-clean`, `resume-template--project-focus`, `resume-template--compact-sidebar`, `resume-template--visual-editorial`, `resume-template--ink-wash`, or `resume-template--neon-portfolio`.

## Validation

Before finishing, perform the smallest reliable checks available:

- If files were generated, confirm they exist and can be opened or rendered.
- If HTML/CSS changed, open it in a browser or use a rendering/screenshot check when possible. For printable HTML, specifically inspect page boundaries, proofread visible text, and fix large blank gaps, uneven text/module spacing, cramped page-edge content, orphaned headings, clipped content, and awkward page breaks before finishing.
- Report any checks that could not be run and why.
