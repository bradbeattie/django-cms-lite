from django.contrib.sitemaps import Sitemap
from cms_lite.utils import get_cms_pages


class CMSLiteSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return get_cms_pages()

    def lastmod(self, obj):
        return None

    def location(self, obj):
        if not obj:
            return "/"
        else:
            return "/" + obj + "/"

    def priority(self, obj):
        return (0.9 - obj.count("/") * 0.1) if obj else 1.0
