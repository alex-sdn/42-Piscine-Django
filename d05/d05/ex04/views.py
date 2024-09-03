from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import psycopg2

dbname = 'formationdjango'
user = 'djangouser'
password = 'secret'

class TitleForm(forms.Form):
    title = forms.ChoiceField(choices=[],)

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['title'].choices = choices

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='localhost',
            port='5432',
        )
        cursor = conn.cursor()
        
        #create movies table
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ex04_movies (
                        title VARCHAR(64) UNIQUE NOT NULL,
                        episode_nb SERIAL PRIMARY KEY,
                        opening_crawl TEXT,
                        director VARCHAR(32) NOT NULL,
                        producer VARCHAR(128) NOT NULL,
                        release_date DATE NOT NULL
                    );
                """)
        conn.commit()

        #close connection
        cursor.close()
        conn.close()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def populate(request):
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
    ]

    status = []

    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='localhost',
            port='5432',
        )
        cursor = conn.cursor()
        
        #add data to table
        for movie in movies:
            try:
                cursor.execute("""
                            INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                            VALUES (%s, %s, %s, %s, %s)
                        """, movie)
                conn.commit()
                status.append('OK')

            except Exception as e:
                conn.rollback()
                status.append(f'{movie[1]}: {str(e)}')

        cursor.close()
        conn.close()

        return render(request, 'ex04/populate.html', {'status': status})

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='localhost',
            port='5432',
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ex04_movies")
        movies = cursor.fetchall() #fetch rows as list of tuples

        if not movies:
            raise Exception('empty')

        cursor.close()
        conn.close()

        columns = ('title', 'episode_nb', 'opening_crawl', 'director', 'producer', 'release_date')
        context = {'columns': columns, 'movies': movies}

        return render(request, 'ex04/display.html', context)

    except Exception as e:
        return HttpResponse('No data available')

def remove(request):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='localhost',
            port='5432',
        )
        cursor = conn.cursor()

        # delete entry
        if request.method == "POST":
            selected_title = request.POST.get('title')
            
            if selected_title:
                cursor.execute("DELETE FROM ex04_movies WHERE title = %s", (selected_title,))
                conn.commit()

        cursor.execute("SELECT title FROM ex04_movies")
        titles = cursor.fetchall()
        titles = list(elem[0] for elem in titles)

        if not titles:
            raise Exception('empty')

        cursor.close()
        conn.close()

        form = TitleForm(choices=[(title, title) for title in titles])
        context = {'form': form}

        return render(request, 'ex04/remove.html', context)

    except Exception as e:
        return HttpResponse('No data available')
