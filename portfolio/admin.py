from django.contrib import admin
#first have to import models from models.py

from .models import Project
#indicates we want to see Project Class in admin page
admin.site.register(Project)
