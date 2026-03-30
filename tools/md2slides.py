#!/usr/bin/env python3
import sys
import pathlib
import html
import re
import webbrowser

def markdown_to_html(md: str) -> str:
    # 保留简单换行
    lines = md.strip().split('\n')
    out = []
    for line in lines:
        if line.startswith('### '):
            out.append('<h3>%s</h3>' % html.escape(line[4:].strip()))
        elif line.startswith('## '):
            out.append('<h2>%s</h2>' % html.escape(line[3:].strip()))
        elif line.startswith('# '):
            out.append('<h1>%s</h1>' % html.escape(line[2:].strip()))
        elif line.strip() == '':
            out.append('<p></p>')
        else:
            # 先处理链接，再转义 HTML，保证安全简单
            text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', line)
            text = html.escape(text)
            # 已经有链接元素的部分会被转义成实体，需要恢复一起处理（只做最简单的演示）
            text = text.replace('&lt;a ', '<a ').replace('&lt;/a&gt;', '</a>').replace('&gt;', '>').replace('&quot;', '"')
            out.append('<p>%s</p>' % text)
    return '\n'.join(out)


def parse_slides(markdown_text: str):
    slides = []
    current_title = '封面'
    current_body = []

    for line in markdown_text.splitlines():
        if line.startswith('## '):
            if current_body or slides:
                slides.append((current_title, '\n'.join(current_body).strip()))
            current_title = line[3:].strip() or '无标题'
            current_body = []
        else:
            current_body.append(line)

    if current_body or not slides:
        slides.append((current_title, '\n'.join(current_body).strip()))

    return slides


def build_html(slides):
    slide_divs = []
    for i, (title, body) in enumerate(slides):
        html_body = markdown_to_html(body or '')
        slide_divs.append('<section class="slide" data-index="%d">\n  <h1>%s</h1>\n  <div class="content">%s</div>\n</section>' % (i, html.escape(title), html_body))

    slides_html = '\n'.join(slide_divs)

    return '''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>Markdown PPT 演示</title>
  <style>
    body {{margin:0;background:#111;color:#eee;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}}
    .ppt {{width:100vw;height:100vh;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;}}
    .slide {{position:absolute;top:0;left:0;right:0;bottom:0;opacity:0;transform:scale(0.96);transition:opacity .25s ease, transform .25s ease;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px;box-sizing:border-box;}}
    .slide.active {{opacity:1;transform:scale(1);}}
    .slide h1 {{font-size:3rem;margin:0 0 1rem;color:#8ef;}}
    .slide .content {{max-width:1000px;text-align:left;line-height:1.6;font-size:1.525rem;}}
    .slide .content p{{margin:0.8rem 0;}}
    a {{color:#8ef;text-decoration:none;}}
    a:hover {{text-decoration:underline;}}
    .control-bar {{position:absolute;bottom:12px;left:50%;transform:translateX(-50%);font-size:1rem;color:#bbb;}}
    button {{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);color:#fff;padding:.5rem .8rem;margin:0 .2rem;border-radius:.25rem;cursor:pointer;}}
    button:hover {{background:rgba(255,255,255,.25);}}
  </style>
</head>
<body>
  <div class="ppt">
    {slides_html}
    <div class="control-bar">
      <button id="prev">◀ </button>
      <span id="counter">0 / {total}</span>
      <button id="next"> ▶</button>
      &nbsp;
    </div>
  </div>

  <script>
    const slides = document.querySelectorAll('.slide');
    let idx = 0;
    function update() {{
      slides.forEach((s, i) => s.classList.toggle('active', i === idx));
      document.getElementById('counter').textContent = (idx+1) + ' / ' + slides.length;
    }}
    document.getElementById('prev').addEventListener('click', () => {{ idx = (idx - 1 + slides.length) % slides.length; update(); }});
    document.getElementById('next').addEventListener('click', () => {{ idx = (idx + 1) % slides.length; update(); }});
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' ) {{ idx = (idx + 1) % slides.length; update(); e.preventDefault(); }}
      if (e.key === 'ArrowLeft') {{ idx = (idx - 1 + slides.length) % slides.length; update(); e.preventDefault(); }}
    }});
    update();
  </script>
</body>
</html>
'''.format(slides_html=slides_html, total=len(slides))


def main():
    if len(sys.argv) < 2:
        print('用法: python md2slides.py path/to/file.md')
        sys.exit(1)

    src = pathlib.Path(sys.argv[1])
    if not src.exists():
        print('文件不存在：', src)
        sys.exit(1)

    text = src.read_text(encoding='utf-8')
    slides = parse_slides(text)
    out_html = build_html(slides)

    out_file = src.with_suffix('.slides.html')
    out_file.write_text(out_html, encoding='utf-8')
    print('已生成', out_file)
    print('正在用默认浏览器打开...')
    webbrowser.open(out_file.resolve().as_uri())

if __name__ == '__main__':
    main()
