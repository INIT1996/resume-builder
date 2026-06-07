# Resume Workflow

## Intake

Collect only what is needed for the target resume. The first question should be whether the user already has a resume. Then follow the matching intake path and ask for missing material progressively. Ask one question at a time, or at most 2-3 closely related questions, instead of presenting a long form.

Default assumptions:

- Language: Chinese, unless the user asks for another language.
- Primary artifact: one editable HTML resume file. Do not create JSON, DOCX, PDF, Markdown, or other side artifacts unless the user explicitly asks for them.
- Template style: the user chooses the style. Before final HTML generation, offer the built-in choices from `resume-template-catalog.md`. Do not choose a style based only on role or scenario. If the user has no preference, ask them to confirm the default `ats-clean` style.

Existing resume path:

1. Ask the user to upload/provide the resume file or paste the content.
2. After reading the resume, ask for the optimization direction, such as highlighting key projects, strengthening target-role keywords, improving ATS readability, polishing expression, changing target roles, or making a visual interview handout. Treat length compression as opt-in: only shorten, remove sections, or reduce bullets when the user explicitly asks for compression, a page limit, or a shorter version.
3. Ask for preferred template style after the optimization direction is clear and before final HTML generation: 简洁 ATS (`ats-clean`), 项目突出 (`project-focus`), 侧栏紧凑 (`compact-sidebar`), 视觉编辑 (`visual-editorial`), 山水纸感 (`ink-wash`), 霓虹作品集 (`neon-portfolio`), or another style the user describes. Do not choose for the user; if they have no preference, ask whether to use `ats-clean` as the default.
4. If the user has no optimization direction, infer it from the resume's target role, job-seeking information, strongest projects, and visible gaps. If the target role is not present, ask only for the target role before optimizing.
5. Identify the strongest 1-3 projects or experiences and decide how to make them more prominent without reducing the original substance by default.

No resume path:

1. Start with the target role and one or two essential profile details. Do not ask for name, age, phone, email, city, school, degree, major, expected salary, links, and certificates all at once.
2. Progressively collect missing basics in small turns: contact method, city/region, education, expected salary if relevant, links, and certificates.
3. Ask whether the user has work experience only after the basic direction is clear.
4. If they have work experience, let them summarize it in one sentence first, then ask only for missing dates, company/role names, responsibilities, tools, and outcomes needed to make the resume truthful and useful.
5. If they do not have work experience, collect internships, part-time work, campus activities, coursework, practice projects, portfolio pieces, learning records, or certificates one category at a time.
6. Use AI-assisted polishing to expand short notes into role-fit bullets, but do not invent employers, commercial clients, production launches, metrics, responsibilities, or seniority.

Useful prompts:

- 你现在有现成简历吗？如果有，可以直接发文件或粘贴内容；如果没有，我先帮你从基础信息搭一版。
- 如果已有简历，你希望这次重点优化什么？例如突出重点项目、改投新岗位、增强关键词、润色表达、换模板风格，或者你也可以说“没有方向”，我会按简历里的求职岗位自行判断。默认不会压缩篇幅；如果你需要压缩到一页或做短版，请明确告诉我。
- 你喜欢哪种模板风格：简洁 ATS、项目突出、侧栏紧凑、视觉编辑、山水纸感、霓虹作品集，还是其他风格？如果没有偏好，我可以使用默认的简洁 ATS，你确认一下即可。
- 如果没有简历，我们先从最关键的开始：你想投什么岗位？所在城市或目标城市是哪里？
- 你是否有工作经验？有的话先用一句话概括就行，例如“做过 2 年前端开发，主要负责后台系统和小程序”。
- 目标岗位是什么？属于技术、运营、销售、市场、产品、设计、行政、人事、财务、客服、教育、制造、服务业，还是其他方向？
- 目标语言和投递地区是否需要改动？默认使用中文、中国大陆简历习惯；也可以改成英文、美国；英文、新加坡；日文、日本；或其他任意语言/地区组合。
- 这份简历主要投递给谁看：HR、业务负责人、技术/专业面试官、熟人内推、校招渠道，还是兼职/实习机会？
- 如果没有工作经验，我们先看一个方向：你有没有实习、兼职、课程项目、校园经历或个人练习？随便说一个最像经历的就行。
- 如果没有正式项目，我会按目标岗位一步步帮你找可展示的练习或作品，不需要一次列全。
- 有没有必须保留、弱化或不能公开的信息？

