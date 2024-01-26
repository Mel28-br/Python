v_carro = int(input("Informer a velocidade do carro: "))

if v_carro > 80:
    multa = (v_carro - 80)*7
    print(f"Voce foi multado em R$ {multa:.2f}!")
if v_carro <= 80 :
    print(f"Sua velocidade esta no limite correto, boa viagem!")