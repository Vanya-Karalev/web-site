from django.core.mail import send_mail
from django_movie.settings import EMAIL_HOST_USER


def send(uselogin, email, movie_title, seat, date_time):
    send_mail(
        f'Бронирование билета на фильм: {movie_title}',
        f'Здравствуйте, {uselogin}! \nВы забронировали {seat} места на фильм:"{movie_title}", дата и время:'
        f'{date_time}',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False)
