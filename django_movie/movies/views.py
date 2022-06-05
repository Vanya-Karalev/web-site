from dateutil.relativedelta import relativedelta
import requests
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from movies.models import Movie, Comment, Ticket, Seats, Seat
from .forms import CommentForm
import datetime
import pytz


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def boockingticket(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    boocking = get_object_or_404(Movie, id=movie_id)

    if 'choices' in request.POST:
        print(request.POST)
        buy_list = [int(i) for i in request.POST.getlist('choices')]
        print(buy_list)

        for buying_ticket in buy_list:
            if not Ticket.objects.filter(movie=movie, seat=buying_ticket).exists():
                Ticket.objects.create(user_first_name=request.user.first_name, user_last_name=request.user.last_name,
                                      user_login=request.user.username, movie=movie, seat=buying_ticket)
        return redirect('movieinfo', movie_id=movie.id)

    context = {
        'boocking': boocking,
        'movie': movie,
    }

    return render(request, 'boockingticket.html', context)


def get_movies(request):
    if settings.NEED_TO_LOAD_FILMS:
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': '8c8e1a50-6322-4135-8875-5d40a5420d86',
        }

        context = {'filmId': []}

        response = requests.request("GET", 'https://kinopoiskapiunofficial.tech/'
                                           'api/v2.2/films/top?type=TOP_AWAIT_FILMS&page=1', headers=headers).json()

        context['filmId'].extend([i['filmId'] for i in response['films']])

        for i in range(16):
            response = requests.request("GET", 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'
                                               f'top?type=TOP_100_POPULAR_FILMS&page={i + 1}', headers=headers).json()

            context['filmId'].extend([i['filmId'] for i in response['films']])

        for film_id in context['filmId']:
            response1 = requests.request("GET",
                                         f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}/distributions',
                                         headers=headers).json()
            context1 = {'date': [i['date'] for i in response1['items']]}

            try:
                film_date = context1['date'][0]

                film_date = film_date.split('-')
            except BaseException:
                continue

            if (datetime.date(int(film_date[0]), int(film_date[1]), int(film_date[2]))) + relativedelta(months=+1) \
                    >= (datetime.date.today()):

                main_response = requests.request(
                    method="GET",
                    url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}',
                    headers=headers,
                ).json()

                if main_response['description'] is None or len(main_response['description']) == 0:
                    main_response['description'] = 'No info about this film('
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
                        movie_length=main_response.get('filmLength', 'Unknown'),
                        category=main_response.get('ratingAgeLimits', ''),
                        price=10,
                        film_id=film_id,
                    )

                else:
                    model = Movie.objects.filter(film_id=film_id).update(
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

    movies = Movie.objects.all().order_by('-title')
    return render(request, 'index.html', {"movie_list": movies})


def comment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if 'date' in request.POST and 'time' in request.POST:
        if request.method == 'POST' and len(request.POST) > 0:
            print(request.POST)

            choice_date = request.POST['date']
            choice_time = request.POST['time']
            new_date = choice_date.split('-')
            new_time = choice_time.split(':')
            date_time = datetime.datetime(int(new_date[0]), int(new_date[1]), int(new_date[2]),
                                          int(new_time[0]), int(new_time[1]))
            timezone = pytz.timezone('Europe/London')
            choice_date_time = timezone.localize(date_time)
            if not Seats.objects.filter(movie=movie, datetime=choice_date_time).exists():
                s = Seats(movie=movie, datetime=choice_date_time)
                s.save()
                for i in range(48):
                    one_seat = Seat.objects.create(type=False, seat=i + 1)
                    one_seat.save()
                    s.seats.add(one_seat)
                    s.save()

            occupied_seats = []

            return redirect('boockingticket', movie_id=movie.id)

    form = CommentForm(request.POST, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user.username
            content = form.cleaned_data['content']
            c = Comment(movie=movie, user=user, content=content, date=datetime.datetime.now())
            c.save()
            return redirect('movieinfo', movie_id=movie.id)
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    commentary = Comment.objects.filter(movie=movie)

    if movie.start_date < datetime.date.today():
        start_date = str(movie.start_date)
        end_date = str(movie.end_date)
        date = str(datetime.date.today())
    else:
        start_date = str(movie.start_date)
        end_date = str(movie.end_date)
        date = str(movie.start_date)

    context = {
        'form': form,
        'movie': movie,
        'commentary': commentary,
        'start_date': start_date,
        'end_date': end_date,
        'date': date,
    }
    return render(request, 'movieinfo.html', context)


def search_results(request):
    if is_ajax(request=request):
        res = None
        movie = request.POST.get('movie')
        qs = Movie.objects.filter(title__icontains=movie)
        if len(qs) > 0 and len(movie) > 0:
            data = []
            for pos in qs:
                item = {
                    'id': pos.id,
                    'title': pos.title,
                    'poster': str(pos.poster)
                }
                data.append(item)
            res = data
        else:
            res = 'No movies found...'

        return JsonResponse({'data': res})
    return JsonResponse({})
