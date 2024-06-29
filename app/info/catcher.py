# _*_ coding: utf-8 _*_

import requests

from info.format import currency_formatter

def weather():
    """
    Returns weather, temperature (ºC) and condition.
    
    Retorna o tempo, temperatura (ºC) e condição.
    """

    codes= {
            0: "Céu limpo",
            1: "Parcialmente nublado",
            2: "Parcialmente nublado",
            3: "Parcialmente nublado",
            45: "Neblina",
            48: "Neblina",
            51: "Chuvisco",
            53: "Chuvisco",
            55: "Chuvisco",
            56: "Chuvisco congelado",
            57: "Chuvisco congelado",
            61: "Chuva",
            63: "Chuva",
            65: "Chuva",
            66: "Chuva congelada",
            67: "Chuva congelada",
            71: "Neve",
            73: "Neve",
            75: "neve",
            80: "Chuva forte",
            81: "Chuva forte",
            82: "Chuva forte",
            85: "Nevasca",
            86: "Nevasca",
            95: "Tempestade",
            96: "Tempestade",
            99: "Tempestade"
    }

    coordinates= (-29.68, -51.14)

    api= f'https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}8&longitude={coordinates[1]}&current=temperature_2m,rain,weather_code&timezone=America%2FSao_Paulo&forecast_days=1'

    info= requests.get(api).json()

    info['current']['temperature_2m']=  str(info['current']['temperature_2m']).replace('.',',')

    return f"{info['current']['temperature_2m']}ºC {codes[info['current']['weather_code']]}"

def usdXbrl():
    """
    Returns exchange rate of US Dollars x Brazilian Reais.

    Retorna a cotação Dólares americanos x Reais brasileiros.
    """

    currency= ('USD', 'BRL')

    api= f'http://economia.awesomeapi.com.br/json/last/{currency[0]}-{currency[1]}'

    info= requests.get(api).json()

    info["USDBRL"]["ask"]= info["USDBRL"]["ask"][:4].replace('.',',')

    return f'Cotãção do dólar ${info["USDBRL"]["ask"]}'

def btcXbrl():
    """
    Returns Bitcoin exchange rate in Brazil (BRL).

    Retorna a cotação do Bitcoin no Brasil (BRL).
    """

    api= f'https://cointradermonitor.com/api/pbb/v1/ticker'

    info= requests.get(api).json()

    info["last"]= currency_formatter(info["last"])

    return f'Cotação do Bitcoin R${info["last"]}'

def lottery():
    """
    Returns current prize and date of next raffle of brazilian lottery Mega-Sena.

    Retorna prêmio atual e data do próximo sorteio da loteria brasileira Mega-sena.
    """

    api= 'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena'

    info= requests.get(api).json()

    info["valorEstimadoProximoConcurso"]= currency_formatter(info["valorEstimadoProximoConcurso"])

    return {
            'loteria': 'Mega-Sena', 
            "premio": f'prêmio atual R${info["valorEstimadoProximoConcurso"]}',
            "sorteio": f'próximo sorteio em {info["dataProximoConcurso"]}'
    }
