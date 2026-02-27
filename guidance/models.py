from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Case(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    case_type = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="قيد المتابعة")

    def __str__(self):
        return self.case_type
