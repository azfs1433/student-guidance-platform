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
