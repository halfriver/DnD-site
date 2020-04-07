from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='list'),
    # path('<slug:character_name>/', views.CharacterDetail.as_view()),
    path('<slug:pk>/', views.CharacterDetail.as_view())
]
