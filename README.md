<div align="center">

# Resume Builder Skill

**中文 | [English](README.en-US.md)**

面向 Codex 的简历生成与优化 Skill。它帮助用户从已有简历、基础资料、面试记录、学习经历、工作经历或项目材料中，整理出更清晰、更贴合目标岗位的 HTML 简历。

</div>

## 项目简介

Resume Builder 是一个用于生成和优化简历的 Codex Skill。它会围绕目标岗位梳理信息结构、调整表达重点，并生成可编辑、可在浏览器查看、适合 A4 打印的 HTML 简历。

`resume-builder/` 目录包含：

- `SKILL.md`：Skill 主入口，定义触发场景、工作流、写作规则、布局规则和验证要求。
- `agents/`：Codex/OpenAI 环境中的展示配置。
- `assets/`：Skill 使用的内置样式资源。
- `examples/`：分页与 HTML 简历示例。
- `references/`：工作流、模板目录、分页规则和资料结构参考。
- `scripts/`：辅助脚本。

## 能做什么

- 从零创建简历。
- 优化已有简历的结构、表达、关键词和项目呈现。
- 针对不同岗位、行业、地区和投递对象调整内容重点。
- 将零散经历整理成工作经历、项目经历、实践经历、课程项目或作品集模块。
- 为应届生、实习求职者、转行者补齐真实、可解释的经历表达。
- 输出适合浏览器阅读和 A4 打印的分页 HTML 简历。

## 工作原则

- 优化已有简历时，默认保留原有信息量；只有用户明确要求时才压缩篇幅或删减内容。
- 先梳理简历结构、岗位重点和证据链，再润色具体文案。
- 技能、工具和项目描述尽量能从经历、课程、作品或实际产出中找到依据。
- 优先保证清晰、可读、适合投递和打印，再考虑视觉风格。
- 联系方式和隐私信息只放在最终私有交付物中，不写入公开示例或可复用模板。

## 目录结构

```text
.
└── resume-builder/
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

## 安装方式

把 `resume-builder/` 整个目录放到 Codex 的 skills 目录中。常见位置是：

```text
$CODEX_HOME/skills/resume-builder
```

在 PowerShell 中可以这样安装：

```powershell
$skillsDir = Join-Path $env:CODEX_HOME "skills"
New-Item -ItemType Directory -Force $skillsDir
Copy-Item -Recurse -Force .\resume-builder $skillsDir
```

安装后重启 Codex，或刷新可用 Skills。确认可用后，在对话中直接提到 `resume-builder` 或 `$resume-builder` 即可触发。

也可以把项目地址发给 Codex 或其他 AI 助手，并说明：

```text
请帮我安装这个 resume-builder skill：https://github.com/INIT1996/resume-builder
```

## 使用方式

在 Codex 中可以这样开始：

```text
使用 resume-builder 帮我优化这份前端开发简历，突出项目经历，输出 HTML 版本。
```

Skill 会先确认用户是否已有简历：

- 如果已有简历：提供文件或粘贴内容，再说明优化方向、目标岗位和模板偏好。
- 如果没有简历：先确认目标岗位和基础情况，再逐步补充联系方式、教育背景、工作经历、实习经历、课程项目、练习项目或校园经历等信息。

默认流程会在最终生成 HTML 前，让用户选择内置模板风格；如果没有偏好，会请求确认默认的 `ats-clean` 风格。

## 内置模板

HTML 简历可使用以下内置模板风格：

| ID | 名称 | 适合场景 |
| --- | --- | --- |
| `ats-clean` | 简洁 ATS | 稳妥投递、HR 筛选、传统行业、需要高可读性的简历 |
| `project-focus` | 项目突出 | 技术、产品、设计、工程等项目导向岗位 |
| `compact-sidebar` | 侧栏紧凑 | 技能、证书、工具较多，但希望控制页数 |
| `visual-editorial` | 视觉编辑 | 面试展示、内推、运营、设计、市场等更重表达的场景 |
| `ink-wash` | 山水纸感 | 教育、文化、公共服务或偏正式中文语境 |
| `neon-portfolio` | 霓虹作品集 | 视觉设计、新媒体、创意技术和作品集展示 |

模板选择和 CSS 使用规则见 `resume-builder/references/resume-template-catalog.md`。

## 打印与导出 PDF

Skill 默认生成 HTML 简历。需要 PDF 时，用浏览器打开生成的 HTML 文件，按 `Ctrl+P`，选择“另存为 PDF”或“打印为 PDF”即可导出。

建议使用 A4 纸张设置，并在保存前检查：

- 页面边距是否正常。
- 文字是否被裁切。
- 模块是否互相遮挡。
- 分页处是否有明显的大空白或孤立标题。

## 本地预览

可以打开 `resume-builder/examples/` 下的示例，用来检查 A4 分页结构和打印行为。

## 维护建议

- Skill 本体保持精简：关键流程放在 `resume-builder/SKILL.md`，详细流程和模板说明放在 `resume-builder/references/`。
- 默认用户交付物只保留 HTML，除非用户明确要求 DOCX、PDF、Markdown 或其他格式。
- 新增模板时要保证布局差异真实存在，不只是换色。
- 修改分页逻辑时，优先参考 `resume-builder/references/html-pagination.md`，并用 `resume-builder/examples/pagination-stress-test.html` 做回归检查。
- 修改中文文档时使用 UTF-8 编码；在 PowerShell 中读取中文文件建议加 `-Encoding UTF8`。

## 本地检查

```powershell
Get-Content -Raw -Encoding UTF8 resume-builder\SKILL.md
Get-Content -Raw -Encoding UTF8 README.md
Test-Path resume-builder\examples\pagination-stress-test.html
```

这些检查可以确认 Skill 说明、中文 README 和分页示例都存在且可读取。