## Content Strategy

Choose a resume angle before writing. The angle should match the target role family:

- 执行交付型：强调任务拆解、按期完成、跨角色协作、问题跟进、稳定输出。
- 服务支持型：强调用户/客户沟通、响应效率、问题闭环、满意度意识、耐心和规范。
- 销售转化型：强调客户开发、需求挖掘、跟进节奏、成交辅助、复盘和话术优化。
- 运营增长型：强调内容/活动/社群/数据复盘、流程搭建、用户触达、转化或留存。
- 行政人事型：强调流程规范、资料管理、会议/招聘/培训支持、细致度和保密意识。
- 财务分析型：强调数据整理、报表、凭证/对账、Excel/系统工具、准确性和合规。
- 设计创意型：强调需求理解、视觉表达、作品集、工具熟练度、迭代反馈和交付质量。
- 教育培训型：强调课程准备、学生沟通、学习反馈、课堂执行、教研或辅导成果。
- 技术研发型：强调需求拆解、工程实现、工具/框架、质量、性能、协作和上线维护。
- 转行成长型：强调可迁移能力、学习路径、可展示作品、岗位相关练习和清晰动机。

## Skill Extraction

Build the skills section from evidence, not from a generic keyword list.

For technical resumes:

- Extract the tech stack from project names, `projects.tech`, tools, methods, bullets, deliverables, code repositories, and implementation descriptions.
- Group extracted items by practical meaning, such as frontend, backend, data, testing, deployment, design tools, collaboration tools, or domain systems.
- Keep only items the user actually used or can explain. If a project only mentions a tool casually, treat it as a weak signal until confirmed.
- Prefer supported wording: "Vue3 / TypeScript / Element Plus" is stronger when a project bullet explains what was built with them.

For non-technical resumes:

- Extract role-fit skills from work and practice evidence, such as Excel reporting, CRM follow-up, SOP documentation, customer communication, content planning, event execution, visual design, teaching preparation, or inventory management.
- Keep tools and methods close to the experience that proves them.

When the extracted skill list is too long, prioritize items that are recent, repeated across multiple experiences, required by the target role, or tied to stronger deliverables.

## Beginner Experience Blocks

When the user is an industry beginner without formal projects, add truthful experience blocks instead of fake company projects.

Recommended labels:

- 个人练习项目
- 模拟业务项目
- 课程项目
- 作品集项目
- 实习/兼职经历
- 校园/社团经历
- 志愿服务经历
- 岗位能力训练

Examples by role:

- 销售：模拟客户开发清单、产品卖点梳理、跟进话术设计、异议处理复盘。
- 运营：小红书/公众号内容选题表、社群活动方案、用户问卷分析、活动复盘报告。
- 行政：会议纪要模板、档案整理流程、物资台账、面试邀约与接待流程。
- 财务：Excel 费用台账、模拟对账、基础凭证整理、经营数据汇总。
- 客服：常见问题知识库、投诉处理流程、服务话术优化、工单分类复盘。
- 设计：海报/详情页/品牌视觉练习、改版案例、Figma/PS 作品集。
- 教育：试讲教案、学生错题分析、课程讲义、学习反馈记录。
- 技术：管理系统、数据看板、小程序、自动化脚本、接口/数据库练习。

Never present these as real employment, client delivery, production launch, commercial revenue, or large-scale user impact unless the user provides evidence.

## Recommended Section Order

Use the order that makes the strongest truthful evidence appear early.

General experienced candidate:

1. Name, target role, contact
2. Profile summary
3. Core skills
4. Work experience
5. Featured projects/practice/cases
6. Education/certifications
7. Additional information

