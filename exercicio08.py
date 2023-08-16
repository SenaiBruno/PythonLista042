"""
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final
"""

n1 = int(input("Escolha um número: "))
n2 = int(input("Escolha um outro número: "))
n3 = int(input("Escolha um ultimo número: "))

if( n1 > n2 and n1 > n3 ):
    print(f"O seu primeiro número: {n1} é maior que os outros 2.")

if( n2 > n1 and n2 > n3 ):
    print(f"O seu segundo número: {n2} é maior que os outros 2.")

if( n3 > n1 and n3 > n2 ):
    print(f"O seu primeiro número: {n3} é maior que os outros 2.")