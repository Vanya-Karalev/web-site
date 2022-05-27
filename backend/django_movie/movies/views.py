from dateutil.relativedelta import relativedelta
import requests
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from movies.models import Movie
import datetime


# def index(request):
#     return render(request, 'index.html')


def movie_info(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movieinfo.html', {'movie': movie})


def boockingticket(request):
    return render(request, 'boockingticket.html')


# class MovieAPI(View):

def get_movies(request):
    if settings.NEED_TO_LOAD_FILMS:
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': '8c8e1a50-6322-4135-8875-5d40a5420d86',
        }

        context = {'filmId': []}

        for i in range(5):
            response = requests.request("GET", 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'
                                               f'top?type=TOP_100_POPULAR_FILMS&page={i+1}', headers=headers).json()

            context['filmId'].extend([i['filmId'] for i in response['films']])

        for film_id in context['filmId']:
            response1 = requests.request("GET", f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}/distributions',
                                         headers=headers).json()
            context1 = {'date': [i['date'] for i in response1['items']]}

            film_date = context1['date'][0]

            if film_date is None:
                continue

            film_date = film_date.split('-')

            if (datetime.date(int(film_date[0]), int(film_date[1]), int(film_date[2]))) + relativedelta(months=+1) \
                    >= (datetime.date.today()):

                main_response = requests.request(
                    method="GET",
                    url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}',
                    headers=headers,
                ).json()

                if main_response['shortDescription'] is None or len(main_response['shortDescription']) == 0:
                    main_response['shortDescription'] = main_response['description'][:150]

                if not Movie.objects.filter(film_id=film_id).exists():
                    model = Movie.objects.create(
                        title=main_response.get('nameRu', ''),
                        small_description=main_response['shortDescription'][:150],
                        description=main_response['description'],
                        poster=main_response.get('posterUrl', ''),
                        start_date=datetime.date(int(film_date[0]), int(film_date[1]), int(film_date[2])),
                        end_date=datetime.date(int(film_date[0]), int(film_date[1]), int(film_date[2])) + relativedelta(
                            months=+1),
                        # genres=main_response['genres'],
                        movie_length=main_response.get('filmLength', '00:00'),
                        category=main_response.get('ratingAgeLimits', ''),
                        price=10,
                        film_id=film_id,
                    )
                else:
                    Movie.objects.filter(film_id=film_id).update(
                        title=main_response.get('nameRu', ''),
                        small_description=main_response['shortDescription'][:150],
                        description=main_response['description'],
                        poster=main_response.get('posterUrl', ''),
                        start_date=datetime.date(int(film_date[0]), int(film_date[1]), int(film_date[2])),
                        end_date=datetime.date(int(film_date[0]), int(film_date[1]), int(film_date[2])) + relativedelta(
                            months=+1),
                        # genres=main_response['genres'],
                        movie_length=main_response.get('filmLength', '00:00'),
                        category=main_response.get('ratingAgeLimits', ''),
                        price=10,
                        film_id=film_id,
                    )
        settings.NEED_TO_LOAD_FILMS = False

    movies = Movie.objects.all()
    return render(request, 'index.html', {"movie_list": movies})
