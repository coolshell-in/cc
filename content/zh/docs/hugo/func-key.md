---
date: 2025-08-10
linktitle: "参数列表"
title: "Hugo Book主题配置参数列表"
weight: 11
#bookCollapseSection: true
---


以下是Hugo Book主题中所有以`book`开头的配置参数及其功能说明，可以在`hugo.yaml`全局配置或在页面前置元数据(frontmatter)中使用：

## 全局配置参数（在hugo.yaml中使用）

| 参数名 | 默认值 | 功能说明 |
| --- | --- | --- |
| `BookTheme` | "light" | 设置颜色主题：light（亮色）、dark（暗色）或auto（自动根据浏览器/系统偏好切换） |
| `BookAuthor` | - | 设置站点作者信息 |
| `BookFlatSection` | false | 控制是否在页面底部显示子页面列表。设为false时禁用底部文章列表 |
| `BookToC` | true | 控制页面右侧目录的可见性。可以通过markup.tableOfContents设置控制起始和结束级别 |
| `BookFavicon` | "favicon.png" | 设置网站图标文件路径 |
| `BookLogo` | - | 设置书籍/网站的logo图片路径 |
| `BookSection` | "docs" | 指定要渲染为菜单的根页面。可以设置为'*'或'/'以渲染所有部分 |
| `BookRepo` | - | 设置源代码仓库位置，用于"最后修改"和"编辑此页面"链接 |
| `BookCommitPath` | "commit" | 指定链接到页面最后修改的提交哈希的链接部分 |
| `BookEditPath` | - | 启用"编辑此页面



## 全局配置参数

| 参数名 | 默认值 | 功能说明 |
| --- | --- | --- |
| `BookEditPath` | - | 启用"编辑此页面"链接。默认禁用，取消注释以启用。需要'BookRepo'参数 |
| `BookDateFormat` | "2006-01-02" | 配置页面上使用的日期格式（在git信息和博客文章中） |
| `BookSearch` | true | 启用flexsearch搜索功能。索引是即时构建的，因此可能会减慢网站速度 |
| `BookComments` | true | 在页面上启用评论模板。默认包含Disqus模板 |
| `BookPortableLinks` | false | 实验性功能，启用可移植链接和markdown页面中的链接检查 |
| `BookServiceWorker` | false | 实验性功能，启用缓存已访问页面和资源以供离线使用的服务工作程序 |
| `BookTranslatedOnly` | false | 实验性功能，仅在存在翻译时才为翻译启用下拉菜单 |
| `BookMenuBundle` | - | 可用于全局隐藏特定部分 |

## 页面级配置参数（在页面前置元数据中使用）

| 参数名 | 默认值 | 功能说明 |
| --- | --- | --- |
| `bookHidden` | false | 设置为true时，在左侧导航菜单中隐藏该页面及其所有子页面 |
| `bookCollapseSection` | false | 设置为true时，该部分在左侧菜单中默认折叠显示 |
| `bookFlatSection` | false | 控制是否在页面底部显示子页面列表。设为false时禁用底部文章列表 |
| `bookToC` | true | 控制页面右侧目录的可见性 |
| `bookComments` | true | 控制页面评论功能是否启用 |
| `bookSearchExclude` | false | 设置为true时，从搜索索引中排除该页面 |
| `bookHref` | - | 可以设置为外部URL，点击菜单项时将导航到该URL |
| `weight` | - | 控制页面在菜单中的排序位置（数字越小越靠前） |
| `no_list` | false | 设置为true时，禁止在父页面底部显示该页面 |
| `cascade` | - | 可以设置参数级联到所有子页面，例如`cascade: bookHidden: true` |

## 特殊用法

1. **隐藏整个部分**：
   ```yaml
   ---
   bookHidden: true
   ---
   ```

2. **默认折叠子菜单**：
   ```yaml
   ---
   bookCollapseSection: true
   ---
   ```

3. **禁用底部文章列表**：
   ```yaml
   ---
   bookFlatSection: false
   ---
   ```

4. **级联配置到所有子页面**：
   ```yaml
   ---
   cascade:
     type: docs
     bookHidden: false
     bookToC: true
   ---
   ```

5. **组合使用多个参数**：
   ```yaml
   ---
   title: "页面标题"
   weight: 10
   bookFlatSection: false
   bookCollapseSection: true
   bookHidden: false
   ---
   ```

这些参数可以根据您的需求灵活组合使用，以实现理想的网站结构和导航体验。
