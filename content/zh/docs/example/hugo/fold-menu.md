---
date: 2025-05-07
linktitle: "折叠菜单"
title: "Hugo站点折叠菜单问题分析"
weight: 10
#bookCollapseSection: true
---

当设置文件创建日期大于当前实际日期时，折叠菜单无法显示。

例如：今天是 2025-05-07，若设置为2035-05-07，折叠菜单页面将无法显示。      

经过检查代码，我发现：

## 日期设置与折叠菜单的关系

在Hugo中使用Book主题，特别注意事项：

1. Hugo默认会根据日期来确定内容是否应该发布
2. 未来日期的内容被视为"草稿"或"未发布"状态
3. 在默认配置下，未发布的内容不会在生成的站点中显示

## 解决方案

两种解决方案：

### 方案1：修改日期
将日期设置为当前日期或过去的日期，例如：

```markdown:/Users/projects/hugo-book/content/zh/docs/example/collapsed/3rd-level/_index.md

---
date: 2023-05-07
linktitle: "第三级菜单"
title: "第三级菜单"
weight: 10
#bookCollapseSection: true
---

// ... existing code ...
```

### 方案2：在Hugo配置中启用未来内容

如果您希望保留未来日期，可以在Hugo配置文件中添加以下设置：

```yaml
# config.yaml 或 config.toml
buildFuture: true
```

这将告诉Hugo在构建站点时包含未来日期的内容。

## 关于 bookCollapseSection

在某些情况下，不设置 `bookCollapseSection: true` 也能正常显示折叠页面。这通常发生在以下情况：

1. 当目录结构本身已经表明该部分应该是可折叠的（例如，有子页面存在）
2. 当主题的默认行为是自动折叠具有子页面的部分

不过，为了确保一致的行为，建议在需要折叠的部分明确设置 `bookCollapseSection: true`，除非您确定主题的默认行为已经满足了需求。

## 总结

1. 将日期设置为当前或过去的日期，或在Hugo配置中启用 `buildFuture: true`
2. 根据需要决定是否使用 `bookCollapseSection: true`

这样应该可以解决折叠菜单显示问题。