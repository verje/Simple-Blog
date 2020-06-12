from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Blog, ContactUs
# Creamos nuestra clase BlogForm que sera nuestro Formulario


class BlogForm(forms.ModelForm):
    # Declaramos una clase Meta donde indicamos el modelo que va a contener el formulario
    class Meta:
        model = Blog  # Usamos el modelo importado en la linea 4
        # indicamos que vamos a incluir todos los campos del modelo Blog (3 campos)
        fields = '__all__'


class ContactForm(forms.ModelForm):
    # Declaramos una clase Meta donde indicamos el modelo que va a contener el formulario
    class Meta:
        model = ContactUs  # Usamos el modelo importado
        # indicamos que vamos a incluir todos los campos del modelo Blog (3 campos)
        fields = ['name', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-group'})
        self.fields['email'].widget.attrs.update({'class': 'form-group'})
        self.fields['phone'].widget.attrs.update({'class': 'form-group'})


def ManageForm(request):  # Creamos un metodo para manejar el formulario una vez que se haga clic en el Boton Submit. Este metodo será llamdo desde el archivo app_urls.py
    # template_name = "forms/contact_form.html"
    template_name = "forms/blog_form.html"
    if request.method == 'POST':
        # Comenzamos a procesar el formulario a traves de la clase BlogForm, la cual a su vez esta conetada al modelo Blog
        # entonces tenemos relacionados todos lo elementos necesarios (Form, Modelo, Plantilla HTML)
        # Basicamente esta variable se usa como contenedor de los campos que mostrará el form
        # form es una variable Python(un objeto), obligatorio usarlo y sirve como contenedor de los campos de nuestro form
        form = BlogForm(request.POST or None)
        errors = None

        if form.is_valid():  # Se valida que todos los campos se hayan llenado
            form.save()  # Se guardan los datos a la base de datos
            # una vez procesado el Form y guardado los datos, redireccionamos al index
            return HttpResponseRedirect("/")

        if form.errors:  # Si hay errores en el form; es decir, no se llenan todos los campos
            errors = form.errors  # Guardamos en la variable errors, los errores encontrados

        context = {"form": form, "errors": errors}
        return render(request, template_name, context)
    else:
        form = BlogForm()
        return render(request, template_name, {'form': form})


def ManageFormContact(request):
    template_name = "forms/contact_form.html"
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        errors = None
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        if form.errors:
            errors = form.errors
        context = {"form": form, "errors": errors}
        return render(request, template_name, context)
    else:
        form = ContactForm
        return render(request, template_name, {'form': form})
