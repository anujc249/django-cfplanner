from django.contrib import admin

from .models import *


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class TaskInline(admin.StackedInline):
    model = Task
    fields = ['status']
    fk_name = 'assignee'
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Task', {'fields': ('component', 'priority', 'status', 'title', 'description')}),
        ('Testing Information', {'fields': ('asana_task', 'pull_request', 'test_link')}),
        ('Resources', {'fields': ('assignee', 'developer', 'project_manager', 'business_manager')}),
        ('Timeline', {'fields': ('create_date', 'due_date', 'completed_date')}),
    ]
    inlines = [CommentInline]
    list_display = ['title', 'component', 'status', 'priority', 'assignee', 'developer', 'due_date']
    list_filter = ['component', 'status', 'priority', 'due_date', 'assignee', 'developer']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('description',)}),
        ('Details', {'fields': ('task', 'added_by', 'add_date', 'parent')}),
    ]
    inlines = [CommentInline]
    list_display = ['description', 'added_by', 'add_date']


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
