# -*- coding: utf-8 -*-
import os

# 中文配置
language = 'zh_CN'
master_doc = 'index'

project = '明远智睿文档'
copyright = '2026'
author = 'myZR'

extensions = ['sphinx_rtd_theme']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['../_templates']
html_static_path = ['../_static']
html_theme = 'sphinx_rtd_theme'

# 关闭重复标签警告（解决你的 download 重复警告）
suppress_warnings = ["ref.duplicate"]