from django.contrib import admin

# Register your models here.
from .models import Blogs
#indicates we want to see Project Class in admin page
admin.site.register(Blogs)