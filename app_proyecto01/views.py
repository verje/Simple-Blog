from django.views import generic
from .models import Blog


class BlogsView(generic.ListView):
    # Python take default Django configuration and look for "templates" folder, then look for the path to_enter/index.html
    # render from de folder views, index.html to present content
    # template_name = 'blogs.html'
    model = Blog
    template_name = "blogs.html"
    context_object_name = "Blog_Objects"

    def get_queryset(self):
        # return Blog.objects.exclude(Q(name__contains="Blog") & Q(topic='Politica')).order_by('name')
        return Blog.objects.exclude(name__contains="Blog", topic='Belleza').order_by('name')


class IndexView(generic.TemplateView):
    template_name = "index.html"
