---
date: 2025-11-10
linktitle: "ImageMagick"
title: "批量处理- 图片裁切"
weight: 11
bookToc: true
type: "docs"
---

以团队简介页面的头像为例。


ImageMagick 是一款创建、编辑、合成，转换图像的命令行工具。支持格式超过 200 种，包括常见的 PNG, JPEG, GIF, HEIC, TIFF, DPX, EXR, WebP, Postscript, PDF, SVG 等。

功能包括调整，翻转，镜像(mirror)，旋转，扭曲，修剪和变换图像，调整图像颜色，应用各种特殊效果，或绘制文本，线条，多边形，椭圆和贝塞尔曲线等。

官网：https://www.imagemagick.org

批量处理命令（ImageMagick）在页面中使用的示例代码。

---


## HTML / 模板 示例
推荐使用 `srcset` 提供 1x/2x 图像：

```html
<img
  src="/images/avatars/jianghao-260.jpg"
  srcset="/images/avatars/jianghao-260.jpg 1x, /images/avatars/jianghao-520.jpg 2x"
  width="260"
  height="347"
  alt="Jianghao"
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

单张处理示例（以 `Atom.png` 为例）：

```bash
# 在仓库根目录运行
magick convert static/images/orig/Atom.png -resize '520x694^' -gravity center -extent 520x694 -strip -quality 82 static/images/avatars/Atom-520.jpg
magick convert static/images/orig/Atom.png -resize '260x347^' -gravity center -extent 260x347 -strip -quality 82 static/images/avatars/Atom-260.jpg
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

## 可选策略
1. 把仓库中原始头像集中到 `static/images/orig/`，运行批量脚本生成 260/520 图并提交到仓库（一次性做完）。
2. 写一个 Hugo shortocode（`layouts/shortcodes/avatar.html`），在内容里只写 `&#123;&#123;&lt; avatar "jianghao" &gt;&#125;&#125;`，shortcode 根据文件名自动选择合适的 srcset（需要修改模板，较为复杂）。
3. 只提供脚本和说明，在本地电脑上人工完成（不改仓库模板）。

---


