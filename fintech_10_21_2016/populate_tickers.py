'''
Use os module to give terminal output
'''
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

from hacker5.models import Tickers
import sys
from datetime import datetime

import csv

import warnings
warnings.filterwarnings("ignore")

csv_filepathname="Yahoo Ticker Symbols - Jan 2016.csv"

def populate():
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    for row in dataReader:
        ticker = Tickers()
        ticker.ticker = row[0]
        ticker.name = row[1]
        ticker.exchange = row[2]
        ticker.country = row[3]
        ticker.category_name = row[4]
        ticker.category_number = row[5]
        ticker.save()

#execute here
if __name__ == '__main__':
    print ("Starting ticker population script...")
    populate()