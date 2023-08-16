"""
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo
"""

nota1 = float(input("Informe sua nota 1:"))
nota2 = float(input("Informe sua nota 2:"))


media = (nota1 + nota2) /2

if ( media <= 3 ):
    print(f"REPROVADO - Média: {media}")

if( media >= 3 and media <= 6.9):
    print(f"PROVA FINAL - Média: {media}")

if( media >= 7):
    print(f"APROVADO - Média: {media}")