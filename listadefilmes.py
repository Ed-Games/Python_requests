import requests
import json
import sys

def movieInfo():
    try:
        movie= input("Nome do filme: ")
        req = requests.get('http://www.omdbapi.com/?apikey=5b5be94f&t='+movie+'&type=movie')
        info = json.loads(req.text)
        return info
    except Exception as error:
        print("Desculpe, um erro ocorreu: ", error)
        return False

def show(info):
    print("title: ",info['Title'])
    print("ano: ",info['Year'])
    print("Duração: ",info['Runtime'])
    print("Gênero: ",info['Genre'])
    print("Diretor: ",info['Director'])
    print("Escritor: ",info['Writer'])
    print("Atores: ",info['Actors'])
    print("Lingua: ",info['Language'])
    print("País: ",info['Country'])
    print("Prêmios: ",info['Awards'])
    print("Nota: ",info['imdbRating'])
    print("Votantes: ",info['imdbVotes'])

args =sys.argv

if len(args) > 2:
    print("excesso de argumentos")
    exit()
elif args[1] == 'info':
    info = movieInfo()
    show(info)
    





