---
date: 2025-05-07
linktitle: "Folding Menu"
title: "Hugo Site Folding Menu Problem Analysis"
weight: 10
#bookCollapseSection: true
---

When the setting file creation date is greater than the current actual date, the folding menu cannot be displayed.

For example: today is 2025-05-07, if it is set to 2035-05-07, the folding menu page will not be displayed.

After checking the code, I found:

## The relationship between date setting and collapse menu

Using Book theme in Hugo, special attention:

1. Hugo will determine whether the content should be published based on the date by default

2. Content with future dates is considered "draft" or "unpublished"

3. Under the default configuration, unpublished content will not be displayed in the generated site

## Solution

Two solutions:

### Solution 1: Modify date
Set the date to the current date or a past date, for example:

```markdown:/Users/projects/hugo-book/content/zh/docs/example/collapsed/3rd-level/_index.md

---
date: 2023-05-07
linktitle: "Third-level menu"
title: "Third-level menu"
weight: 10
#bookCollapseSection: true
---

// ... existing code ...
```

### Solution 2: Enable future content in Hugo configuration

If you want to preserve future dates, you can add the following setting to your Hugo configuration file:

```yaml
# config.yaml or config.toml
buildFuture: true
```

This will tell Hugo to include future dated content when building the site.

## About bookCollapseSection

In some cases, it is possible to display collapsed pages without setting `bookCollapseSection: true`. This usually happens in the following cases:

1. When the directory structure itself indicates that the section should be collapsible (for example, there are subpages)

2. When the default behavior of the theme is to automatically collapse sections with subpages

However, to ensure consistent behavior, it is recommended to explicitly set `bookCollapseSection: true` in the sections that need to be collapsed, unless you are sure that the default behavior of the theme already meets your needs.

## Summary

1. Set the date to the current or past date, or enable `buildFuture: true` in Hugo configuration

2. Use `bookCollapseSection: true` as needed

This should solve the collapse menu display problem.