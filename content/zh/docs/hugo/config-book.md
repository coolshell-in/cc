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




## 撤销默认首页底部的子页面列表

hugo-book主题中，默认在左侧菜单中显示所有页面和子页面的文章列表。

在主题有缺陷的情况下，若一个页面有子页面，可能页面正文下方，还有一个与左侧栏相同的子页面列表。

所以两者重复了，我们仅仅保留一个左侧栏的文章列表即可。

如何撤销默认首页底部的子菜单（文章列表）？


最简单的方法是在`_custom.scss` 增加以下代码：

```scss
.book-page .markdown > ul:last-child,
.book-page .markdown > ol:last-child {
  display: none;
}
```

然后，通过配置默认首页来控制是否在左侧栏显示全部页面，在front matter中增加配置：
```md
---
cascade:
    type: docs
    no_list: true
---
```

正常情况下，配置很简单，只需要在某一个专栏的父页面做以上配置，其子页面也都将继承父页面的配置。

但是可能由于主题缺陷，不支持简单配置，要求在全部的父页面和子页面中都要增加配置 `no_list: true`，这样就把事情复杂化了。

因此以上两处代码的配合使用，将有效解决问题。


# 默认首页的子页面列表的文章摘要的长度控制

/posts/ 默认首页的文章列表，其文章摘要都很长，如何做长度控制？例如限定为200字？


