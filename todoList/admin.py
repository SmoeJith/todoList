from django.contrib import admin
from .models import Todo

# Models are registered for the admin panel below
admin.site.register(Todo)