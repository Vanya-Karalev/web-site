# Generated by Django 4.0.4 on 2022-06-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_seats_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.PositiveIntegerField(blank=True, null=True, verbose_name='Seat')),
                ('type', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='seats',
            name='seat',
        ),
        migrations.RemoveField(
            model_name='seats',
            name='type',
        ),
        migrations.AddField(
            model_name='seats',
            name='seats',
            field=models.ManyToManyField(related_name='seats', to='movies.seat'),
        ),
    ]
