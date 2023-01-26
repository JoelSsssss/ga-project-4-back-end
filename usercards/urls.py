from django.urls import path  # import path from django
from .views import UserCardsListView, UserCardsDetailView

urlpatterns = [
    path('', UserCardsListView.as_view()),
    path('<int:pk>/', UserCardsDetailView.as_view()),
]
