"""
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000
"""

num1 = int(input("Escolha um número: "))

if(num1 < 1000):
    print("Seu número está abaixo de 1000")

if(num1 >= 1000 and num1 <= 5000 ):
    print("Seu está entre 1000 e 5000.")

if(num1 > 5000 ):
    print("Seu número está acima de 5000.")