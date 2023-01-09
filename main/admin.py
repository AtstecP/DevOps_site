from django.contrib import admin
from .models import VacancyModel, InfoPage, GeographyPage, SkillsPage
from .models import HomePage


# Register your models here.

@admin.register(VacancyModel)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('hh_id', 'name', 'published_at',
                    'key_skills', 'address', 'url',
                    'salary', 'employer',)


@admin.register(HomePage)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(InfoPage)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(GeographyPage)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SkillsPage)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)
