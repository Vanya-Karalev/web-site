from dateutil.relativedelta import relativedelta
import requests
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from movies.models import Movie, Comment
from .forms import CommentForm
import datetime
from django.template import Context
from django.template.loader import get_template
from django.template.loader_tags import BlockNode


# def movie_info(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     return render(request, 'movieinfo.html', {'movie': movie})


def boockingticket(request, movie_id):
    boocking = get_object_or_404(Movie, id=movie_id)

    context = {
        'boocking': boocking
    }
    if request.method == 'POST':
        seat_count = int(request.POST['seat_count'])
        print(seat_count)
        # try:
        #     seat_count = int(request.POST['seat_count'])
        #     assert showtime.status == showtime.SALE_OPEN, 'فروش بلیت برای این سانس ممکن نیست.'
        #     assert showtime.free_seats >= seat_count, 'این سانس به اندازه کافی صندلی خالی ندارد.'
        #     price = showtime.price * seat_count
        #     assert request.user.profile.spend(price), 'اعتبار شما برای خرید بلیت کافی نیست.'
        #     showtime.reserve_seats(seat_count)
        #     ticket = Ticket.objects.create(showtime=showtime, customer=request.user.profile, seat_count=seat_count)
        # except Exception as e:
        #     context['error'] = str(e)
        # else:
        #     return HttpResponseRedirect(reverse('ticket_details', kwargs={'ticket_id': ticket.id}))
    # temp = get_template('boockingticket.html')
    # for node in temp.template:
    #     if isinstance(node, BlockNode) and node.name == 'title':
    #         print(node.render(Context()))

    # each_movie = Movie.objects.get(id=movie_id)
    #
    # if request.method == 'POST':
    #     form = CommentForm(request.POST, instance=each_movie)
    #     if form.is_valid():
    #         user = request.user.first_name
    #         content = form.cleaned_data['content']
    #         c = Comment(movie=each_movie, user=user, content=content, date=datetime.now())
    #         c.save()
    #         return redirect('movieinfo')
    #     else:
    #         print('form is invalid')
    # else:
    #     form = CommentForm()
    # context = {
    #     'form': form,
    # }

    return render(request, 'boockingticket.html', {'boocking': boocking})


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

                if main_response['description'] is None or len(main_response['description']) == 0:
                    main_response['description'] = ''
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


def comment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    form = CommentForm(request.POST, instance=movie)
    if request.method == 'POST':

        if form.is_valid():
            user = request.user.username
            content = form.cleaned_data['content']
            c = Comment(movie=movie, user=user, content=content, date=datetime.datetime.now())
            c.save()
            return redirect('index')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    commentary = Comment.objects.filter(movie=movie)

    context = {
        'form': form,
        'movie': movie,
        'commentary': commentary,
    }
    return render(request, 'movieinfo.html', context)
