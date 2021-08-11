'''Este Projeto tem por objetivo identificar o possível assasino em um processo de investigação criminosa.
Para que seja possível a identificação o usuário terá que responder a 5 perguntas. '''


print('Projeto detetive. Responda todas as perguntas abaixo:')
print(' ')
telefone = str(input('Você Telefonou para a Vitima?')).strip().upper()
local = str(input('Você esteve no local do crime?')).strip().upper()
vive = str(input('Você mora perto da Vitima?')).strip().upper()
devia = str(input('Você devia para a Vitima?')).strip().upper()
trabalhou = str(input('Você ja trabalhou com a Vitima?')).strip().upper()

if telefone == "SIM" or "S":
  resp_s = 1
else:
  resp_n = 1
if local ==  "S":
  resp_s = resp_s + 1
else:
  resp_n = resp_n + 1
if vive == "S":
  resp_s = resp_s + 1
else:
  resp_n = resp_n + 1
if devia == "S":
  resp_s = resp_s + 1
else:
   resp_n = resp_n + 1
if trabalhou == "S":
  resp_s = resp_s + 1
else:
  resp_n = resp_n + 1
if resp_s == 2:
  print ('Você está sendo investigada como suspeita do crime.')
elif resp_s == 3 or resp_s == 4:
  print ('Você está sendo investigada como cúmplice do crime.')
elif resp_s == 5:
  print ('Você é o(a) provável Assassino(a).')
else:
  print('Você é inocente.')