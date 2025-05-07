---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
# 不设置 author，这样会使用全局设置
---