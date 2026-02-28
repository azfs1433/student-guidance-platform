from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ClassRoom, Student, Referral, ReferralStudent, Intervention


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        # الأعمدة اللي تبيها في الاستيراد/التصدير
        fields = ("id", "name", "national_id", "classroom", "phone")
        import_id_fields = ("national_id",)  # يعتمد عليها بالتحديث بدل تكرار الطلاب
        skip_unchanged = True
        report_skipped = True


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ("id", "name", "national_id", "classroom", "phone")
    list_filter = ("classroom",)
    search_fields = ("name", "national_id", "phone")


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "created_by", "reason", "created_at", "assigned_to")
    list_filter = ("reason", "created_at")
    search_fields = ("notes",)


@admin.register(ReferralStudent)
class ReferralStudentAdmin(admin.ModelAdmin):
    list_display = ("id", "referral", "student", "is_closed", "closed_at")
    list_filter = ("is_closed",)
    search_fields = ("student__name",)


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ("id", "referral_student", "action", "created_by", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("notes",)
