<div align="center">

# Resume Builder Skill

**中文 | [English](README.en-US.md)**

一个面向 Codex 的简历生成与优化 Skill。默认生成一个可编辑、适合浏览器查看和 A4 打印的 HTML 简历文件。

</div>

## 简介

Resume Builder 用于创建、改写、排版和本地化简历。它可以根据已有简历、基础信息、面试记录、学习经历、工作经历或项目材料，整理出更清晰、更贴合目标岗位的简历。

默认情况下，简历内容使用中文，交付物为单个 HTML 文件；如果用户明确要求，也可以改成英文或其他语言。

## 能做什么

- 从零创建简历。
- 优化已有简历的结构、表达、关键词和项目呈现。
- 针对不同岗位、行业、地区和投递对象调整版本。
- 将零散经历整理成工作经历、项目经历、实践经历或作品集模块。
- 为应届生、转行者、实习求职者整理课程项目、练习项目、模拟业务项目等经历。
- 生成适合浏览器查看和 A4 打印的单文件 HTML 简历。

## 工作原则

- 基于用户提供的真实材料优化表达，不随意新增无法支撑的经历、数据或技能。
- 优化已有简历时，默认保留原有内容信息量；只有用户明确要求时才压缩篇幅或删减内容。
- 先梳理简历结构和岗位重点，再润色具体文案。
- 技能、工具和项目描述尽量能从经历、课程、作品或实际产出中找到依据。
- 优先保证清晰、可读、适合投递和打印，再考虑视觉风格。
- 联系方式和隐私信息只放在最终私有交付物中，不写入公开示例或可复用模板。

## 目录结构

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

## 文件说明

- `resume-builder/SKILL.md`：Skill 主入口，定义触发场景、工作流、写作规则、布局规则和验证要求。
- `resume-builder/references/resume-workflow.md`：完整的简历访谈、策略、内容改写和最终检查流程。
- `resume-builder/references/resume-template-catalog.md`：内置 HTML 简历模板说明与选择建议。
- `resume-builder/assets/builtin-template-styles.css`：内置 HTML 简历样式系统。
- `resume-builder/agents/openai.yaml`：Codex/OpenAI 环境中的展示信息。

## 安装方式

把 `resume-builder/` 整个目录放到 Codex 的 skills 目录中。常见位置是 `$CODEX_HOME/skills/resume-builder`。

也可以直接把本项目地址 [INIT1996/resume-builder](https://github.com/INIT1996/resume-builder) 发给 Codex 或其他 AI 助手，并说明：

```text
请帮我安装这个 resume-builder skill：https://github.com/INIT1996/resume-builder
```

如果 AI 可以访问本地文件或拉取项目，它会把 `resume-builder/` 目录复制到正确的 skills 目录中。

在 PowerShell 中可以这样安装：

```powershell
$skillsDir = Join-Path $env:CODEX_HOME "skills"
New-Item -ItemType Directory -Force $skillsDir
Copy-Item -Recurse -Force .\resume-builder $skillsDir
```

安装后重启 Codex，或刷新可用 Skills。确认可用后，就可以在对话里直接提到 `resume-builder` 或 `$resume-builder`。

## 使用方式

在 Codex 中可以这样触发：

```text
使用 resume-builder 帮我优化这份前端开发简历，突出项目经历，输出 HTML 版本。
```

Skill 会先确认你是否已有简历，然后默认输出一个 HTML 文件：

- 如果已有简历：提供文件或粘贴内容，再说明优化方向和模板偏好。
- 如果没有简历：先确认目标岗位和基础情况，再逐步补充联系方式、教育背景、工作、实习、课程项目、练习项目或校园经历等信息。

## 打印与导出 PDF

Skill 默认生成 HTML 简历。需要 PDF 时，直接用浏览器打开生成的 HTML 文件，按 `Ctrl+P`，选择“另存为 PDF”或“打印为 PDF”即可导出。

建议打印设置使用 A4 纸张；如果浏览器提供缩放选项，优先保持默认比例，确认预览中没有文字裁切或内容遮挡后再保存。

## 内置模板

HTML 简历可使用以下内置模板风格：

| ID | 适合场景 |
| --- | --- |
| `ats-clean` | 稳妥投递、HR 筛选、传统行业、需要高可读性的简历 |
| `project-focus` | 技术、产品、设计、工程等项目导向岗位 |
| `compact-sidebar` | 技能、证书、工具较多，但希望控制页数 |
| `visual-editorial` | 面试展示、内推、运营、设计、市场等更重表达的场景 |
| `ink-wash` | 教育、文化、公共服务或偏正式中文语境 |
| `neon-portfolio` | 视觉设计、新媒体、创意技术和作品集展示 |

如果用户没有偏好，默认选择最稳妥且符合目标岗位的模板。

## 本地检查

```powershell
Get-Content -Raw -Encoding UTF8 resume-builder\SKILL.md
Test-Path resume.html
```

这可以确认 Skill 说明可读，并且仓库中有一个可打开的 HTML 示例。

## 维护建议

- Skill 本体保持精简：关键流程放在 `SKILL.md`，详细流程和模板说明放在 `references/`。
- 不要在 `resume-builder/` 目录内新增 README、安装指南或过多辅助文档。
- 默认用户交付物只保留 HTML。
- 新增模板时要保证布局差异真实存在，不只是换色。
- 修改中文文档时使用 UTF-8 编码；在 PowerShell 中读取中文文件建议加 `-Encoding UTF8`。
