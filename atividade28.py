from random import choice

num = [1,2,3,4,5]

Usuar = int(input('Qual será o número? '))
s = choice(num)

if Usuar == num:
    print('Parabéns voce acertou!!')
    
else:
    print('Voce errou! o número era '.format(num))