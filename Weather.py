import requests
import json
from googletrans import Translator

def forecast(city):
    try:
        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=07e06c7b80eb71b6294398b8e8be1815')
        result = json.loads(req.text)
    except:
        print("Um erro ocorreu, por favor tente novamente")
        Main()
        return None
    return result
    
def Main():
    city = input("Deseja consultar o clima de qual cidade? ")
    result = forecast(city)
    weather = translate(result['weather'][0]['main'])
    description = translate(result['weather'][0]['description'])
    temp = int(result['main']['temp']) - 273,15
    print("Temperatura: ",temp[0],"ºC")
    print("Tempo: ",weather )
    print("Descrição: ",description )
    #print(result)

def translate(text):
    translator = Translator()
    text_pt = translator.translate(text, dest='pt')
    return text_pt.text


Main()