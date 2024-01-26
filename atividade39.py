from datetime import date

datan = int(input("Data de nascimento: "))

anot = date.today().year
ano_alis = datan - anot

print('Voce tem {} SOLDADO!'.format(ano_alis))

if ano_alis < 18:
    print("Voce esta no tempo adquador")
    