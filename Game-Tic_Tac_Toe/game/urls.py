from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<int:id>/<str:name>/', views.game, name='game_with_name'),
]
