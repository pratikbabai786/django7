from django.contrib import admin
from pratikapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display=['taskname','deadline','completed']


admin.site.register(Task,TaskAdmin)
