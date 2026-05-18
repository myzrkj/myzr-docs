# -*- coding: utf-8 -*-
import os

# 英文配置
language = 'en'
master_doc = 'index'

project = 'MYZR Documentation'
copyright = '2026'
author = 'myZR'

extensions = ['sphinx_rtd_theme']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['../_templates']
html_static_path = ['../_static']
html_theme = 'sphinx_rtd_theme'

# 关闭重复标签警告
suppress_warnings = ["ref.duplicate"]