---
date: 2025-05-03
linktitle: "Content Directory"
title: "Modify the Content Directory of the Article on the Right Column"
weight: 10
bookToc: true
type: "docs"
layout: "single"
---

# Control the display of TOC

Modify the Content Directory of the Article on the Right Column TOC

The default homepage of the multi-level menu, file name _index.md, will not display the right TOC even if ``bookToc: true`` is added to the front matter. The default right column displays a list of tags and categories.

The TOC can be automatically displayed for non-homepages.

If the content on the homepage also has multi-level titles, how to add a right column TOC to it?

## Solution: Use content parameters to force the display of TOC

Add special parameters in the _index.md file:

```md
---
date: 2025-05-03
linktitle: "Content Directory"
title: "Modify the content directory of the article in the right column"
weight: 10
bookToc: true
type: "docs"
layout: "single"
---

```

Added type: "docs" and layout: "single" parameters, which will force Hugo to use a single page layout instead of the homepage layout.

## Solution: Create a custom layout file
If you don't want to modify the theme file directly, you can create a custom layout:

1. Create in the project root directory: /Users/projects/hugo-book/layouts/_default/section.html
2. Copy the content of single.html in the theme to this file
3. Make sure the TOC section is not restricted by the homepage

Of course, you can also use shortcode to insert TOC and other methods. Here we recommend that you give priority to solutions that do not require code changes.

## Cancel the sub-page list at the bottom of the default homepage

In the hugo-book theme, the article list of all pages and sub-pages is displayed in the left menu by default.

In the case of a defective theme, if a page has sub-pages, there may be a sub-page list below the body of the page that is the same as the left column.

So the two are repeated, and we only keep a list of articles in the left column.

How to cancel the sub-menu (article list) at the bottom of the default homepage?

The simplest way is to add the following code to `_custom.scss`:

```scss
.book-page .markdown > ul:last-child,
.book-page .markdown > ol:last-child {
display: none;
}
```

Then, by configuring the default homepage to control whether to display all pages in the left column, add the configuration in the front matter:
```md
---
cascade:
type: docs
no_list: true
---
```

Under normal circumstances, the configuration is very simple. You only need to make the above configuration on the parent page of a column, and its child pages will also inherit the configuration of the parent page.

However, due to defects in the theme, it may not support simple configuration, and it is required to add the configuration `no_list: true` to all parent and child pages, which complicates things.

Therefore, the combined use of the above two codes will effectively solve the problem.

# Length control of article summaries in the default homepage subpage list

/posts/ The article summaries in the default homepage article list are very long. How can I control the length? For example, limit it to 200 words?