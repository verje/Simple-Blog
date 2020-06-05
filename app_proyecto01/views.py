from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Blog
from .form_contacto import ContactForm


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


class AboutView(generic.TemplateView):
    template_name = "about.html"


def contact(request):
    template_name = "contact.html"
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        errors = None
        if form.is_valid():
            return HttpResponseRedirect("/s/")
        if form.errors:
            errors = form.errors
        context = {"form": form, "errors": errors}
        return render(request, template_name, context)
    else:
        form = ContactForm()
        return render(request, template_name, {'form': form})
