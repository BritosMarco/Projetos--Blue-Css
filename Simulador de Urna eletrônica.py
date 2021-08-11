#Projeto 04 - Simulador de votação:
#Crie um programa que simule um sistema de votação, ele deve receber votos até
#que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
#duas funções:
    #A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
    #ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
    #valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
    #OBRIGATÓRIO nas eleições.
    #A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
    #da função autoriza_voto()) e o voto que é o número que a pessoa votou.
#Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
#contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
#escolher de 1 a 5 (crie 3 candidatos para a votação):
#1, 2 ou 3 - Votos para os respectivos candidatos
#4- Voto Nulo 5 - Voto em Branco
#Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato; O total de votos nulos;
# O total de votos em branco;
#Qual candidato venceu a votacao


import operator
# declaração de listas, dicionários e variáveis
print('-'*60)
print('                      ***Eleições 2022***')
print('-'*60)
voto1 = voto2 = voto3 = voto4 = voto5 = 0   
vencedor = dict()
ranking_final = list()

def autoriza_voto(ano): # esta função apura a condição do eleitor de acordo com sua idade,
        from datetime import date
        atual = date.today().year # pega o ano atual
        idade = atual - ano

        if 18 <= idade < 70:
            return 'OBRIGATÓRIO'
            
        elif 70  <= idade or  16 <= idade <= 18:
            return 'FACULTATIVO'

        else:
            return  'NEGADO' 
def votacao(ano_nasc): # esta função valida o eleitor de acordo com a idade e recebe o voto
    validacao = autoriza_voto(ano_nasc)
    if validacao == 'NEGADO':
        print('            Você não pode votar')
        print()
    else:
        print(f'''
            |============================|
            |1- | Drummond               |            
            |2- | Castro Alves           |             
            !3- | Machado de Assis       |
            |4- | Voto Branco            |
            |5- | Voto Nulo              |
            |============================|
            ''')
        return int(input('            Digite seu voto:'))

def vencedor(voto1,voto2,voto3,voto4,voto5): #esta função apura os votos ranqueia os candidatos e apura o vencedor
    
    vencedor ={ '1-Drummont ' : voto1,
                '2-Castro Alves ' : voto2,
                '3-Machado de Assis ' : voto3,
                '4-Voto Branco ' : voto4,
                '5-Voto Nulo ' : voto5
                }
    print()   
    print('-'*30)
    print(f'      ***RANKING FINAL ***')
    print('-'*30)
    ranking_final = sorted(vencedor.items(),key = operator.itemgetter(1), reverse= True) # ordena o ranking em ordem decrescente
    for k, v in ranking_final:
        print(f'{k} :  {v} voto(s).')

    print()    
    print('-'*30)
    print(f'      ***GRANDE VENCEDOR ***')
    print('-'*30)

    print()
    # neste bloco apuramos o grande vencedor com o maior número de VOTOS
    if voto1 > voto2 and voto1 > voto3:
        print(f' O Grande vencedor foi: \n o Canditado Drummont com {voto1} voto(s)')
    elif voto2 > voto1 and voto2 > voto3:
        print(f' O Grande vencedor foi\n o Candidato Casto Alves com {voto2} voto(s)')
    elif voto3 > voto1 and voto3 > voto2:
        print(f' O Grande vencedor foi\n o Canditado Machado de Assis com {voto3} voto(s)')
    else: 
        print('A eleição terminou empatada!')
        print()

def funcao_principal():
    voto1 = voto2 = voto3 = voto4 = voto5 = 0   

    while True:
        ano_nasc = int(input('            Digite seu Ano de Nascimento: '))
        voto = votacao(ano_nasc) 
        # condicional para atribuição dos votos
        if voto == 1:
            voto1 += 1
        elif voto == 2:
            voto2 += 1
        elif voto == 3:
            voto3 += 1
        elif voto == 4:
            voto4 += 1
        elif voto == 5:
            voto5 += 1
        else:
            valid = autoriza_voto(ano_nasc)
            if valid != 'NEGADO':
                print('            *Voto Inválido*')
            else:
                print()

        continuar = input('            Deseja Continuar [S/N]: ').strip().upper()
        if continuar == 'N':
            break
    vencedor(voto1,voto2,voto3,voto4,voto5) # chama a funcão vencedor com a contagem dos votos a puração do vencedor

if __name__== "__main__": # informa que esta é a função prinicpal do projeto
    funcao_principal()
