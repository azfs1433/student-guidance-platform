from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ClassRoom, Student, Referral, ReferralStudent, Intervention


# --------- Import/Export (Students) ---------
class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        # الأعمدة اللي بتظهر في ملف التصدير والاستيراد
        fields = ("id", "name", "national_id", "phone", "classroom")
        export_order = ("id", "name", "national_id", "phone", "classroom")

    # مهم: نخلي classroom يقرأ بالـ ID أو بالاسم حسب ما تفضّل
    # إذا تبي بالاسم فقط، خلّ الاستيراد يكون بنفس اسم الفصل بالضبط.


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ("id", "name", "national_id", "classroom", "phone")
    list_filter = ("classroom",)
    search_fields = ("name", "national_id", "phone")


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "reason", "created_by", "assigned_to", "created_at")
    list_filter = ("reason", "created_at")
    search_fields = ("reason", "notes", "created_by__username", "assigned_to__username")


@admin.register(ReferralStudent)
class ReferralStudentAdmin(admin.ModelAdmin):
    list_display = ("id", "referral", "student", "is_closed", "closed_at")
    list_filter = ("is_closed",)
    search_fields = ("student__name", "student__national_id")


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "created_by", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("notes", "created_by__username")
