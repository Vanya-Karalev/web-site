from django.urls import path
from . import views


urlpatterns = [
    path('movieinfo/', views.movieinfo, name='movieinfo'),
    path('', views.index, name='index'),
    path('boockingticket/', views.boockingticket, name='boockingticket'),
]
