from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def ex00(request):
    dbname = 'formationdjango'
    user = 'djangouser'
    password = 'secret'
    
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
                    CREATE TABLE IF NOT EXISTS ex00_movies (
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
