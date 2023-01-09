import datetime

from django.db import models


# Create your models here.
class VacancyModel(models.Model):
    hh_id = models.CharField(max_length=100, default='0000')
    name = models.CharField(
        'Название вакансии',
        max_length=100,
        default='name'
    )
    published_at = models.DateTimeField(
        'Дата публикации',
        default=datetime.datetime(2023, 1, 7, 15, 10, 47, 625508)
    )
    description = models.TextField('Описание', blank=True, null=True)
    key_skills = models.TextField('Навыки', blank=True, null=True)
    address = models.TextField('Город', blank=True, null=True)
    url = models.URLField('Ссылка', max_length=100, null=True)
    salary = models.CharField(
        'зарплата',
        max_length=100,
        blank=True,
        null=True
    )
    employer = models.CharField(
        'Имя нанимателя',
        max_length=100,
        blank=True,
        null=True
    )


class HomePage(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text = models.TextField('Текст', default=None)
    image = models.ImageField(
        'img', default=None,
        upload_to='homepage'
    )


class InfoPage(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='infopage'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'Левый график',
        default=None,
        upload_to='infopage'
    )
    graph_right = models.ImageField(
        'Правый график',
        default=None,
        upload_to='infopage'
    )


class GeographyPage(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geographyPage'
    )
    text_1 = models.TextField('Первый заголовок', default=None)
    text_2 = models.TextField('Второй заголовок', default=None)
    table_1 = models.TextField('Таблицы для IT', default=None)
    table_2 = models.TextField('Таблицы для DevOps', default=None)



class SkillsPage(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skillsPage'
    )
    text = models.TextField('Текст', default=None)
