from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

dbname = 'formationdjango'
user = 'djangouser'
password = 'secret'

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

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ex08_planets (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(64) UNIQUE NOT NULL,
                        climate VARCHAR,
                        diameter INT,
                        orbital_period INT,
                        population BIGINT,
                        rotation_period INT,
                        surface_water REAL,
                        terrain VARCHAR(128)
                    );
                """)
        conn.commit()

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ex08_people (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(64) UNIQUE NOT NULL,
                        birth_year VARCHAR(32),
                        gender VARCHAR(32),
                        eye_color VARCHAR(32),
                        hair_color VARCHAR(32),
                        height INT,
                        mass REAL,
                        homeworld VARCHAR(64),
                        CONSTRAINT fk_homeworld
                            FOREIGN KEY (homeworld)
                            REFERENCES ex08_planets(name)
                    );
                """)
        conn.commit()

        cursor.close()
        conn.close()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')
    
def populate(request):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='localhost',
            port='5432',
        )
        cursor = conn.cursor()

        #copy from .csv
        with open('planets.csv', 'r') as file:
            cursor.copy_from(file, 'ex08_planets', null='NULL', columns=(
                'name', 'climate', 'diameter', 'orbital_period', 
                'population', 'rotation_period', 'surface_water', 'terrain')
            )
            conn.commit()
        
        with open('people.csv', 'r') as file:
            cursor.copy_from(file, 'ex08_people', null='NULL', columns=(
                'name', 'birth_year', 'gender', 'eye_color',
                'hair_color', 'height', 'mass', 'homeworld')
            )
            conn.commit()

        cursor.close()
        conn.close()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')
    
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

        #fetch filtered data
        cursor.execute("""
                    SELECT ppl.name, ppl.homeworld, planet.climate
                    FROM ex08_people ppl
                    JOIN ex08_planets planet ON ppl.homeworld = planet.name
                    WHERE planet.climate ILIKE '%windy%'
                    ORDER BY ppl.name ASC;
            """)
        results = cursor.fetchall()

        if not results:
            raise Exception('empty')
        
        cursor.close()
        conn.close()

        columns = ('name', 'homeworld', 'climate')
        context = {'columns': columns, 'characters': results}

        return render(request, 'ex08/display.html', context)

    except Exception as e:
        return HttpResponse('No data available')