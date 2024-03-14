from django.urls import path 
# from films.views import FilmListAPIView, FilmDetailAPIView
from ducks.views import DuckViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('ducks/', DuckListAPIView.as_view()),
#     path('ducks/<int:pk>/', DuckDetailAPIView.as_view())
# ]

router = DefaultRouter()
router.register('ducks', DuckViewSet, basename='ducks')
urlpatterns = router.urls