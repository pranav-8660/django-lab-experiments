from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_usn', 'student_sem')
    ordering = ('student_name',)
    search_fields = ('student_name',)

admin.site.register(Course)
