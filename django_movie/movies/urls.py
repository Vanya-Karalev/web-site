from django.urls import path
from . import views


urlpatterns = [
    path('movieinfo/<int:movie_id>', views.comment, name='movieinfo'),
    # path('search/', views.main_view, name='main'),
    path('search_results/', views.search_results, name='search_results'),
    path('movieinfo/<int:movie_id>/boockingticket/', views.boockingticket, name='boockingticket'),
    path('', views.get_movies, name="index"),
]
