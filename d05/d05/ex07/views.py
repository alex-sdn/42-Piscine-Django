from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from django import forms

class UpdateForm(forms.Form):
    title = forms.ChoiceField(choices=[],)
    Input = forms.CharField(label="Input")

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['title'].choices = choices

def populate(request):
    try:
        movies = [
            [1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'],
            [2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'],
            [3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'],
            [4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'],
            [5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'],
            [6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'],
            [7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'],
        ]
        status = []

        for movie in movies:
            try:
                Movies.objects.create(
                    episode_nb=movie[0],
                    title=movie[1],
                    director=movie[2],
                    producer=movie[3],
                    release_date=movie[4]
                )
                status.append('OK')
            except Exception as e:
                status.append(f'Error: {str(e)}')

        return render(request, 'ex07/populate.html', {'status': status})

    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')
    
def display(request):
    movies = Movies.objects.all()
    
    columns = [field.name for field in Movies._meta.get_fields() if field.concrete]
    context = {'columns': columns, 'movies': movies}

    if not movies:
        return HttpResponse('No data available')

    return render(request, 'ex07/display.html', context)

def update(request):
    try:
        if request.method == 'POST':
            movies = Movies.objects.all()
            form = UpdateForm(request.POST, choices=[(movie.title, movie.title) for movie in movies])

            if form.is_valid():
                selected_title = form.cleaned_data['title']
                input_data = form.cleaned_data['Input']
                # Update opening_crawl
                movie = Movies.objects.get(title=selected_title)
                movie.opening_crawl = input_data
                movie.save() #for updated field

        movies = Movies.objects.all()

        if not movies:
            raise Exception('empty')
        
        form = UpdateForm(choices=[(movie.title, movie.title) for movie in movies])
        context = {'form': form}

        return render(request, 'ex07/update.html', context)

    except Exception as e:
        return HttpResponse('No data available')