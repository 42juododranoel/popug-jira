from django.contrib import admin

from app.admin import ModelAdmin
from todos.models import Todo


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    fields = [
        'text',
        'image',
    ]
