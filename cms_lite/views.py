from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.views.decorators.http import require_http_methods
import os


@require_http_methods(["GET"])
def render_template(request, name="index"):
    if "_" in name:
        return redirect(
            reverse(
                "cms_lite_render_template",
                args=[name.replace("_", "-")],
            ),
            permanent=True,
        )
    try:
        if name.startswith("-"):
            raise TemplateDoesNotExist()
        return render_to_response(
            os.path.join("cms_lite", name.replace("-", "_") + ".html"),
            context_instance=RequestContext(request, {}),
        )
    except TemplateDoesNotExist:
        if name.endswith("/index"):
            raise Http404()
        else:
            return render_template(request, name=name + "/index")
