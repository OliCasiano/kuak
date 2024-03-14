from django.urls import path
from ducks.views import DuckListAPIView, DuckDetailAPIView

urlpatterns = [
    path('ducks/', DuckListAPIView.as_view()),
    path('ducks/<int:pk>/', DuckDetailAPIView.as_view())
]