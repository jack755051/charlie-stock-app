from django.contrib import admin
from .models import Stock, StockPrice

# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'category', 'updated_at')
    list_filter = ('category', 'updated_at')
    search_fields = ('symbol', 'name')

@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'open', 'close', 'volume')
    list_filter = ('date',)
    search_fields = ('stock__symbol', 'stock__name')
