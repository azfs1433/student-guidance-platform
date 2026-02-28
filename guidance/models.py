from django.db import models
from django.contrib.auth.models import User


class ClassRoom(models.Model):
    # مثال: "أول متوسط 1"
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
national_id = models.CharField(max_length=20)
classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} - {self.classroom.name}"
        

class Referral(models.Model):
    """
    التحويل من (معلم/وكيل/إداري) إلى (موجه طلابي)
    ويمكن أن يحتوي أكثر من طالب
    """
    REASON_CHOICES = [
        ("weak", "ضعف دراسي"),
        ("absence", "غياب متكرر"),
        ("late", "تأخر صباحي متكرر"),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referrals_created")
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # لاحقاً إذا عندك أكثر من موجه نقدر نستخدم assigned_to
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="referrals_assigned"
    )

    students = models.ManyToManyField(Student, through="ReferralStudent", related_name="referrals")

    def __str__(self):
        return f"{self.get_reason_display()} - {self.created_at:%Y-%m-%d}"


class ReferralStudent(models.Model):
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # حالة الطالب داخل التحويل (مفتوح/مغلق)
    is_closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("referral", "student")

    def __str__(self):
        return f"{self.student.name} ({self.referral.get_reason_display()})"


class Intervention(models.Model):
    """
    إجراءات الموجه على الطالب المحوّل
    """
    ACTION_CHOICES = [
        ("session", "فتح جلسة إرشادية"),
        ("case", "فتح دراسة حالة"),
        ("committee", "تحويل لجنة التوجيه الطلابي"),
        ("notify_parent", "إبلاغ ولي أمر الطالب"),
        ("summon_parent", "استدعاء ولي أمر الطالب"),
        ("pledge_close", "تعهد الطالب بالالتزام وتم إنهاء الحالة"),
    ]

    referral_student = models.ForeignKey(ReferralStudent, on_delete=models.CASCADE, related_name="interventions")
    action = models.CharField(max_length=30, choices=ACTION_CHOICES)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interventions_created")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referral_student.student.name} - {self.get_action_display()}"
        
