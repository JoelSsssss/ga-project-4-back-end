from django.urls import path
from .views import TemplatesListView
urlpatterns = [
    path('', TemplatesListView.as_view())
]
