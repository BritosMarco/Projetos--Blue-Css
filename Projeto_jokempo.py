'''Jogo de jokenpo'''
from random import randint
#Declaração de variaveis
rodadas = 0
pedra = '[1] Pedra'
papel = '[2] Papel'
tesoura = '[3] Tesoura'
vitorias_jog = 0
vitorias_comp = 0
empate = 0
n = 1
jogador = []

rodadas = int(input('Digite quantas rodadas ou [0] para sair: '))
print(f' {pedra}\n {papel}\n {tesoura}')

# Escolha da opção
for i in range(rodadas):
  print('')
  jogador = int(input(' Digite sua opção: '))
  computador = randint(1,3)
  print('')
   # verifca empate
  if jogador == computador:
    empate += 1
    if jogador == 1:
      print(f' Você e o computador escolheram: {pedra} Rodada {n} - Empate')
      n += 1
    elif jogador == 2:
      print(f' Você e o computador escolheram: {papel} Rodada {n} - Empate')
      n += 1
    elif jogador == 3:
      print(f' Você e o computador escolheram: {tesoura} Rodada {n} - Empate')
      n += 1

    #jogador escolhe opção 1 pedra
  elif jogador == 1 and computador == 2:
      print(f' Você escolheu {pedra}\n O Computador escolheu {papel}\n Resultado da rodada {n} - O computador venceu')
      n += 1
      vitorias_comp +=1
  elif jogador == 1 and computador == 3:
      print(f' Você escolheu {pedra}\n O Computador escolheu {tesoura}\n Resultado da rodada {n} - Você venceu')
      n += 1
      vitorias_jog +=1
  # Jogador Escolhe opção 2 papel
  elif jogador == 2 and computador == 1:
      print(f' Você escolheu {papel}\n O Computador escolheu {pedra}\n Resultado da rodada {n} - Você venceu')
      n += 1
      vitorias_jog +=1
  elif jogador == 2 and computador == 3:
      print(f' Você escolheu {papel}\n O Computador escolheu {tesoura}\n - Resultado da rodada {n} - O computador venceu')
      n += 1
      vitorias_comp +=1

     # Jogador Escolhe opção 3 tesoura
  elif jogador == 3 and computador == 1:
      print(f' Você escolheu {tesoura}\n O Computador escolheu {pedra}\n - Resultado da rodada {n} - O computador venceu')
      n += 1
      vitorias_comp +=1
  elif jogador == 3 and computador == 2:
      print(f' Você escolheu {tesoura}\n O Computador escolheu {papel}\n - Resultado da rodada {n} - Você venceu')
      n += 1
      vitorias_jog +=1
      #Calculando o grande vencedor
print('')
print('-----------------------------')
print('    ***Apuração Final***')
print('-----------------------------')
print(f' Vitoria(s) do computador: {vitorias_comp}\n Sua(s) Vitória(s): {vitorias_jog}')
if vitorias_jog > vitorias_comp:
  print(f' Você foi o grande vencedor')
elif vitorias_jog < vitorias_comp:
  print(' O computador venceu...Game Over ')
else:
  print(' Resultado: Empate')

print('')
opcao = ''
opcao = str(input('Jogar novamente [S/N]: ')).strip().upper()
if opcao == 'S':
    rodadas = int(input('Digite quantas rodadas ou [0] para sair: '))