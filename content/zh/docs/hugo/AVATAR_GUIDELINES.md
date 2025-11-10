---
date: 2025-11-10
linktitle: "头像规范"
title: "头像规范与批量处理指南"
weight: 11
bookToc: true
type: "docs"
---

本文档总结了为保证页面整洁、个人简介的头像显示一致而推荐的尺寸规范、响应策略、批量处理命令（ImageMagick）和在页面中使用的示例代码。把此文件保存到仓库后，团队成员可以统一按照规范准备或生成头像图。

---

## 结论（要点）
- 建议纵横比：3:4（宽:高 = 3:4），与当前 170×227 接近。
- 页面显示（CSS 控制）推荐：桌面最多显示宽度 260px（已在样式中设置为 `max-width: 260px`）；窄屏（<=640px）显示约 160–220px（目前 media query 为 45%/max 220px）。
- 源图像建议：为了在 Retina / 高分屏也清晰，源图至少为显示尺寸的 2×。例如桌面最大显示 260px → 源宽至少 520px；按 3:4，高应为 520 × 4/3 ≈ 694px。
- 推荐的源尺寸（3:4）：
  - 2x (retina): 520 × 694 px
  - 1x: 260 × 347 px
  - 可选小图: 130 × 174 px
- 格式：优先 WebP（更节省带宽），保留 JPEG 作为回退；压缩质量建议 70–85%。

---

## 为什么采用以上规格
- 统一的宽高比能保证在页面上排列整齐，避免某些纵向或横向拉长图片破坏布局。
- 提供 1x/2x 两套资源能兼顾常规屏与 Retina 屏幕的显示质量。
- 限制 `max-width`（260px）能防止在超宽屏上头像过大，影响文本阅读。

---

## HTML / 模板 示例
推荐使用 `srcset` 提供 1x/2x 图像：

```html
<img
  src="/images/avatars/jianghao-260.jpg"
  srcset="/images/avatars/jianghao-260.jpg 1x, /images/avatars/jianghao-520.jpg 2x"
  width="260"
  height="347"
  alt="江浩"
  class="avatar" />
```

如果想使用 WebP 并提供回退：

```html
<picture>
  <source type="image/webp" srcset="/images/avatars/jianghao-260.webp 1x, /images/avatars/jianghao-520.webp 2x">
  <img src="/images/avatars/jianghao-260.jpg" srcset="/images/avatars/jianghao-260.jpg 1x, /images/avatars/jianghao-520.jpg 2x" width="260" height="347" alt="江浩" class="avatar">
</picture>
```

在 Hugo 中你也可以用 shortcode 或模板内的 image processing 自动生成不同尺寸，但那会增加构建开销。

---

## 批量处理命令（ImageMagick）
下面的命令假设你把原始图片放到 `static/images/orig/`，脚本会生成 `static/images/avatars/` 下的 `*-260.jpg` 和 `*-520.jpg`。

先安装工具（macOS）：

```bash
brew install imagemagick webp
```

单张处理示例（以 `xuwenwen.png` 为例）：

```bash
# 在仓库根目录运行
magick convert static/images/orig/xuwenwen.png -resize '520x694^' -gravity center -extent 520x694 -strip -quality 82 static/images/avatars/xuwenwen-520.jpg
magick convert static/images/orig/xuwenwen.png -resize '260x347^' -gravity center -extent 260x347 -strip -quality 82 static/images/avatars/xuwenwen-260.jpg
```

批量处理（适用于 `orig` 目录下所有图片）：

```bash
for f in static/images/orig/*.{png,jpg,jpeg}; do
  [ -f "$f" ] || continue
  name=$(basename "$f")
  base=${name%.*}
  magick convert "$f" -resize '520x694^' -gravity center -extent 520x694 -strip -quality 82 "static/images/avatars/${base}-520.jpg"
  magick convert "$f" -resize '260x347^' -gravity center -extent 260x347 -strip -quality 82 "static/images/avatars/${base}-260.jpg"
done
```

生成 WebP（可选）：

```bash
for img in static/images/avatars/*-520.jpg; do
  cwebp -q 80 "$img" -o "${img%.jpg}.webp"
done
for img in static/images/avatars/*-260.jpg; do
  cwebp -q 80 "$img" -o "${img%.jpg}.webp"
done
```

（需要 `cwebp`：`brew install webp`）

---

## 命名与管理建议
- 目录：`static/images/avatars/`。
- 命名规则：`小写-连字符`，无空格，例如：`jianghao-260.jpg`、`jianghao-520.jpg`。
- 若图片需要人工裁切（例如人脸不居中），请单独处理并替换对应 `orig` 文件后再运行批量脚本。

---

## 可选策略（由我代劳）
1. 我帮你把仓库中原始头像集中到 `static/images/orig/`，运行批量脚本生成 260/520 图并提交到仓库（适合你希望我一次性做完）。
2. 我写一个 Hugo shortocode（`layouts/shortcodes/avatar.html`），在内容里只写 `&#123;&#123;&lt; avatar "jianghao" &gt;&#125;&#125;`，shortcode 根据文件名自动选择合适的 srcset（需要你同意我修改模板）。
3. 只提供脚本和说明由你/团队运行（不改仓库模板）。

---

如果你确认让我代劳（选 1 或 2），请回复你偏好的选项，并把原始头像放到 `static/images/orig/`（或允许我把当前 `static/images/` 下的头像作为原始图来处理）。如果你需要我先做 1 个示例（例如处理 `xuwenwen.png`），我也可以先运行并提交示例文件供你审核。

---

