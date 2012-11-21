from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    "cms_lite.views",
    url(r"^(?P<name>)?$", "render_template", name="cms_lite_render_template"),
    url(r"^(?P<name>(\w[\w\/\-]*\w|\w))/$", "render_template", name="cms_lite_render_template"),
)
