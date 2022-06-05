from django.contrib import admin
from .models import Genre, Movie, Comment, Ticket, Seat


admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(Seat)
