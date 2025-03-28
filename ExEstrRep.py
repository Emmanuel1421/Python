#for
#
# #for i in range(5):
#     print(i)
#
# #for com lista
# nomes = ['João', 'Maria', 'Pedro', 'José', 'Ana']
# for nome in nomes:
#     print(f'Olá, {nome} !')

# #for com enumarate
# nomes = ['João', 'Maria', 'Pedro', 'José', 'Ana']
# for i, nome in enumarate(nomes):
#     print(f'{i}: Olá, {nome}!')

# #criando uma lista a partir de uma função for
# quadrados = [x**2 for x in range(10)]
# print (quadrados)

#Função zip

#while

contador = 0
while contador < 5:
    print(contador)
    contador += 1

resposta = ""
while resposta.lower() != "sair":
    resposta = input("Digite 'sair' para encerrar o programa: ")


for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

