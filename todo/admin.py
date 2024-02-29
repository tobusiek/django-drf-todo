from django.contrib import admin

from todo import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class PriorityAdmin(admin.ModelAdmin):
    pass


class ProgressAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "progress", "due_to")
    readonly_fields = ("slug",)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Priority, PriorityAdmin)
admin.site.register(models.Progress, ProgressAdmin)
admin.site.register(models.Task, TaskAdmin)
