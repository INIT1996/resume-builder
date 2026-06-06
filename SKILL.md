---
name: resume-builder
description: Create, rewrite, tailor, lay out, and export Chinese technical resumes from interview notes, existing resumes, project histories, or career-positioning conversations. Use when the user asks to make a resume/CV, optimize resume wording, package a resume-making workflow, produce HTML/DOCX/PDF resume versions, compare visual resume templates, or adapt a resume for frontend/full-stack/product-oriented roles.
---

# Resume Builder

## Overview

Use this skill to turn raw career material into a polished, position-aware Chinese technical resume. Preserve the user's real experience, improve expression and structure, and produce practical artifacts such as Markdown drafts, HTML previews, DOCX, PDF, and template variants when useful.

## Workflow

1. Clarify the target: role, seniority, city/remote preference, industry, whether the resume should emphasize delivery, product sense, full-stack growth, AI tooling, or management potential.
2. Inventory the source material: existing resume, project notes, work history, skills, education, certifications, links, and any constraints about privacy or length.
3. Build structured resume data before polishing prose. If starting from scratch, run `scripts/create_profile_template.py` to create a JSON skeleton, then fill it from the conversation and files.
4. Shape the strategy: choose the resume headline, summary, section order, which projects to feature, what to compress, and what to omit.
5. Rewrite content with evidence: turn vague duties into concrete actions, technology choices, business flow ownership, collaboration, delivery outcomes, and user-facing impact. Do not invent metrics or responsibilities.
6. Produce the primary version first. For Chinese tech resumes, prefer one clean DOCX/PDF version and optionally one HTML visual version for review.
7. Create variants only when they serve a real use case: ATS/plain, visual/interview handout, role-specific version, or bilingual version.
8. Verify final artifacts: spelling, dates, consistency, private data, print layout, text overflow, page count, and exported PDF readability.

## Writing Rules

- Write in concise Chinese by default. Keep English technical terms where they are standard: Vue3, TypeScript, UniApp, WebRTC, ECharts, Electron, Nginx.
- Use strong but truthful Chinese action verbs such as "responsible for", "led", "participated in", "decomposed", "integrated", "encapsulated", "optimized", "delivered", "maintained", and "promoted" translated naturally into Chinese.
- Prefer result-oriented bullets with this shape: action + technical/business context + delivered capability/impact.
- Avoid empty claims such as strong learning ability, responsibility, or familiarity with development processes unless tied to concrete evidence.
- Keep project bullets scannable. Usually 3-5 bullets for featured projects and 1-2 lines for secondary projects.
- Do not fabricate numbers. If impact is qualitative, state the delivered workflow, supported scenario, reuse value, stability improvement, or collaboration outcome.
- Treat personal information as sensitive. Do not place phone, email, address, ID numbers, or private links into reusable templates or public examples.

## Layout Rules

- For job applications, optimize clarity before decoration. A restrained visual style is better than a complex design that hurts scanning or printing.
- Keep the resume printable on A4. Check margins, section spacing, heading hierarchy, bullet density, and whether long Chinese/English mixed strings wrap cleanly.
- For HTML resumes, make a real resume page, not a landing page. Use stable A4 dimensions for print previews and responsive fallbacks for browser review.
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
