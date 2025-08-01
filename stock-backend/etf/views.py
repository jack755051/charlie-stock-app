from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock,StockPrice

class StockListView(APIView):
    def get(self, request):
        queryset = Stock.objects.all().values('symbol', 'name', 'category')
        return Response(list(queryset))

class ETFListView(APIView):
    def get(self, request):
        queryset = Stock.objects.filter(category='ETF').values('symbol', 'name', 'category')
        data = list(queryset)
        return Response({
            "count": len(data),  # 總筆數
            "results": data      # 股票清單
        })