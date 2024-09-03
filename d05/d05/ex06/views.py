from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import psycopg2

dbname = 'formationdjango'
user = 'djangouser'
password = 'secret'

class UpdateForm(forms.Form):
    title = forms.ChoiceField(choices=[],)
    Input = forms.CharField(label="Input")

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
                    CREATE TABLE IF NOT EXISTS ex06_movies (
                        title VARCHAR(64) UNIQUE NOT NULL,
                        episode_nb SERIAL PRIMARY KEY,
                        opening_crawl TEXT,
                        director VARCHAR(32) NOT NULL,
                        producer VARCHAR(128) NOT NULL,
                        release_date DATE NOT NULL,
                        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
        conn.commit()

        #add trigger function
        cursor.execute("""
                    CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                    RETURNS TRIGGER AS $$
                    BEGIN
                    NEW.updated = now();
                    NEW.created = OLD.created;
                    RETURN NEW;
                    END;
                    $$ language 'plpgsql';
                    CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                    ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                    update_changetimestamp_column();
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
                            INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
                            VALUES (%s, %s, %s, %s, %s)
                        """, movie)
                conn.commit()
                status.append('OK')

            except Exception as e:
                conn.rollback()
                status.append(f'{movie[1]}: {str(e)}')

        cursor.close()
        conn.close()

        return render(request, 'ex06/populate.html', {'status': status})

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

        cursor.execute("SELECT * FROM ex06_movies")
        movies = cursor.fetchall()

        if not movies:
            raise Exception('empty')

        cursor.close()
        conn.close()

        columns = ('title', 'episode_nb', 'opening_crawl', 'director', 'producer', 'release_date', 'created', 'updated')
        context = {'columns': columns, 'movies': movies}

        return render(request, 'ex06/display.html', context)

    except Exception as e:
        return HttpResponse('No data available')

def update(request):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='localhost',
            port='5432',
        )
        cursor = conn.cursor()

        if request.method == "POST":
            cursor.execute("SELECT title FROM ex06_movies")
            titles = cursor.fetchall()
            titles = list(elem[0] for elem in titles)

            form = UpdateForm(request.POST, choices=[(title, title) for title in titles])

            if form.is_valid():
                selected_title = form.cleaned_data['title']
                input_data = form.cleaned_data['Input']
                # Update opening_crawl
                cursor.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s", (input_data, selected_title))
                conn.commit()

        cursor.execute("SELECT title FROM ex06_movies")
        titles = cursor.fetchall()
        titles = list(elem[0] for elem in titles)

        if not titles:
            raise Exception('empty')

        cursor.close()
        conn.close()

        form = UpdateForm(choices=[(title, title) for title in titles])
        context = {'form': form}

        return render(request, 'ex06/update.html', context)

    except Exception as e:
        return HttpResponse('No data available')
