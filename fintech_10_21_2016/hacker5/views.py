from django.shortcuts import render, redirect
from yahoo_finance import Share

def index(request):
    # Get data about Apple share
    apple = Share('AAPL')

    # Get the share price
    data = apple.get_price()
    # OUTPUT: 116.16

    # Since data is changing constantly, you can refresh the share and get the new data
    apple.refresh()
    data2 = apple.get_price()
    # OUTPUT: 116.3811

    # You can access the full share dataset  
    data3 = apple.data_set

    return render(request, 'index.html', {'data': data, 'data2': data2, 'data3': data3})