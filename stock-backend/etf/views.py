from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ETF

class RecommendETFView(APIView):
    def get(self, request):
        data = [
            {"symbol": "0050", "name": "元大台灣50", "score": 9.2},
            {"symbol": "0056", "name": "元大高股息", "score": 8.5},
            {"symbol": "00881", "name": "國泰台灣5G+", "score": 8.3},
        ]
        return Response(data)


class ETFListView(APIView):
    def get(self, request):
        queryset = ETF.objects.all().values('symbol', 'name', 'price', 'category')
        return Response(list(queryset))