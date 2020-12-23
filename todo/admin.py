# todo/admin.py

from django.contrib import admin
from .models import Todo  # add this


class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = (
        'id', 'title', 'description', 'category', 'completed', 'priority', 'created', 'modified')


# Register your models here.
admin.site.register(Todo, TodoAdmin)  # add this
