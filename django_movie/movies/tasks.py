from django_movie.celery import app
from django.core.mail import send_mail
from django_movie.settings import EMAIL_HOST_USER


@app.task(bind=True)
def send(user_login, email, movie_title, seat, date_time):
    send_mail(
        f'Booking a movie ticket: {movie_title}',
        f'Hello, {user_login}! \nYou have booked {seat} seats for the movie:"{movie_title}", date and time:'
        f'{date_time}',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False)
