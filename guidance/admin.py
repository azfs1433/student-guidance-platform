from django.contrib import admin
from .models import ClassRoom, Student, Case


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "national_id", "classroom", "phone")
    list_filter = ("classroom",)
    search_fields = ("name", "national_id", "phone")


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "case_type", "date")
    list_filter = ("case_type", "date")
    search_fields = ("student__name", "student__national_id", "case_type")
