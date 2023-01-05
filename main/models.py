from django.db import models

# Create your models here.
class VacancyModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)