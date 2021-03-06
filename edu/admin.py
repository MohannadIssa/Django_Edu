from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['project']

    list_display = ['number', 'fname','mname',
                    'lname', 'project']
    list_editable = ['project']
    list_filter = ['project', 'fname', 'number']
    list_per_page = 10
    list_select_related = ['project']
    search_fields = ['number','fname']

    def project_name(self, student):
        return student.project.name



@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ['name', 'students_count']
    search_fields = ['name']

    @admin.display(ordering='students_count')
    def students_count(self, project):
        url = (
            reverse('admin:edu_student_changelist')
            + '?'
            + urlencode({
                'project__pnumber': str(project.pnumber)
            }))
        return format_html('<a href="{}">{} students</a>', url, project.students_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            students_count=Count('students')
        )

