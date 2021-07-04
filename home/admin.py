from django.contrib import admin
from .models import Todo

class AdminTodo(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'date_created']

admin.site.register(Todo, AdminTodo)