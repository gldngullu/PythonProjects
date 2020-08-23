from django.db import models
from django.contrib.auth.models import User

DAYS = ((0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"))

CLASS_HOURS = ((0, "9.00"),
               (1, "10.00"),
               (2, "11.00"),
               (3, "12.00"),
               (4, "13.00"),
               (5, "14.00"),
               (6, "15.00"),
               (7, "16.00"))


class Course(models.Model):
    courseName = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    courseCode = models.CharField(max_length=10)
    courseDescription = models.TextField()
    courseDay = models.IntegerField(choices=DAYS, default=None)
    courseHourStart = models.IntegerField(choices=CLASS_HOURS, default=None)
    courseHourEnd = models.IntegerField(choices=CLASS_HOURS, default=None)

    def __str__(self):
        return self.courseCode


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return '{self.user.username} Profile'


