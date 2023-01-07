import datetime

from django.db import models


# Create your models here.
class VacancyModel(models.Model):
    hh_id = models.CharField(max_length=100, default='0000')
    name = models.CharField(max_length=100, default='name')
    published_at = models.DateTimeField(default=datetime.datetime(2023, 1, 7, 15, 10, 47, 625508))
    description = models.TextField(blank=True, null=True)
    key_skills = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=100, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    employer = models.CharField(max_length=100, blank=True, null=True)

