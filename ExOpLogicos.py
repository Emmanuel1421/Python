produto = "Robux"
valor = 90
cliente_vip = True

if (produto == "Robux" or produto == "rp") and valor < 100 and cliente_vip:
    desconto = 0.2
    valor_final = valor * (1 - desconto)
    print(f"O valor final da compra é de R${valor_final:.2f}")
else:
    print("não ha desconto disponivel")