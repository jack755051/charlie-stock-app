from django.urls import path
from .views import RecommendETFView ,ETFListView

urlpatterns = [
    path('recommend/', RecommendETFView.as_view()),
    path('list/', ETFListView.as_view()),
]