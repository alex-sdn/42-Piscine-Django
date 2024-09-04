from django.shortcuts import render
from django.http import HttpResponse
from .models import Planets, People

def display(request):
    characters = (People.objects
        .filter(homeworld__climate__icontains='windy')
        .select_related('homeworld')
        .order_by('name')
        .values_list('name', 'homeworld__name', 'homeworld__climate')
    )

    if not characters:
        return HttpResponse('No data available, please use the following command line before use: python3 manage.py loaddata ex09/fixtures/ex09_initial_data.json')

    columns = ('name', 'homeworld', 'climate')
    context = {'columns': columns, 'characters': characters}

    return render(request, 'ex09/display.html', context)
