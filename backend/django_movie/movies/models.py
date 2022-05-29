from django.db import models


class Genre(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField('Movie title', null=True, blank=True, max_length=250)
    small_description = models.CharField('Small description', null=True, blank=True, max_length=150)
    description = models.TextField('Description', null=True, blank=True)
    poster = models.URLField('Poster', null=True, blank=True, max_length=1000)
    start_date = models.DateField('Premiere beginning', null=True, blank=True)
    end_date = models.DateField('Premiere ending', null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    movie_length = models.PositiveIntegerField('Movie length', null=True, blank=True)
    category = models.CharField('Movie category', null=True, blank=True, default='', max_length=250)
    price = models.PositiveIntegerField('Movie price', default=10)
    film_id = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField('User name', null=True, blank=True, max_length=250)
    movie = models.ForeignKey('Movie', related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.movie)


class Seat(models.Model):
    seat = models.PositiveIntegerField('Seat', null=True, blank=True)

    def __str__(self):
        return self.seat


class Ticket(models.Model):
    user_name = models.CharField('User name', null=True, blank=True, max_length=250)
    user_login = models.CharField('User login', null=True, blank=True, max_length=250)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    date = models.DateField('Date of movie', null=True, blank=True)
    time = models.DateTimeField('Movie date and time', null=True, blank=True)
    seats = models.ManyToManyField(Seat, related_name='seats')
    seat_count = models.PositiveIntegerField('Seat count', null=True, blank=True)
    type = models.CharField('Ticket type', null=True, blank=True, max_length=100)

    def __str__(self):
        return self.movie


# class Times(models.Model):movie_id=movie.id
#     date = models.TimeField('Times', null=True, blank=True, max_length=100)
#
#     def __str__(self):
#         return self.date
