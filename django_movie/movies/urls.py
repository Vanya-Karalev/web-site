from django.urls import path
from . import views

urlpatterns = [
    path('movieinfo/<int:movie_id>', views.comment, name='movieinfo'),
    path('search_results/', views.search_results, name='search_results'),
    path('movieinfo/<int:movie_id>/<str:choice_date_time>/boockingticket/', views.boockingticket,
         name='boockingticket'),
    path('', views.get_movies, name="index"),
]
