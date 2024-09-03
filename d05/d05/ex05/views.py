from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from django import forms

class TitleForm(forms.Form):
    title = forms.ChoiceField(choices=[],)

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

        return render(request, 'ex05/populate.html', {'status': status})

    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')
    
def display(request):
    movies = Movies.objects.all() #possible errors?
    
    columns = [field.name for field in Movies._meta.get_fields() if field.concrete]
    context = {'columns': columns, 'movies': movies}

    if not movies:
        return HttpResponse('No data available')

    return render(request, 'ex05/display.html', context)

def remove(request):
    try:
        # delete if post
        if request.method == 'POST':
            selected_title = request.POST.get('title') #use Form methods?

            if selected_title:
                Movies.objects.filter(title=selected_title).delete()

        movies = Movies.objects.all()

        if not movies:
            raise Exception('empty')
        
        form = TitleForm(choices=[(movie.title, movie.title) for movie in movies])
        context = {'form': form}

        return render(request, 'ex05/remove.html', context)

    except Exception as e:
        return HttpResponse('No data available')