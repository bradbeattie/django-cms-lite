from django.contrib.sitemaps import Sitemap
from cms_lite.utils import get_cms_pages


class CMSLiteSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return get_cms_pages()

    def lastmod(self, obj):
        return None

    def location(self, obj):
        return obj

    def priority(self, obj):
        return (1.0 - obj.count("/") * 0.1)
