from django.shortcuts import render
from .models import VacancyModel
from .utils import add_vacancies


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def info(request):
    return render(request, 'main/info.html')


def geography(request):
    return render(request, 'main/geography.html')


def vacancies(request):
    add_vacancies()
    return render(request, 'main/vacanvies_template.html',
                  context={'vacancies': VacancyModel.objects.order_by('-published_at')[:10], })


def skills(request):
    return render(request, 'main/skills.html')


