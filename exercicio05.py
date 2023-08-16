"""
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
"""

sig = input("Escolha uma sigla de um estado brasileiro ( Com as letras em maiuscula ): ")
sig1 = "ES"
sig2 = "MG"
sig3 = "RJ"
sig4 = "SP"

if(sig == sig1):
    print("Seu estado é do Sudeste.")

if(sig == sig2):
    print("Seu estado é do Sudeste.")

if(sig == sig3):
    print("Seu estado é do Sudeste.")

if(sig == sig4):
    print("Seu estado é do Sudeste.")

else:
    print("Seu estado não é do Sudeste.")