# Changelog

All notable changes to this expert package will be documented in this file.

## [1.2.0] - 2026-11-12

### Added
- **Skill 交付模板包** `skills/iot-fde-delivery/`：5 份结构化交付文档模板（现场调研计划、领域本体与设备盘点、MVP 接入方案、上线计划与验收清单、项目复盘报告），专家可按阶段调用并填充现场真实信息
- **问法路由表**：单轮提问按问法类型直接切入对应工作流阶段，不再每次从 Phase 1 讲起
- **Few-shot 示例对话**：明确"模糊提问 → 定向追问 3 个关键问题 → 按模板产出"的标准行为模式
- **边界声明**：明确不做什么（纯理论空谈、商务决策、敏感数据样例）及何时移交人工

### Changed
- quickPrompts 第 3 条调整为产出型问法（协议选型对比表）
- plugin.json 补全 author / keywords 字段

## [1.1.0] - 2026-11-12

### Changed
- 针对首轮审核反馈重写 Agent 人设：
  - 五阶段工作流全部配备内嵌产出模板
  - 新增物联网协议选型速查表与典型交付陷阱
  - 新增交互规则（最多追问 3 个问题、先诊断后开方、结论先行）

## [1.0.0] - 2026-11-12

### Added
- 初始版本：Palantir FDE 方法论专家，物联网与云平台交付方向
