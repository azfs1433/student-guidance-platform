from django.contrib import admin
from .models import ClassRoom, Student, Referral, ReferralStudent, Intervention


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "classroom", "phone")
    list_filter = ("classroom",)
    search_fields = ("name", "phone")


class ReferralStudentInline(admin.TabularInline):
    model = ReferralStudent
    extra = 0


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "reason", "created_by", "assigned_to", "created_at")
    list_filter = ("reason", "created_at")
    search_fields = ("created_by__username",)
    inlines = [ReferralStudentInline]


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "created_by", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("created_by__username", "referral_student__student__name")
    

