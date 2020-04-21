from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharactersList.as_view(), name='characters_list'),
    # path('<slug:character_name>/', views.CharacterDetail.as_view()),
    path('<slug:name>/', views.CharacterDetail.as_view())
]
