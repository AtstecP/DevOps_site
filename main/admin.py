from django.contrib import admin
from .models import VacancyModel


# Register your models here.
@admin.register(VacancyModel)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('hh_id', 'name', 'published_at',
                    'key_skills', 'address', 'url',
                    'salary', 'employer',)
