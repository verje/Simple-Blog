from .models import Blog
from django.views import generic


class BlogsView(generic.ListView):
    # Python take default Django configuration and look for "templates" folder, then look for the path to_enter/index.html
    # render from de folder views, index.html to present content
    #template_name = 'to_enter/index.html'
    model = Blog
    template_name = "blogs.html"
    context_object_name = "Blog_Objects"


class IndexView(generic.TemplateView):
    template_name = "index.html"


class AboutView(generic.TemplateView):
    template_name = "about.html"