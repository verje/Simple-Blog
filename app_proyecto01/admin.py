from django.contrib import admin

# Register your models here.
from .models import Blog, ContactUs
admin.site.register(Blog)
admin.site.register(ContactUs)
