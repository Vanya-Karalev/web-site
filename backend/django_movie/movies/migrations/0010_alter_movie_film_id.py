# Generated by Django 4.0.4 on 2022-05-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_movie_film_id_alter_movie_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='film_id',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
