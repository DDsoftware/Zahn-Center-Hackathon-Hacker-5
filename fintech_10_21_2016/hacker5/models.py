import datetime
from django.db import models

class Tickers(models.Model):
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=128)
    exchange = models.CharField(max_length=3)
    country = models.CharField(max_length=32)
    category_name = models.CharField(max_length=128)
    category_number = models.CharField(max_length=3)
    create_date = models.DateTimeField(default=datetime.datetime.now)

def __unicode__(self):
    return "%s, %s" % (self.ticker, self.name)
