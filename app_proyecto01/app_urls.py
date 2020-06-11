from django.urls import path
# from django.conf.urls import url
from . import views, forms

urlpatterns = [
    # desde views.py llamamos a la Clase IndexView y BlogsView
    path('', views.IndexView.as_view(), name="indexview"),
    path('blogs/', views.BlogsView.as_view(), name="blogsview"),
    path('new_blog/', forms.ManageForm),
    # cuando la ruta sea http://127.0.0.1:8000/contacto, Inicia la magia...llamaremos del archivo
    # form.py al Metodo ManageForm para que procese el formulario que se encuentra en el archivo BlogForm.html
    path('contact/', forms.ManageFormContact),
    # url(r'^contacts/$', views.contact, name='contact_form'),
    # path('about/', TemplateView.as_view(template_name="about.html"))
    # path('about/', views.AboutView.as_view()),
]
