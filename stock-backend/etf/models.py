from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.symbol} - {self.name}"


class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.FloatField(null=True)
    close = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    volume = models.BigIntegerField(null=True)

    class Meta:
        unique_together = ('stock', 'date')

    def __str__(self):
        return f"{self.stock.symbol} on {self.date}: {self.close}"