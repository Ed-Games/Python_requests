import requests
import json
import datetime
import time


def main():
    var1 = input('Qual moeda deseja converter em Reais, USD(Dolar) ou EUR(euro)? \n ')
    if var1 == 'USD' or var1 == 'EUR':
        quant= float(input('informe a quantidade: '))
    else:
        print('Moeda desconhecida, tente de novo')
        main()
        return None

    while True:
        cotacao = request(var1)
        print(quant,' ',var1,'=',cotacao*quant,' em BRL às ',datetime.datetime.now(),' horas')
        time.sleep(3)

def request(var1):
    req = requests.get('https://economia.awesomeapi.com.br/all/'+var1+'-BRL')
    result = json.loads(req.text)
    return float(result[var1]['ask'])


main()