'''from prettytable import PrettyTable
import json
import csv

data = {
    "name": "João",
    "age": 30

}
with open('data.json','w') as jsonfile:
    json.dump(data, jsonfile)

with open('data.json','r') as jsonfile:
    data = json.load(jsonfile)
    print(data)

table = PrettyTable()
table.add_column("Nome",["João","Maria","Pedro"])
table.add_column("Idade",[30, 25, 40])
table.align["Nome"]= "l"
table.align["Idade"]= "r"
print(table)  '''

'''
valor1 = "{:<8}".format("123")
print(valor1)

valor2 = "{:0>5.2f}".format(7.89)
print(valor2)

valor3 = "{:^5}".format("CDE")
print(valor3)

valor4 = "{:6.2f}".format(12.456)
print(valor4)'''
'''import sys
from datetime import datetime

nome = "Jailson"
idade = 25
data_nascimento = datetime(1998, 5, 12)

separador = " | "

finalizador = " - "

print("Nome:", nome, sep=separador, end=finalizador)
print("Idade:", idade, sep=separador, end=finalizador)
print("Data de Nascimento:", data_nascimento.strftime("%d/%m/%Y"),file=sys.stderr, flush=True)


print ("O seu nome é: ",nome)
'''
'''
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
numero = float(input("Digite um número: "))
print(f"Olá, {nome}! Você tem {idade} anos e o número que você digitou foi {numero:.2f}")'''
