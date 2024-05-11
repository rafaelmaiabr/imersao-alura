import requests
import random

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(url)

data = resposta.json()

valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']
#print(f'A palavra secreta tem {len(palavra_secreta)} letras -> {dica}')
# recebe o palpite da tecnologia
print(f'A palavra secreta tem {len(palavra_secreta)} letras')
print(f'A dica é: {dica}')
chute = input(f'O que você acha que é: ')

if chute == palavra_secreta:
  print('Acertou')
else:
  print(f'Errou! A palavra secreta era {palavra_secreta}')
