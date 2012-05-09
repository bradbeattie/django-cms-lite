from django.contrib.sitemaps import Sitemap
from django.template.loaders.app_directories import app_template_dirs
import os
import re


class CMSLiteSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        templates = []
        for app_template_dir in app_template_dirs:
            cms_lite_dir = os.path.join(app_template_dir, "cms_lite")
            for root, subFolders, files in os.walk(cms_lite_dir):
                templates.extend([
                    re.sub(r"_", "-", re.sub(r"\/?index", "", re.sub(r"\.html$", "", os.path.relpath(os.path.join(root, f), cms_lite_dir))))
                    for f in files
                    if not f.startswith("_") and f.endswith(".html")
                ])
        return sorted(set(templates))

    def lastmod(self, obj):
        return None

    def location(self, obj):
        if not obj:
            return "/"
        else:
            return "/" + obj + "/"

    def priority(self, obj):
        return (0.9 - obj.count("/") * 0.1) if obj else 1.0
