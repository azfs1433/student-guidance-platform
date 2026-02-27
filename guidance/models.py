from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    national_id = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Case(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    case_type = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    action_taken = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.case_type}"
from django.contrib.auth.models import User


class Referral(models.Model):

    REFERRAL_TYPE = [
        ('academic', 'ضعف دراسي'),
        ('absence', 'غياب متكرر'),
        ('late', 'تأخر صباحي'),
    ]

    STATUS = [
        ('new', 'جديد'),
        ('session', 'جلسة ارشادية'),
        ('case', 'دراسة حالة'),
        ('committee', 'لجنة التوجيه الطلابي'),
        ('parent_notify', 'ابلاغ ولي الامر'),
        ('parent_call', 'استدعاء ولي الامر'),
        ('pledge', 'تعهد الطالب'),
        ('closed', 'انهاء الحالة'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    referral_type = models.CharField(max_length=20, choices=REFERRAL_TYPE)
    status = models.CharField(max_length=20, choices=STATUS, default='new')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.get_referral_type_display()}"
        
