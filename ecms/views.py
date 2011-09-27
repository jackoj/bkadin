from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext
from django.utils.http import urlquote

from mezzanine.conf import settings
from mezzanine.pages import page_processors
from mezzanine.pages.models import Page
from mezzanine.template.loader import select_template

# Create your views here.
def topic_page(request, slug, template="pages/page.html", extra_context=None):
    """
    Display content for a page. First check for any matching page processors
    and handle them. Secondly, build the list of template names to choose
    from given the slug and type of page being viewed.
    """
    print request.user
    page = get_object_or_404(Page.objects.published(request.user), slug=slug)
    if page.login_required and not request.user.is_authenticated():
        path = urlquote(request.get_full_path())
        url = "%s?%s=%s" % (settings.LOGIN_URL, REDIRECT_FIELD_NAME, path)
        return redirect(url)
    context = {"page": page}
    if extra_context is not None:
        context.update(extra_context)
    model_processors = page_processors.processors[page.content_model]
    slug_processors = page_processors.processors["slug:%s" % page.slug]
    for processor in model_processors + slug_processors:
        response = processor(request, page)
        if isinstance(response, HttpResponse):
            return response
        elif response:
            try:
                context.update(response)
            except (TypeError, ValueError):
                name = "%s.%s" % (processor.__module__, processor.__name__)
                error = ("The page processor %s returned %s but must return "
                         "HttpResponse or dict." % (name, type(response)))
                raise ValueError(error)
    templates = [u"pages/%s.html" % slug]
    if page.content_model is not None:
        templates.append(u"pages/%s.html" % page.content_model)
    templates.append(template)
    request_context = RequestContext(request, context)
    t = select_template(templates, request_context)
    return HttpResponse(t.render(request_context))

def logout_view(request):
    logout(request)
    return redirect('/')
