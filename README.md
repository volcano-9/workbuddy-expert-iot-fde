# WorkBuddy Expert · 前向部署工程师 FDE（iot-fde）

![avatar](avatars/expert.png)

> 借鉴 **Palantir 前向部署工程师（Forward Deployed Engineer）方法论**：真正的问题不在需求文档里，而在客户现场的数据、流程和人的日常操作中。

深入客户现场挖掘真实需求、建模数据、快速构建原型，专精**物联网设备接入**与**云平台项目交付落地**的实战型工程师专家。

## ✨ 核心能力

| 能力 | 说明 |
|------|------|
| **现场需求挖掘** | 调研计划、访谈提纲、数据采样清单，找到客户的"真实问题"而非表面需求 |
| **本体建模与数据集成** | 领域本体建模（对象—属性—关系—事件），MQTT / Modbus / OPC UA 等协议适配与数据管道设计 |
| **快速原型与交付落地** | 最小可行接入方案、端到端验证、分阶段上线计划（试点 → 扩量 → 并行 → 切换） |
| **交付风险管理与复盘** | 根因分析、推进策略、可复用交付资产沉淀 |

## 🔄 工作流（Palantir FDE 五阶段）

```
Discover（现场调研） → Model（建模摸底） → Prototype（原型验证）
→ Deploy（部署迭代） → Productize（沉淀复用）
```

## 📦 安装

将本仓库克隆到 WorkBuddy 专家目录：

```bash
git clone https://github.com/volcano-9/workbuddy-expert-iot-fde.git \
  ~/.workbuddy/plugins/marketplaces/my-experts/plugins/iot-fde
```

然后注册使其在专家中心可见（在 expert-manager skill 目录下执行）：

```bash
python scripts/register_expert.py \
  ~/.workbuddy/plugins/marketplaces/my-experts/plugins/iot-fde
```

> Windows 用户请将 `~/.workbuddy` 替换为 `C:\Users\<你>\.workbuddy`。

## 💬 试试这样问

- 「我们有一个新客户要接入物联网平台，帮我制定一份客户现场调研计划」
- 「客户现场设备数据格式混乱、协议不统一，帮我设计数据建模与清洗方案」
- 「项目交付进度卡住了，帮我分析根因并给出推进策略」

## 🗂 仓库结构

```
workbuddy-expert-iot-fde/
├── .codebuddy-plugin/
│   └── plugin.json        # 专家元数据（展示字段、分类、快捷提示词）
├── agents/
│   └── iot-fde.md         # Agent 人设定义（角色、能力、工作流、输出规范）
├── avatars/
│   └── expert.png         # 头像（512×512 PNG）
└── README.md
```

## 📄 许可

[MIT](LICENSE)
