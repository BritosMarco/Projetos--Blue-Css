#Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#O programa tem que:


# importando as bibliotecas
from itertools import count
from random import randint
import time
import operator

# Declarando listas e variavies
sorteio = list()
vencedor = dict()
ranking = list()
ranking_final = list()
vitoria = vit_jog_1 = vit_jog_2 = vit_jog_3 = vit_jog_4 = rodada =  0


# exibindo o cabeçalho criando o dicionario e sorteando os dados aleatoriamente no mesmo comando
print()
print('-'*30)
print('Emocionante Jogo de Dados ')
print('-'*30)
print('''Regras: 
        - Você definirá quantas rodadasquer jogar.
        - O grande CAMPEÃO será o jogador\n vencedor do maior número de rodadas
        - Será apurado rodadas empatadas 
        - Ao final será apurado o grande Vencedor e o Raking Final''')
print('-'*60)
print()
# Definindo e validando a quantidade de jogadas
jog = int(input('Digite Quantas Rodadas ou [0] para sair: '))
while True:
  if jog == 0: # apurando se o jogador decidiu encerrar o jogo
    print('Você decidiu não jogar') 
    break # encerra o laço while e o jogo
  for n in range(jog): #criando o dicionario e sorteando os dados aleatoriamente no mesmo comando
    jogo = {'jogador 1': randint(1,6),
            'jogador 2': randint(1,6),
            'jogador 3': randint(1,6),
            'jogador 4': randint(1,6)}
    
    rodada += 1
    print()
    print('-'*30)
    print(f'      ***{rodada}ª RODADA ***')
    print('-'*30)
# Neste bloco estamos apurando o jogador vencedor em cada rodada
    if jogo['jogador 1'] > jogo['jogador 2'] and jogo['jogador 1'] > jogo['jogador 3'] and jogo['jogador 1'] > jogo['jogador 4']:
        vit_jog_1 += 1
    elif jogo['jogador 2'] > jogo['jogador 1'] and jogo['jogador 2'] > jogo['jogador 3'] and jogo['jogador 2'] > jogo['jogador 4']:
        vit_jog_2 += 1
    elif jogo['jogador 3'] > jogo['jogador 1'] and jogo['jogador 3'] > jogo['jogador 2'] and jogo['jogador 3'] > jogo['jogador 4']: 
        vit_jog_3 += 1
    elif jogo['jogador 4'] > jogo['jogador 1'] and jogo['jogador 4'] > jogo['jogador 2'] and jogo['jogador 4'] > jogo['jogador 3']:
        vit_jog_4 += 1

# neste bloco apuramos o ranking de cada rodada
    ranking = sorted(jogo.items(),key = operator.itemgetter(1), reverse= True)
    for k, v in ranking:
        print(f'{k} :  {v} pontos.')
        time.sleep(1)
     
  print()    
  print('-'*30)
  print(f'      ***GRANDE CAMPEÃO ***')
  print('-'*30)
  print()
# neste bloco apuramos o grande campeão com o maior número de vitórias
  if vit_jog_1 > vit_jog_2 and vit_jog_1 > vit_jog_3 and vit_jog_1 > vit_jog_4: # Apura de o vencedor foi o jogador 1
      print(f' O Grande vencedor foi\n o Jogador 1 com {vit_jog_1} vitoria(s)')
  elif vit_jog_2 > vit_jog_1 and vit_jog_2 > vit_jog_3 and vit_jog_2 > vit_jog_4: # Apura se o vencedor foi o jogador 2
      print(f' O Grande vencedor foi\n o Jogador 2 com {vit_jog_2} vitoria(s)')
  elif vit_jog_3 > vit_jog_1 and vit_jog_3 > vit_jog_2 and vit_jog_3 > vit_jog_4: # Apura se o vencedor foi o jogador 3
      print(f' O Grande vencedor foi\n o Jogador 3 com {vit_jog_3} vitoria(s)')
  elif vit_jog_4 > vit_jog_1 and vit_jog_4 > vit_jog_3 and vit_jog_4 > vit_jog_2:# Apura se o vencedor foi o jogador 4
      print(f' O Grande vencedor foi\n o Jogador 4 com {vit_jog_4} vitoria(s)')
  else: 
      print('O Jogo terminou empatado!')
      print()
  time.sleep(1)

  # apurando o rankink final e inserindo em um dicionario
  vencedor ={'jogador 1' : vit_jog_1,
             'jogador 2' : vit_jog_2,
             'jogador 3' : vit_jog_3,
             'jogador 4' : vit_jog_4}
  print    
  print('-'*30)
  print(f'      ***RANKING FINAL ***')
  print('-'*30)
   # Ordenando e apurando o ranking final
  ranking_final = sorted(vencedor.items(),key = operator.itemgetter(1), reverse= True)
  for k, v in ranking_final:
      print(f'{k} :  {v} vitória(s).')
      time.sleep(1)
  
  
  break
  
