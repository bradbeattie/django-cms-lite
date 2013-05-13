from django.conf.urls import patterns, url

urlpatterns = patterns(
    "cms_lite.views",
    url(r"^(?P<name>)?$", "render_template", name="cms_lite_page"),
    url(r"^(?P<name>(\w[\w\/\-]*\w|\w))/$", "render_template", name="cms_lite_page"),
)
