from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.genre}"


class Comment(models.Model):
    """Stores Comments by users about the movie """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
