from django.template.loaders.app_directories import app_template_dirs
import os
import re


def get_cms_pages(base_dir="cms_lite", sub_dirs=[]):
    templates = []
    for app_template_dir in app_template_dirs:
        cms_lite_dir = os.path.join(app_template_dir, "cms_lite", *sub_dirs)
        for root, subFolders, files in os.walk(cms_lite_dir):
            templates.extend([
                re.sub(r"_", "-", re.sub(r"\/?index", "", re.sub(r"\.html$", "", os.path.relpath(os.path.join(root, f), cms_lite_dir))))
                for f in files
                if not f.startswith("_") and f.endswith(".html")
            ])
    return sorted(set(templates))