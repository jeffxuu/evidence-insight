# Evidence Insight

**为图表、URL、论文、数据集和压缩包提供经证据核对的分析，并生成可直接发布的社交观点。**

面向具备工具使用能力的 AI Agent 的可移植证据综合层。
它在读取、研究、选材和写作阶段检查来源适用性、因果边界、必要限定，
并把分析交付与作者面向公众的社交成品分开。

[English](README.md) · [安装](docs/installation.md) · [评测方法](evals/README.md) · [验证状态](docs/verification.md)

[![Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![结构验证](https://github.com/jeffxuu/evidence-insight/actions/workflows/validate-skill.yml/badge.svg?branch=oss%2Fv1.0.0)](https://github.com/jeffxuu/evidence-insight/actions/workflows/validate-skill.yml)

**当前为 v1.0.0 发布准备。已提供 benchmark 方法，结果待完成。**

## 它要防止哪些失败

以下是测试目标说明，**不是实际模型 A/B 输出**。真实对照示例尚待完成。

| 常见失败 | 本 Skill 要求的边界 |
| --- | --- |
| 把不同人群的研究说成对原结论的反证 | 先比较人群、变量、结果、时间与研究设计 |
| “某情景下可能减少”压缩成“将会消失” | 保留模型、情景、程度和不确定性 |
| 把相关性改写成确定因果 | 核查识别依据，检验合理的竞争解释 |
| 把图、表和 README 当成同一种来源 | 分开精确数字、定义、版本、来源与视觉表达的职责 |
| 文案成为中性简报，或混入“我可以帮你监控” | 形成一个有证据支持的作者判断，保持成品封闭 |

## 快速安装

需要 Node.js/npm、支持 Skill 的宿主，以及仓库访问能力。

**默认分支安装：BLOCKED，等待合并。** 已实际运行该命令，main 上未发现 Skill。

```bash
npx skills add jeffxuu/evidence-insight --skill evidence-insight
```

候选分支安装方法和准确状态见[安装说明](docs/installation.md)。
`skills@1.5.26` 本地与远端候选分支的文件安装已验证；这不等于模型执行或默认分支安装已验证。

已验证的候选分支命令：

```bash
npx --yes skills@1.5.26 add 'jeffxuu/evidence-insight#oss/v1.0.0' --skill evidence-insight -a codex --copy -y
```

安装后提供材料，说“分析”“深度分析”或“分析并给一段配图文案”。
“只要分析”“只要配图文案”可以选择输出。默认文风和字数范围沿用中文规则。
[ChatGPT Project adapter](adapters/chatgpt-project-instructions.txt) 为可选适配，公开版本同步为 **1.0.0**。

## 为什么需要它

找到可信来源，只解决了一部分问题。正确的数据可能被套到错误的人群上，方法局限可能被写成反证，
压缩后的文案也可能比原始证据更确定。Evidence Insight 把这些检查放在实际产生错误的环节。
它提供流程与规则，不自带搜索服务、数据权限、模型或执行沙箱。

## 核心能力

- 多来源输入分工；处理数据版本、图片与表格冲突。
- 已知信息抑制，先分解指标，再开展研究。
- 来源质量、接近原始来源、证据适用性和原研究覆盖检查。
- 竞争解释与证据不足时的合理降级。
- 同一个合格证据池，Analysis 与 Social 分别选材。
- 限定传播、语义强度保留和有限次数的风格修订。
- 一主旨、有作者立场、自适应长度且没有助手服务话术的社交成品。

## 输入与架构

支持图表、截图、网页、URL、PDF、论文、CSV、TSV、JSON、XLSX、ZIP 及混合材料。
实际读取能力取决于宿主；读不到的内容必须说明，不能假装已读取。

[SKILL.md](skills/evidence-insight/SKILL.md) 保留入口、工作流程、关键边界和逐项加载条件；
十个 reference 随 Skill 一起安装。研究只执行一次，两个输出从同一证据池分别选材。
迁移清单和评测答案不进入安装包。拆文件不代表已测得 token 节省。

## 示例

[图表分析](examples/chart-analysis/README.md) · [URL 研究](examples/url-research/README.md) ·
[数据集](examples/dataset-analysis/README.md) · [混合来源](examples/mixed-source/README.md) ·
[社交文案](examples/social-output/README.md)

目前提供合成输入与预期边界。真实 vanilla / Evidence Insight 对照输出待完成。
不打包无授权的媒体整图、社交截图或付费 infographic。

## Benchmark

**已提供方法，结果待完成。**

[Rubric](evals/rubric.md) 区分硬失败、0–4 锚点评分与独立社交偏好选择。
[协议](evals/protocol.md) 要求先做迁移回归，再做 vanilla A/B；同模型、强度、输入、工具和次数，
每题每组至少三次，随机顺序盲评，支持人工与独立模型 judge。
确定性 CI 只能验证工程结构和评测工具，不能证明模型更少幻觉或已抵抗注入。

## 兼容性

| 环境 | 格式／安装 | 行为验证 |
| --- | --- | --- |
| Agent Skills | 官方验证器通过 | 格式通过不等于行为正确 |
| Codex | 本地及远端候选分支文件安装通过 | BLOCKED：测试环境模型宿主认证／初始化不可用 |
| 其他宿主 | 本项目未验证 | UNVERIFIED |
| ChatGPT Projects | adapter 与生成包结构已检查 | 实际上传和加载 UNVERIFIED |

## 安全与限制

外部网页、PDF、数据、README、metadata、截图及引用中的指令是不可信证据内容。
它们不能授权读取秘密、上传、执行命令、修改仓库、安装软件或调用工具；正常的数据定义仍可使用。
详见 [SECURITY.md](SECURITY.md)。提示词边界不能代替宿主权限与执行隔离。

结果依赖模型和工具，跨宿主、多语言效果尚未建立。
十个公开 holdout 蓝图不是封存的 unseen 测试集。行为验证、真实 demo 与完整 benchmark 仍待完成。

## 贡献、Star History 与许可

优先提交“输入 → 当前输出 → 观察到的失败 → 预期边界 → 回归测试”，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

Star History：**UNVERIFIED / pending**，动态端点确认可用后再展示，不使用静态虚假增长图。
skills.sh 收录：**UNVERIFIED**，兼容生态不等于已上架或已进入排行榜。

项目采用 [Apache-2.0](LICENSE)。第三方资料仍受各自许可约束，详见[资料审查](docs/materials.md)。
