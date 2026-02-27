from django.contrib import admin
from .models import ClassRoom, Student, Referral, ReferralStudent, Intervention


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "classroom", "phone")
    list_filter = ("classroom",)
    search_fields = ("name", "phone", "classroom__name")


class ReferralStudentInline(admin.TabularInline):
    model = ReferralStudent
    extra = 0
    autocomplete_fields = ("student",)


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "reason", "created_by", "assigned_to", "created_at")
    list_filter = ("reason", "created_at")
    search_fields = ("notes", "created_by__username", "assigned_to__username")
    inlines = [ReferralStudentInline]


@admin.register(ReferralStudent)
class ReferralStudentAdmin(admin.ModelAdmin):
    list_display = ("id", "referral", "student", "is_closed", "closed_at")
    list_filter = ("is_closed",)
    search_fields = ("student__name",)


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ("id", "referral_student", "action", "created_by", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("referral_student__student__name", "notes", "created_by__username")
