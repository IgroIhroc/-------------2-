import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Student Documentation'
author = 'Ilya Holovatyi'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
}