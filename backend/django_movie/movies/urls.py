from django.urls import path
from . import views


urlpatterns = [
    path('movieinfo/<int:movie_id>', views.movie_info, name='movieinfo'),
    path('boockingticket/', views.boockingticket, name='boockingticket'),
    path('', views.get_movies, name="index"),
    # path('', views.index, name='index'),
]
