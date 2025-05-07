---
author: "Michael Henderson"
date: 2014-09-28
linktitle: Mermaid 图表

title: Mermaid 图表
weight: 10
---

# Mermaid 图表

[MermaidJS](https://mermaid-js.github.io/) 是一个用于从文本生成 SVG 图表和示意图的库。

{{% hint info %}}
**覆盖 Mermaid 初始化配置**
要覆盖 Mermaid 的[初始化配置](https://mermaid-js.github.io/mermaid/#/Setup)，
请在 `assets` 文件夹中创建一个 `mermaid.json` 文件！
{{% /hint %}}

## 示例

{{% columns %}}

```tpl
{{</* mermaid [class="..."] >}}
stateDiagram-v2
State1：​​带有注释的状态

注释位于 State1 右侧
重要信息！您可以编写
注释。
结束注释
State1 --> State2
注释位于 State2 左侧：这是左侧的注释。
{{< /mermaid */>}}
```

<--->


{{<mermaid>}}
stateDiagram-v2
    State1: The state with a note
    note right of State1
        Important information! You can write
        notes.
    end note
    State1 --> State2
    note left of State2 : This is the note to the left.
{{</mermaid>}}

{{% /columns %}}