from django.db import models


# Create your models here.
class VacancyModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    key_skills = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=100, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    employer = models.CharField(max_length=100, blank=True, null=True)