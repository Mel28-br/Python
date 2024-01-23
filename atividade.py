from math import sin , cosh , atan , radians

angulo = float(input("Digite um angulo: "))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cosh(radiano)
tangentes = atan(radiano)


print(f"Sua seno é {seno:.2f}, cosseno {cosseno:.2f} e tangentes {tangentes:.2f}")

