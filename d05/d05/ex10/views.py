from django.shortcuts import render
from django import forms
from .models import Planets, People, Movies

class SearchForm(forms.Form):
    min_date = forms.DateField(label='Movies minimum release date')
    max_date = forms.DateField(label='Movies maximum release date')
    diameter = forms.IntegerField(label='Planet diameter greater than')
    gender = forms.ChoiceField(choices=[], label="Character gender")

    def __init__(self, *args, **kwargs):
        genders = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['gender'].choices = genders


def ex10(request):
    results = []
    genders = People.objects.values_list('gender', flat=True).distinct()
    
    if request.method == 'POST':
        form = SearchForm(request.POST, choices=[(gender, gender) for gender in genders])

        if form.is_valid():
            min_date = form.cleaned_data['min_date']
            max_date = form.cleaned_data['max_date']
            diameter = form.cleaned_data['diameter']
            gender = form.cleaned_data['gender']

            movies = Movies.objects.filter(
                release_date__range=(min_date, max_date),
                characters__homeworld__diameter__gt=diameter,
                characters__gender=gender
            ).distinct()

            for movie in movies:
                #get the characters in movie that match
                characters = People.objects.filter(
                    movies=movie,
                    gender=gender,
                    homeworld__diameter__gt=diameter
                )
                for char in characters:
                    results.append((movie.title, char.name, gender, char.homeworld.name, char.homeworld.diameter))

    form = SearchForm(choices=[(gender, gender) for gender in genders])
    
    context = {'form': form, 'results': results}
    return render(request, 'ex10/ex10.html', context)
