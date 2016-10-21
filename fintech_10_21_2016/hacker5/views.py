from django.shortcuts import render, redirect
from yahoo_finance import Share

from hacker5.models import Tickers

def index(request):
    return render(request, 'index.html')

def search(request):
    data = []
    keyword = request.POST['keyword']
    close = None
    price = None
    ticker = None
    trade = None
    symbol = None
    much = None
    different = None
    many = None
    time = None
    moc = None
    stop = None
    order = None
    open_price = None
    change = None
    market = None
    cycle = None
    name = None

    words = keyword.split()
    for word in words:
        print(word)
        word = word.lower()
        if word == "close" or word == "closing" or word == "closed" or word == "previous":
            close = True
        if word == "price" or word == "pricing" or word == "priced" or word == "value" or word == "values" or word == "valued" or word == "cost" or word == "costed" or word == "stock":
            price = True
        if Tickers.objects.filter(ticker=word.upper()).exists():
            ticker = word.upper()
        if word == "trade" or word == "trading" or word == "traded":
            trade = True
        if word == "ticker" or word == "tickers":
            symbol = True
        if word == "much":
            much = True
        if word == "different":
            different = True
        if word == "many":
            many = True
        if word == "time":
            time = True
        if word == "moc":
            moc = True
        if word == "market":
            if close == "True":
                moc = True
        if word == "stop":
            stop = True
        if word == "order" or word == "orders":
            order = True
        if word == "open" or word == "opens" or word == "opened":
            open_price = True
        if word == "change" or word == "changed":
            change == True
        if word == "market" or word == "markets":
            market = True
        if word == "low" or word == "high":
            cycle = True
        if word == "name":
            name = True
        else:
            print(2)

    if ticker != None:
        sym = Share(ticker)
    if market == True and time == True and order == True and stop == True:
        moc = False
        data.append("All MOC orders must be received at NYSE markets by 15:45 ET, unless entered to offset a published imbalance. NYSE markets' rules also prohibit the cancellation or word == reduction in size of any market-on-close (MOC) order after 15:45 ET.")
    if moc == True:
        data.append("All MOC orders must be received at NYSE markets by 15:45 ET, unless entered to offset a published imbalance. NYSE markets' rules also prohibit the cancellation or word == reduction in size of any market-on-close (MOC) order after 15:45 ET.")
    if price == True and ticker != None:
        data.append(ticker + " price: " + sym.get_price())
    if close == True and ticker != None:
        data.append(ticker + " previous close price: " + sym.get_prev_close())
    if open_price == True and ticker != None:
        data.append(ticker + " open price: " + sym.get_open())
    if different == True and symbol == True:
        data.append("The total number of different tickers: " + str(Tickers.objects.count()))
    if trade == True and ticker != None:
        data.append(ticker + " has traded: " + str(sym.get_volume()))
    if change == True and ticker != None:
        data.append(ticker + " price has changed by: " + str(sym.get_change()))
    if cycle == True and ticker != None:
        data.append(ticker + " daily low has changed by: " + str(sym.get_days_high()))
        data.append(ticker + " daily high has changed by: " + str(sym.get_days_low()))
        data.append(ticker + " yearly low has changed by: " + str(sym.get_year_low()))
        data.append(ticker + " yearly high has changed by: " + str(sym.get_year_high()))
    if name == True and ticker != None:
        data.append(ticker + " name is: " + str(sym.get_name()))
    if data == [] and ticker != None:
        data.append(ticker + " price: " + sym.get_price())
    elif data == []:
        data.append("Please enter ticker names")
    return render(request, 'index.html', {'data': data, 'keyword': keyword})