from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import m2m_changed

from django_testing import settings


class Student(models.Model):
    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )


class Course(models.Model):
    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )

def students_changed(sender, **kwargs):
    if kwargs['instance'].students.count() > settings.MAX_STUDENTS_PER_COURSE:
        raise ValidationError('На одном курсе не может быть больше 20 студентов')

m2m_changed.connect(students_changed, sender=Course.students.through)
