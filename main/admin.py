from django.contrib import admin
from .models import VacancyModel

# Register your models here.
@admin.register(VacancyModel)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'published_at', 'description',)
