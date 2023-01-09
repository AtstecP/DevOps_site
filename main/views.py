from django.shortcuts import render
from .models import VacancyModel, HomePage, InfoPage, SkillsPage, GeographyPage
from .utils import add_vacancies


# Create your views here.

def home(request):
    homepage = HomePage.objects.all()[0]
    return render(
        request,
        'main/home.html',
        context={
            'homepage': homepage,
        }
    )


def info(request):
    infopage = InfoPage.objects.all()[0]
    return render(
        request,
        'main/info.html',
        context={
            'infopage': infopage,
        }
    )


def geography(request):
    geographypage = GeographyPage.objects.all()[0]
    return render(
        request,
        'main/geography.html',
        context={
            'geographypage': geographypage,
        }
    )


def vacancies(request):
    add_vacancies()
    return render(request, 'main/vacanvies_template.html',
                  context={'vacancies': VacancyModel.objects.order_by('-published_at')[:10], })


def skills(request):
    skillspage = SkillsPage.objects.all()[0]
    return render(
        request,
        'main/skills.html',
        context={
            'skillspage':skillspage,
        }
    )


