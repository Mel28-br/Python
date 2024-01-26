casa = float(input("Valor da casa: "))
saldo = float(input("Digite o salário: "))
ano = int(input("Quantos anos para pagar: "))

if (casa / (ano * 12) > (saldo * 0.30)):
    print("Infelizmente não foi disponível")
else:
    print(f"Valor da prestação a pagar R$ in  Emprétismo OK!!")