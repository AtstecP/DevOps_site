from django.shortcuts import render
from .models import VacancyModel
import requests

# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def info(request):
    return render(request, 'main/info.html')


def geography(request):
    return render(request, 'main/geography.html')


def vacancies(request):

    set_vacancyModels(get_vacancies())
    return render(request, 'main/vacanvies_template.html', context={'vacancies': VacancyModel.objects.all(), })


def skills(request):
    return render(request, 'main/skills.html')


def set_vacancyModels(vacancies):
    models = VacancyModel.objects.all()
    for i, item in enumerate(models):
        item.name = vacancies[i]['name']
        item.published_at = vacancies[i]['published_at']
        item.description = vacancies[i]['description']
        item.key_skills = vacancies[i]['key_skills']
        item.address = vacancies[i]['area']
        item.url = vacancies[i]['alternate_url']
        item.employer = vacancies[i]['employer']['name']
        item.salary = vacancies[i]['salary']
        item.save()


def clean_vacancy(vacancy):
    vacancy['area'] = vacancy['area']['name'] if vacancy['area'].__contains__('name') else 'Нет данных'
    if vacancy['salary']['from'] != None and vacancy['salary']['to'] != None:
        vacancy[
            'salary'] = f"от {vacancy['salary']['from']} до {vacancy['salary']['to']} {vacancy['salary']['currency']}"
    elif vacancy['salary']['from'] != None:
        vacancy['salary'] = f"{vacancy['salary']['from']} {vacancy['salary']['currency']}"
    elif vacancy['salary']['to'] != None:
        vacancy['salary'] = f"{vacancy['salary']['to']} {vacancy['salary']['currency']}"
    else:
        vacancy['salary'] = 'Нет данных'
    print(vacancy['salary'])
    vacancy['key_skills'] = ', '.join(map(lambda x: x['name'], vacancy['key_skills']))
    return vacancy


def get_vacancies():
    data = []
    info = requests.get('https://api.hh.ru/vacancies?text=%22devops%22&specialization=1&per_page=100').json()
    for row in info['items']:
        if row['name'].lower().__contains__('devops') and not row['salary'] is None:
            data.append({'id': row['id'], 'published_at': row['published_at']})
    data = sorted(data, key=lambda x: x['published_at'], reverse=True)
    print(data)
    vacancies = []
    for i, vacancy in enumerate(data):
        if i == 10:
            break
        vacancies.append(clean_vacancy(requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()))
    print(vacancies)
    return vacancies
