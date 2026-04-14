print("======================================")
print("   SISTEMA DE NOTA IFB - DECISÃO      ")
print("======================================")

nome = input("Digite o nome do aluno: ")
materia = input("Digite a matéria: ")
total_aulas = 30 

nota1 = float(input(f"Digite a nota 1 de {materia}: "))
nota2 = float(input(f"Digite a nota 2 de {materia}: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota1 + nota2) / 2
percentual_faltas = (faltas / total_aulas) * 100
limite_faltas = total_aulas * 0.25 

if faltas > limite_faltas:
    situacao = "Reprovado por faltas"
elif media >= 7.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado por nota"

print("\n======================================")
print(f"ALUNO: {nome}")
print(f"MATÉRIA: {materia}")
print(f"MÉDIA: {media:.1f}")
print(f"FALTAS: {faltas} ({percentual_faltas:.1f}% das aulas)")
print("--------------------------------------")
print(f"SITUAÇÃO FINAL: {situacao}")
print("======================================")