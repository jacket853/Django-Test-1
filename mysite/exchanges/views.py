from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

currencies = {
    "euro":"1.00 EUR:1.09 USD",
    "bitcoin":"1.00 BTC:23,863.99 USD",
    "ethereum":"1.00 ETH:1,576.78 USD",
    "peso":"1.00 MXN:0.054 USD",
    "yen":"1.00 JPY:0.0078 USD",
    "pound":"1.00 GBP:1.23 USD",
    "yuan":"1.00 CNY:0.15 USD",
    "rupee":"1.00 INR:0.012 USD",
    "ruble":"1.09 RUB:0.014 USD",
    "krone":"1.00 NOK:0.099 USD"
}

def index(request):
    monies = list(currencies.keys())
    return render(request, "exchanges/index.html", {
        "rates_key":monies
    })

def money_target(request, money_type):
    dataToReturn = ""

    try:
        dataToReturn = currencies[money_type]
        return render(request, "exchanges/exchange.html", {
            "text":dataToReturn,
            "money_name":money_type.capitalize()
        })
    except:
        return HttpResponseNotFound("ERROR; money_type")
