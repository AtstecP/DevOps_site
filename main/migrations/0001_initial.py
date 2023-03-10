# Generated by Django 4.1.4 on 2023-01-14 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeographyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='geographyPage', max_length=100, verbose_name='Заголовок')),
                ('text_1', models.TextField(default=None, verbose_name='Первый заголовок')),
                ('text_2', models.TextField(default=None, verbose_name='Второй заголовок')),
                ('table_1', models.TextField(default=None, verbose_name='Таблицы для IT')),
                ('table_2', models.TextField(default=None, verbose_name='Таблицы для DevOps')),
                ('graph_IT', models.ImageField(default=None, upload_to='geographypage', verbose_name='IT график')),
                ('graph_devops', models.ImageField(default=None, upload_to='geographypage', verbose_name='DevOps график')),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='homepage', max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(default=None, verbose_name='Текст')),
                ('image', models.ImageField(default=None, upload_to='homepage', verbose_name='img')),
            ],
        ),
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='infopage', max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(default=None, verbose_name='Текст')),
                ('table', models.TextField(default=None, verbose_name='Таблица')),
                ('graph_left', models.ImageField(default=None, upload_to='infopage', verbose_name='Левый график')),
                ('graph_right', models.ImageField(default=None, upload_to='infopage', verbose_name='Правый график')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='skillsPage', max_length=100, verbose_name='Заголовок')),
                ('graph', models.ImageField(blank=True, default=None, null=True, upload_to='skillspage', verbose_name='график')),
                ('text', models.TextField(default=None, verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='VacancyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hh_id', models.CharField(default='0000', max_length=100)),
                ('name', models.CharField(default='name', max_length=100, verbose_name='Название вакансии')),
                ('published_at', models.DateTimeField(default=datetime.datetime(2023, 1, 7, 15, 10, 47, 625508), verbose_name='Дата публикации')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('key_skills', models.TextField(blank=True, null=True, verbose_name='Навыки')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Город')),
                ('url', models.URLField(max_length=100, null=True, verbose_name='Ссылка')),
                ('salary', models.CharField(blank=True, max_length=100, null=True, verbose_name='зарплата')),
                ('employer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя нанимателя')),
            ],
        ),
    ]
