#from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):

#pocasi
    appid = '82b797b6ebc625032318e16f1b42c016'
    url_wheather = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Prague'
    res_weather = requests.get(url_wheather.format(city)).json()
    temp = round((res_weather['main']['temp']),1)

    #cov19
    url_cov19 = 'https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/nakaza.min.json'
    res_cov19 = requests.get(url_cov19).json()
    count_cov19 = res_cov19['data'][-1]['pocetDen']
    datum_cov19 = res_cov19['data'][-1]['datum']

    #kurz
    url_kurz = 'https://api.kb.cz/openapi/v1/exchange-rates'
    res_kurz = requests.get(url_kurz).json()
    kurz = round(res_kurz[0]['exchangeRates'][6]['middle'],2)


    data = {'info': temp,
            'pocetDen': count_cov19,
            'datum': datum_cov19,
            "kurz": kurz

            }

    return render(request, "articles/index.html", context=data)
