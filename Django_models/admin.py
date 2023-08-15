from django.contrib import admin

from .models import Task,Comment,Project


admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)
