"""
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
"""

n1 = int(input("Escolha um número de 1 a 7: "))

dom = 1
seg = 2
ter = 3
quar = 4
quin = 5
sex = 6
sab = 7

if( n1 == 1):
    print(f"o número {n1} representa domingo.")

if( n1 == 2 ):
    print(f"o número {n1} representa segunda-feira.")

if( n1 == 3 ):
    print(f"o número {n1} representa terça-feira")

if( n1 == 4 ):
    print(f"o número {n1} representa quarta-feira")

if( n1 == 5 ):
    print(f"o número {n1} representa quinta-feira")

if( n1 == 6 ):
    print(f"o número {n1} representa sexta-feira")

if( n1 == 7 ):
    print(f"o número {n1} representa sábado")

else:
    print("O número inserido não é valido")