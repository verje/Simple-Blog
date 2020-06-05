from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    # from views.py take de class Index
    path('', views.IndexView.as_view(), name="indexview"),
    path('blogs/', views.BlogsView.as_view(), name="blogsview"),
    path('contacto/', views.contact, name='contact_form'),
    #url(r'^contacts/$', views.contact, name='contact_form'),
    #path('about/', TemplateView.as_view(template_name="about.html"))
    #path('about/', views.AboutView.as_view()),
]
