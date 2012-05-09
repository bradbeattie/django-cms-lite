from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("cms_lite.views",
    url(r"^$", "render_template"),
    url(r"^(?P<name>[\w\/\-]+)/$", "render_template", name="cms_lite_render_template"),
)
