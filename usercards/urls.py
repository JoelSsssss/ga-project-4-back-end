from django.urls import path  # import path from django
from .views import UserCardsListView  # import class from .views

urlpatterns = [
    path('', UserCardsListView.as_view()),
]
