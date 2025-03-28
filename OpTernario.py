# valor_produto = 100
# desconto = 0.1 if valor_produto >= 50 else 0
# valor_final = valor_produto * (1 - desconto)
# print(f"Valor final da compra: R${valor_final:.2f}")


# status_pedido = "pendente"
#
# mensagem_pedido = "Seu pedido está em análise." if status_pedido == "pendente"\
#     else "Seu pedido foi aprovado." if status_pedido =="enviado"\
#     else "seu pedido foi entregue!"
# print(f"mensagem do pedido {mensagem_pedido}")

# numero1=input("Digite um número: ")
# numero2=input("Digite outro número: ")
# operacao = input("Digite a operação: "+","-","*","/"")
# operacao = "+"
# resultado = (numero1 + numero2) if operacao == "+" \
#     else (numero1 - numero2) if operacao == "-" \
#     else (numero1 * numero2) if operacao == "*" \
#     else (numero1 / numero2) if operacao == "/" \
#     else "Operação inválida"
# print(f"Resultado da operação: {resultado}")

# valor_digitado = input("Digite um número: ")
# try:
#     numero = int(valor_digitado)
#     mensagem = "Número válido." if numero > 0 \
# else "Número inválido: deve ser positivo."
# except ValueError:
#     mensagem = "Número inválido: digite um numero."
# print(mensagem)
#

tipo_fruta  = "maçã"

match tipo_fruta:
    case "laranja","limão":
        print("Fruta cítrica")

    case "maçã","pera":
        print("Fruta de caroço")

    case "banana","kiwi":
        print("Fruta tropical")

    case _:
        print("tipo de fruta não encontrado")