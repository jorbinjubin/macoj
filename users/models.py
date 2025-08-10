from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    points = models.IntegerField(default=0)

    # For grades, 9-12 = Grade 9 through 12, 13 = Alumni, 14 = Teacher
    grade = models.IntegerField(max=14, blank=True)

    problems_solved = models.ManyToManyField('problems.Problem', blank=True)
    badges = modles.ManyToManyField('badges.Badge', blank=True)

    