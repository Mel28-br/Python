distancia = int(input("Informe a distancia(Km): "))

if distancia <= 200:
    pas = distancia * 0.50
else:
    pas = distancia * 0.45

print(f"Preço da passagem é de R$ {pas}")