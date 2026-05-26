DISCIPLINAS = ["informatica", "matematica", "fisica"]


def menu():
    menu = """======================================
Seja bem vindo ao sistema de nota IFB
======================================
1. Cadastrar aluno
2. Gerar relatório final
3. Adicionar notas
0. Sair

Digite sua opção: """
    return input(menu)


# ETAPA 5 - Cadastro de dados
def cadastrar_aluno(alunos):
    nome = input("\nDigite o nome do aluno: ")

    if buscar_aluno(alunos, nome):
        print(f"\nO aluno {nome} já está cadastrado.\n")
        return

    escolaridade = input("Digite a escolaridade do aluno: ")
    faltas = int(input("Digite o número de faltas: "))

    aluno = {
        "nome": nome,
        "escolaridade": escolaridade,
        "total_aulas": 30,
        "faltas": faltas,
        "situacao": None,
        "notas": {}
    }

    for disciplina in DISCIPLINAS:
        aluno["notas"][disciplina] = {
            "n1": None,
            "n2": None,
            "media": None,
            "situacao": None
        }

    alunos.append(aluno)
    print(f"\nAluno {nome} cadastrado com sucesso!\n")


def buscar_aluno(alunos, nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


# ETAPA 5 - Cálculo de nota
def calcular_nota(n1, n2):
    return (n1 + n2) / 2


# ETAPA 5 - Cálculo de frequência
def calcular_frequencia(aluno):
    limite = aluno["total_aulas"] * 0.25

    if aluno["faltas"] > limite:
        return "Reprovado por faltas"

    return "Frequência OK"


def adicionar_notas(aluno):

    if calcular_frequencia(aluno) == "Reprovado por faltas":
        aluno["situacao"] = "Reprovado por faltas"
        print("\nAluno reprovado por faltas.\n")
        return

    print("\nEscolha a disciplina:")

    for i, disciplina in enumerate(DISCIPLINAS, 1):
        print(f"{i}. {disciplina.capitalize()}")

    opcao = int(input("Digite sua opção: "))

    if opcao < 1 or opcao > 3:
        print("\nOpção inválida.\n")
        return

    disciplina = DISCIPLINAS[opcao - 1]

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
        print("\nNota inválida.\n")
        return

    media = calcular_nota(n1, n2)

    aluno["notas"][disciplina]["n1"] = n1
    aluno["notas"][disciplina]["n2"] = n2
    aluno["notas"][disciplina]["media"] = media

    if media >= 7:
        aluno["notas"][disciplina]["situacao"] = "Aprovado"
    else:
        aluno["notas"][disciplina]["situacao"] = "Reprovado por nota"

    print(f"\nMédia em {disciplina}: {media}\n")


# ETAPA 5 - Relatório final
def gerar_relatorio(alunos):

    if not alunos:
        print("\n>>> Não possui alunos cadastrados <<<\n")
        return

    print("\n=========== RELATÓRIO FINAL ===========")

    for aluno in alunos:

        print(f"\nNome: {aluno['nome']}")
        print(f"Escolaridade: {aluno['escolaridade']}")
        print(f"Faltas: {aluno['faltas']}")

        frequencia = calcular_frequencia(aluno)
        print(f"Frequência: {frequencia}")

        for disciplina in DISCIPLINAS:
            dados = aluno["notas"][disciplina]

            if dados["media"] is not None:
                print(
                    f"{disciplina.capitalize()} -> "
                    f"N1: {dados['n1']} | "
                    f"N2: {dados['n2']} | "
                    f"Média: {dados['media']} | "
                    f"Situação: {dados['situacao']}"
                )

        print("----------------------------------")


def main():

    alunos = []

    while True:

        opcao = menu()

        if opcao == "1":
            cadastrar_aluno(alunos)

        elif opcao == "2":
            gerar_relatorio(alunos)

        elif opcao == "3":

            if not alunos:
                print("\n>>> Não possui alunos cadastrados <<<\n")
                continue

            nome = input("\nDigite o nome do aluno: ")

            aluno = buscar_aluno(alunos, nome)

            if aluno:
                adicionar_notas(aluno)
            else:
                print("\nAluno não encontrado.\n")

        elif opcao == "0":
            print("\nSaindo...\n")
            break

        else:
            print("\nOpção inválida.\n")


main()