from django.urls import path
from .views import StockListView , ETFListView

urlpatterns = [
    path('list/', StockListView.as_view()),
    path('list/etf/', ETFListView.as_view()),
]