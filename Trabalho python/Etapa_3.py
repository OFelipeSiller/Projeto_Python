print("======================================")
print("   SISTEMA DE NOTA IFB - REPETIÇÃO    ")
print("======================================")

while True:
    nome = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    total_aulas = 30
    limite_faltas = total_aulas * 0.25

    quantidade_materias = int(input(f"Quantas disciplinas deseja cadastrar para {nome}? "))

    for i in range(quantidade_materias):
        print(f"\n--- {i+1}ª Disciplina ---")
        materia = input("Nome da disciplina: ")
        
        nota1 = float(input(f"Digite a nota 1 de {materia}: "))
        nota2 = float(input(f"Digite a nota 2 de {materia}: "))
        faltas = int(input(f"Total de faltas em {materia}: "))

        media = (nota1 + nota2) / 2
        
        if faltas > limite_faltas:
            situacao = "Reprovado por faltas"
        elif media >= 7.0:
            situacao = "Aprovado"
        elif media >= 4.0:
            situacao = "Em Recuperação"
        else:
            situacao = "Reprovado por nota"

        print(f"Média: {media:.1f} | Faltas: {faltas} | Situação: {situacao}")

    print(f"\nCadastro de disciplinas para {nome} concluído.")
    print("-" * 40)

print("\nSistema encerrado.")