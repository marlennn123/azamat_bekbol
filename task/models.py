from django.db import models


class Faculty(models.Model):
    name_faculty = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_faculty


class Professor(models.Model):
    name_professor = models.CharField(max_length=32)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    bio = models.TextField()

    def __str__(self):
        return self.name_professor


class Student(models.Model):
    name_student = models.CharField(max_length=32)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name_student


class Course(models.Model):
    name_course = models.CharField(max_length=32)
    code = models.CharField(max_length=16)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name_course