DISCIPLINAS = ["informatica", "matematica", "fisica"]


def menu():
    menu = """======================================
Seja bem vindo ao sistema de nota IFB
======================================
1. Cadastrar aluno
2. Listar alunos (Relatório)
3. Adicionar notas
0. Sair

Digite sua opção: """
    return input(menu)


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def filtro_aluno(alunos, nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def verificar_faltas(aluno):
    limite = aluno["total_aulas"] * 0.25
    return aluno["faltas"] > limite


def criar_notas():
    notas = {}

    for disciplina in DISCIPLINAS:
        notas[disciplina] = {
            "n1": None,
            "n2": None,
            "media": None,
            "situacao": None
        }

    return notas


def cadastrar_aluno(alunos):
    nome = input("\nDigite o nome do aluno: ")

    if filtro_aluno(alunos, nome):
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
        "notas": criar_notas()
    }

    if verificar_faltas(aluno):
        aluno["situacao"] = "Reprovado por faltas"

    alunos.append(aluno)

    print(f"\nAluno {nome} cadastrado com sucesso!\n")


def processar_aluno(aluno):

    if verificar_faltas(aluno):
        aluno["situacao"] = "Reprovado por faltas"
        return

    aprovado = True

    for disciplina in DISCIPLINAS:
        media = aluno["notas"][disciplina]["media"]

        if media is not None and media < 7:
            aprovado = False

    if aprovado:
        aluno["situacao"] = "Aprovado"
    else:
        aluno["situacao"] = "Reprovado por nota"


def adicionar_notas(aluno):

    if verificar_faltas(aluno):
        print("\nAluno reprovado por faltas. Não é possível adicionar notas.\n")
        aluno["situacao"] = "Reprovado por faltas"
        return

    print("\nDeseja inserir notas de qual matéria?\n")

    for i, disciplina in enumerate(DISCIPLINAS, 1):
        print(f"{i}. {disciplina.capitalize()}")

    opcao = input("\nDigite sua opção: ")

    if opcao not in ["1", "2", "3"]:
        print("\nOpção inválida.\n")
        return

    disciplina = DISCIPLINAS[int(opcao) - 1]

    n1 = float(input("\nDigite a primeira nota: "))
    if n1 < 0 or n1 > 10:
        print("\nNota inválida. Digite entre 0 e 10.\n")
        return

    n2 = float(input("Digite a segunda nota: "))
    if n2 < 0 or n2 > 10:
        print("\nNota inválida. Digite entre 0 e 10.\n")
        return

    media = calcular_media(n1, n2)

    aluno["notas"][disciplina]["n1"] = n1
    aluno["notas"][disciplina]["n2"] = n2
    aluno["notas"][disciplina]["media"] = media

    if media < 7:
        situacao = "Reprovado por nota"
    else:
        situacao = "Aprovado"

    aluno["notas"][disciplina]["situacao"] = situacao

    print(f"\nMédia de {disciplina}: {media}")
    print(f"Situação: {situacao}\n")

    processar_aluno(aluno)


def listar_alunos(alunos):

    if not alunos:
        print("\n>>> Não possui alunos cadastrados <<<\n")
        return

    print("\n========= RELATÓRIO =========")

    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Escolaridade: {aluno['escolaridade']}")
        print(f"Faltas: {aluno['faltas']}")

        for disciplina in DISCIPLINAS:
            dados = aluno["notas"][disciplina]

            if dados["media"] is not None:
                print(
                    f"{disciplina.capitalize()} - "
                    f"N1: {dados['n1']}, "
                    f"N2: {dados['n2']}, "
                    f"Média: {dados['media']}, "
                    f"Situação: {dados['situacao']}"
                )

        print(f"Situação Final: {aluno['situacao']}")
        print("---------------------------------")


def main():

    alunos = []

    while True:
        opcao = menu()
        print("\n====================================\n")

        if opcao == "1":
            cadastrar_aluno(alunos)

        elif opcao == "2":
            listar_alunos(alunos)

        elif opcao == "3":

            if not alunos:
                print("\n>>> Não possui alunos cadastrados <<<\n")
                continue

            nome = input("Digite o nome do aluno: ")

            aluno = filtro_aluno(alunos, nome)

            if aluno:
                adicionar_notas(aluno)
            else:
                print("\nAluno não encontrado.\n")

        elif opcao == "0":
            print("\nSaindo...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


main()