"""
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
"""

n1 = int(input("Informe o ano do seu nascimento: "))
n2 = int(input("Informe o ano atual:"))

n3 = n2 - n1

print(f"Sua idade é de {n3}")

if(n1 > n2):
    print("Um dos números inseridos esta invalido")