Beginner or career-change candidate:

1. Name, target role, contact
2. Profile summary
3. Role-fit skills
4. Practice projects / portfolio / cases
5. Internship, part-time, campus, or volunteer experience
6. Education/certifications
7. Learning path or tools, only if it supports the target role

Move practice projects above work experience when the user's portfolio is stronger than job history or the user is changing tracks.

## Bullet Transformation

Convert raw notes into focused bullets.

General pattern:

Raw: “做过一些运营内容。”

Better: “围绕目标用户整理 20+ 个内容选题方向，拆分标题、发布渠道和互动引导方式，形成可复用的内容排期表。”

Raw: “帮忙整理资料。”

Better: “负责会议资料、人员名单和物资台账整理，按时间节点完成核对、归档和异常标记，支持活动现场执行。”

Raw: “学过 Excel。”

Better: “使用 Excel 完成模拟费用台账和月度汇总表，包含分类统计、基础公式、数据筛选和异常金额标注。”

Raw: “做了后台页面和接口联调。”

Better: “基于 Vue3 + Element Plus 完成订单、商品与权限配置模块开发，对接后端接口并处理表单校验、状态流转和列表筛选等核心交互。”

## Artifact Flow

Prefer this sequence:

1. Produce a concise content plan or draft for quick review when the content is incomplete or the risk of misinterpretation is high.
2. Create the clean primary HTML resume artifact by default.
3. Tune HTML print pagination before exporting or finishing. For multi-page resumes, use the JavaScript-assisted pagination workflow in `html-pagination.md`: render content once, measure block heights, compare each block with the A4 content area height after page padding, then create separate `.resume-page` elements. Do not only calculate large modules. If a card or section does not fit but the current page still has useful space, split the next module by the current page's remaining height and move only the measured amount that fits upward. If the remaining height can only fit one line, split the first text item by measured height, move that line upward, and keep the remaining text plus the rest of the module as one continuation block. The moved fragment must keep the same card/bullet/accent formatting as the original module; do not render it as bare text. Avoid repeatedly splitting the same header or creating several continuation labels for one module. If the first fragment narrowly does not fit, try a compact page-fragment style before opening a new page. Avoid large blank areas caused by oversized unbreakable cards; allow long project/experience blocks to split naturally, adjust spacing, or refine layout density so page boundaries look continuous. For existing resumes, do not shorten bullets, remove sections, or compact content to fix pagination unless the user explicitly requests or approves that tradeoff. Add enough page-edge breathing room so headings, company names, project titles, and first bullets are not pressed against the top or bottom of a page.
4. Stop after the editable HTML resume is complete unless the user explicitly asks for another artifact.
5. Keep source files editable and avoid hiding private contact information in reusable public examples.
6. Summarize decisions and remaining risks.

## Final Review Checklist

- Target role is obvious in the first screen/page.
- Visible resume text has no typos, wrong characters, accidental encoding artifacts, inconsistent names, or incorrect role/project/company terms.
- Summary matches the strongest evidence in the experience section.
- Dates and organization/project names are consistent.
- Skills listed are supported by work, study, project, practice, or portfolio content.
- Featured items show real actions and deliverables, not only participation.
- Beginner practice items are labeled honestly.
- No invented metrics, fake employers, fake clients, fake seniority, or unverifiable claims.
- Contact info is present only in final private deliverables, not in reusable examples.
- HTML print layout uses an A4 page frame by default, with `@page size: A4` or an equivalent A4 print simulation, unless the user explicitly requested another paper size.
- Multi-page HTML uses separate `.resume-page` elements generated by measuring rendered content height against the available A4 content area, not a single long page with accidental browser slicing.
- HTML print layout has no text clipping, overlapping, or awkward orphan lines.
- HTML print preview has no obvious page-break gaps, oversized blank areas, uneven text/module spacing, cramped page-edge content, orphaned section headings, clipped content, inconsistent split-fragment formatting, repeated continuation headers, or cards pushed wholesale to the next page when they could be split or adjusted with layout changes.
