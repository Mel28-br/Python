progra = float(input("Qual é o seu salario? "))

if progra > 1250.00:
    print(f"salario inicial {progra:.2f}\n - Com reajuster de 10% é R$ {progra * 1.10:.2f}")
else :
    print(f"salario inicial {progra:.2f}\n - Com reajuster de 15% é R$ {progra * 1.15:.2f}")