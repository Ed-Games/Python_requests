import oauth2
import json
import urllib.parse

#Your keys (suas chaves):
api_key = 'your consumer key'
api_secret_key = 'your consumer key secret '
access_token = 'your token'
access_token_secret = 'your token secret'

#OBS: create a developer acount on twitter to get the keys (crie uma conta de desenvolvedor no twitter para pegar as chaves)
#link: https://developer.twitter.com/en/apps/18313913 

#oauth2 validation (validação com ouath2):
consumer = oauth2.Consumer(api_key,api_secret_key)
token = oauth2.Token(access_token,access_token_secret)
client = oauth2.Client(consumer,token)


#Pesquise por algo no twitter
def request():
    try:
        word = input("Pesquise no Twitter: " )

        #coding string to prevent problems with special characters (codificando strings para prevenir problemas com caracteres especiais)
        query = urllib.parse.quote(word, safe='')
        req = client.request('https://api.twitter.com/1.1/search/tweets.json?q='+query)
        return req
    except:
        print('Desculpe, um erro ocorreu, tente novamente e verifique se sua digitação está correta')
        request()
        return None
    
#Show results and prevent errors (mostrar resultados e prevenir erros)
def show(tweets):
    try:
        for tweet in tweets['statuses']:
            print(tweet['user']['screen_name'])
            print(tweet['text'])
            print()
    except:
        print("Desculpe, um erro ocorreu, tente novamente e verifique se sua digitação está correta")
        text = request()
        tweets = json.loads(text[1].decode())
        show(tweets) 


#Code starts here (código começa aqui)
def main():
    text = request()
    tweets = json.loads(text[1].decode())
    show(tweets)
    

main()




