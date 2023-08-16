"""
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
"""

n1 = int(input("Escolha seu primeiro número: "))
n2 = int(input("Escolha seu segundo número: "))

if(n1 > n2):
    print(f"O seu primeiro número {n1}, é maior que o seu segundo número {n2}.")

if(n1 == n2):
    print(f"Os seus dois números são iguais.")

if(n1 < n2):
    print(f"O seu segundo número {n2}, é maior que o seu primeiro número {n1}.")