from cms_lite import forms
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loaders.filesystem import Loader
from django.views.decorators.http import require_http_methods
import codecs
import os


@require_http_methods(["GET", "POST"])
def render_template(request, name="index"):
    if not name:
        name="index"
    if "_" in name:
        return redirect(
            reverse(
                "cms_lite_page",
                args=[name.replace("_", "-")],
            ),
            permanent=True,
        )
    try:
        if name.startswith("-"):
            raise TemplateDoesNotExist()
        filename = os.path.join("cms_lite", name.replace("-", "_") + ".html")
        cms_can_edit = request.user.is_superuser
        if "edit" in request.REQUEST and cms_can_edit:
            source, abspath = Loader().load_template_source(filename)
            form = forms.CmsPageForm(data=request.POST or None)
            if form.is_valid():
                with codecs.open(abspath, encoding="utf-8", mode="w") as f:
                    f.write(form.cleaned_data["source"])
                messages.success(request, "CMS page updated")
                return redirect(request.META.get("PATH_INFO"))
            else:
                form.initial["source"] = source
                return render_to_response(
                    "cms_lite/_edit.html",
                    context_instance=RequestContext(request, {
                        "cms_can_edit": cms_can_edit,
                        "form": form,
                    }),
                )
        else:
            return render_to_response(
                filename,
                context_instance=RequestContext(request, {
                    "cms_can_edit": cms_can_edit,
                }),
            )
    except TemplateDoesNotExist:
        if name.endswith("/index"):
            raise Http404()
        else:
            return render_template(request, name=name + "/index")
