# Built-in HTML Resume Templates

Use this catalog when the user wants to choose a resume template style, or when the resume should default to an appropriate built-in HTML style.

Default rule: ask the user to choose one of these styles after confirming whether they already have a resume. If the user has no preference, choose the safest role-fit option and briefly explain why.

All templates must follow the HTML print rules in `SKILL.md`: Chinese by default, A4 by default, no typos, even spacing, no page-break gaps, no cramped page-edge content, and no text clipping.

## Template Options

| ID | Name | Best For | Visual Direction | Layout |
| --- | --- | --- | --- | --- |
| `ats-clean` | 简洁 ATS | Most job applications, HR screening, conservative industries | White paper, restrained blue-gray accents | Single-column, dense but readable |
| `project-focus` | 项目突出 | Technology, product, design, engineering, portfolio-heavy candidates | Iridescent cyan/blue with subtle magenta accent | Strong header, highlight metrics, project cards |
| `compact-sidebar` | 侧栏紧凑 | Candidates with many skills, certificates, tools, or contact details | Muted olive paper, editorial restraint | Left sidebar + main timeline |
| `visual-editorial` | 视觉编辑 | Marketing, design, operations, creative roles, interview handouts | Frosted glass, gray-white depth, warm accent | Magazine-like header + elegant sections |
| `ink-wash` | 山水纸感 | Education, culture, public sector, Chinese-style formal resumes | Pale ink blue, ivory paper, subtle gold | Calm editorial sections |
| `neon-portfolio` | 霓虹作品集 | Creative technology, visual design, new media, portfolio presentation | Black base, neon green/cyan accent | Bold cover band + gallery-like project blocks |

## Selection Guidance

- Choose `ats-clean` when the user wants the safest delivery or has no style preference.
- Choose `project-focus` when key projects should be the visual and content center.
- Choose `compact-sidebar` when the resume has many skills/tools but must stay compact.
- Choose `visual-editorial` when the user wants a more advanced, high-end handout without hurting readability.
- Choose `ink-wash` when the resume benefits from a quiet Chinese editorial tone.
- Choose `neon-portfolio` only for creative/portfolio scenarios; do not use it for conservative HR delivery unless the user asks.

## User-facing Choice Text

When offering templates, use concise Chinese copy:

> 你可以选一个模板风格：  
> 1. 简洁 ATS：稳妥投递，HR 友好。  
> 2. 项目突出：适合技术/产品/作品集，重点项目更醒目。  
> 3. 侧栏紧凑：信息多但想控制页数。  
> 4. 视觉编辑：更高级，适合面试展示或内推。  
> 5. 山水纸感：克制、东方感，适合正式或文化类场景。  
> 6. 霓虹作品集：强视觉，适合作品集/创意方向。  
> 没有偏好我会按岗位自动选择。

## CSS Usage

Use `assets/builtin-template-styles.css` as the style source. Wrap the resume with:

```html
<article class="resume-page resume-template resume-template--project-focus">
  ...
</article>
```

For a different template, replace the modifier class:

- `resume-template--ats-clean`
- `resume-template--project-focus`
- `resume-template--compact-sidebar`
- `resume-template--visual-editorial`
- `resume-template--ink-wash`
- `resume-template--neon-portfolio`

Recommended generic structure:

```html
<article class="resume-page resume-template resume-template--ats-clean">
  <header class="resume-hero">...</header>
  <main class="resume-body">
    <section class="resume-section">...</section>
  </main>
</article>
```

Use optional utility classes where appropriate:

- `.resume-grid`: two-column body layout.
- `.resume-sidebar`: sidebar area.
- `.resume-main`: main content area.
- `.resume-card`: work/project block.
- `.resume-tags`: tag list.
- `.resume-metrics`: metric row.

Do not force every template into the same structure. Use the CSS as a style system and adapt the HTML layout to the candidate's content.
