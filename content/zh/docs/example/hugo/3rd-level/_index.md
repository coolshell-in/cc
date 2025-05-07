---
date: 2025-05-03
linktitle: "内容目录"
title: "右侧栏的文章内容目录修改"
weight: 10
bookToc: true
type: "docs"
layout: "single"
---

# 控制显示TOC

右侧栏的文章内容目录TOC修改

多级菜单的默认首页 文件名 _index.md， 即使在front matter中添加了 ``bookToc: true``，也不会显示右侧TOC，默认右侧栏显示的是tag，categories的列表。

非首页则可以自动显示TOC。

若首页中的内容也有多级标题，如何给其增加右侧栏TOC？

## 方案：使用内容参数强制显示TOC

在 _index.md 文件中添加特殊参数：

```md
---
date: 2025-05-03
linktitle: "内容目录"
title: "右侧栏的文章内容目录修改"
weight: 10
bookToc: true
type: "docs"
layout: "single"
---

```

添加了 type: "docs" 和 layout: "single" 参数，这会强制Hugo使用单页面布局，而非首页布局。


## 方案：创建自定义布局文件
如果不想直接修改主题文件，可以创建自定义布局：

1. 在项目根目录创建： /Users/projects/hugo-book/layouts/_default/section.html
2. 复制主题中的 single.html 内容到这个文件
3. 确保TOC部分不受首页限制

当然，还可以使用shortcode插入TOC等方法，这里我们推荐优先采纳不用改代码的方案。




## 撤销默认首页底部的文章列表

左侧菜单中已经有文章列表，不要重复了。


    页面👌
    hugo FAQ
    Hidden


# 文章列表摘要的长度控制

/posts/ 默认首页的文章列表，其文章摘要都很长，如何做长度控制？例如限定为200字？


