from django.db import models


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    # poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    # directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    # actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    # genres = models.ManyToManyField(Genre, verbose_name="жанры")
    # world_premiere = models.DateField("Примьера в мире", default=date.today)
    # budget = models.PositiveIntegerField("Бюджет", default=0,
    #                                      help_text="указывать сумму в долларах")
    # fees_in_usa = models.PositiveIntegerField(
    #     "Сборы в США", default=0, help_text="указывать сумму в долларах"
    # )
    # fess_in_world = models.PositiveIntegerField(
    #     "Сборы в мире", default=0, help_text="указывать сумму в долларах"
    # )
    # category = models.ForeignKey(
    #     Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    # )
    # url = models.SlugField(max_length=130, unique=True)
    # draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Comment(models.Model):
    article = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author_name = models.CharField('имя автоpа', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
