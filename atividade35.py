med = float(input("Digite a primeira medida: "))
med2 = float(input("Digite a segunda medida: "))
med3 = float(input("Digite a terceira medida: "))

if (med < med2 + med3) and (med2 < med + med3) and (med3 < med + med2):
    print("È um triangulo")
else:
    print("Não é um triangulo")