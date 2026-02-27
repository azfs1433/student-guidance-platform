from django.contrib import admin
from .models import ClassRoom, Student, Case

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "classroom", "phone")
    list_filter = ("classroom",)
    search_fields = ("name", "phone", "national_id")

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "case_type", "date")
    list_filter = ("case_type", "date")
    search_fields = ("student__name", "description", "action_taken")
    
