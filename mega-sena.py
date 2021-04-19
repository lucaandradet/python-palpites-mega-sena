from random import randint #importando a função randint da biblioteca random
from time import sleep #importando a função sleep da biblioteca time

lista = list() #Criando lista vazia para lista
jogos = list() #Criando lista vazia para jogos

print ('-' * 40)
print('       Palpite de jogos na Mega Sena       ')
print('-' * 40)

quant = int(input('Quantos jogos você deseja sortear? '))

tot = 1 #Total de jogos que irá sortear

while tot <= quant:
    cont = 0 
    while True: #Loop infinito
        num = randint(1,60) #Randomizando número de 1 à 60
        if num not in lista: #Validando se o número já existe na lista
            lista.append(num) #Adicionando o número a lista
            cont += 1
        if cont >= 6: #Se o cont for maior ou igual a 6
            break #Sai do loop
    lista.sort() #Coloca os números da lista em ordem
    jogos.append(lista[:]) #Adicionando a lista criada dentro da lista de jogos
    lista.clear() #Apagando a lista
    tot += 1
    
print('-=' * 4, f'Sorteando {quant} jogos', '=-' * 4)

for i, l in enumerate(jogos): #Para o indice da lista de jogos
    print(f'Jogo {i+1}: {l}') #Imprimindo o indice e o jogo salvo dentro da lista de jogos
    sleep(0.5) #Aguarda 0.5 segundos

print('-=' * 4, '< Boa Sorte! >', '=-' * 4)