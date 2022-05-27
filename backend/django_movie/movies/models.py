from django.db import models


class Genre(models.Model):
    name = models.CharField(default='', max_length=50)

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
    user = models.CharField('User name', default='', max_length=250)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Ticket(models.Model):
    user = models.CharField('User name', default='', max_length=250)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    time = models.DateTimeField('Movie date and time', default=None)
    seat = models.PositiveIntegerField('Seat', default=0)

    def __str__(self):
        return self.movie
