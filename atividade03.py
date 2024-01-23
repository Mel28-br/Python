from random import choice

nome1 = input("Digite um nome: ")
nome2  = input("Digite um nome: ")
nome3  = input("Digite um nome: ")
nome4  = input("Digite um nome: ")
alunos = [nome1, nome2, nome3, nome4]

print(f"O sorteado do dia é {choice(alunos)}")