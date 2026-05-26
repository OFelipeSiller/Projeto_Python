def menu():
    menu = """======================================
Seja bem vindo ao sistema de nota IFB
======================================
1. Cadastrar aluno
2. Listar Alunos (Relatório)
3. Adicionar Notas
0. Sair.

Digite sua opção: """
    return input(menu)


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def filtro_faltas(aluno):
    if aluno["faltas"] > aluno["total_aulas"] * 0.25:
        return "Reprovado por faltas"
    return None


def filtro_alunos(alunos, nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def validar_nota(msg):
    while True:
        try:
            nota = float(input(msg))
            if 0 <= nota <= 10:
                return nota
            print("Nota inválida. Digite entre 0 e 10.")
        except ValueError:
            print("Digite apenas números.")


def cadastrar_aluno(alunos):
    nome = input("\nDigite o nome do aluno: ")

    if filtro_alunos(alunos, nome):
        print(f"\nO aluno {nome} já está cadastrado.\n")
        return

    escolaridade = input("Digite o nível da educação do aluno: ")

    while True:
        try:
            faltas = int(input("Digite o número de faltas: "))
            if faltas >= 0:
                break
            print("Digite um número válido.")
        except ValueError:
            print("Digite apenas números.")

    # quantidade de disciplinas
    while True:
        try:
            qtd = int(input("Quantas disciplinas deseja cadastrar? "))
            if qtd > 0:
                break
            print("Digite no mínimo 1.")
        except ValueError:
            print("Digite apenas números.")

    notas = {}

    # uso do FOR
    for i in range(qtd):
        nome_disciplina = input(f"Digite o nome da disciplina {i+1}: ").lower()

        notas[nome_disciplina] = {
            "n1": None,
            "n2": None,
            "media": None,
            "situacao": None
        }

    aluno_cadastrado = {
        "nome": nome,
        "escolaridade": escolaridade,
        "total_aulas": 30,
        "faltas": faltas,
        "situacao": filtro_faltas({
            "faltas": faltas,
            "total_aulas": 30
        }),
        "notas": notas
    }

    alunos.append(aluno_cadastrado)

    print(f"\nAluno {nome} cadastrado com sucesso!\n")


def calcular_notas(aluno):

    if filtro_faltas(aluno):
        print("\nAluno reprovado por faltas. Não é possível adicionar notas.\n")
        aluno["situacao"] = "Reprovado por faltas"
        return

    print("\nDisciplinas disponíveis:")

    disciplinas = list(aluno["notas"].keys())

    # uso do FOR
    for i, disciplina in enumerate(disciplinas, 1):
        print(f"{i}. {disciplina.title()}")

    opcao = input("Escolha a disciplina: ")

    if not opcao.isdigit():
        print("Opção inválida.")
        return

    opcao = int(opcao)

    if opcao < 1 or opcao > len(disciplinas):
        print("Opção inválida.")
        return

    materia = disciplinas[opcao - 1]

    n1 = validar_nota(f"Digite a primeira nota de {materia}: ")
    n2 = validar_nota(f"Digite a segunda nota de {materia}: ")

    media = calcular_media(n1, n2)

    aluno["notas"][materia]["n1"] = n1
    aluno["notas"][materia]["n2"] = n2
    aluno["notas"][materia]["media"] = media

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado por nota"

    aluno["notas"][materia]["situacao"] = situacao

    print(f"\nMédia de {materia}: {media}")
    print(f"Situação: {situacao}\n")


def listar_alunos(alunos):
    if not alunos:
        print("\n>>> Não possui alunos cadastrados <<<\n")
        return

    print("\n===== ALUNOS CADASTRADOS =====")

    # uso do FOR
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Escolaridade: {aluno['escolaridade']}")
        print(f"Faltas: {aluno['faltas']}")

        if aluno["situacao"]:
            print(f"Situação: {aluno['situacao']}")

        for materia, dados in aluno["notas"].items():
            if dados["media"] is not None:
                print(
                    f"{materia.title()} - "
                    f"N1: {dados['n1']} | "
                    f"N2: {dados['n2']} | "
                    f"Média: {dados['media']} | "
                    f"Situação: {dados['situacao']}"
                )


def main():

    alunos = []

    # uso do WHILE
    while True:
        opcao = menu()

        if opcao == "1":
            cadastrar_aluno(alunos)

        elif opcao == "2":
            listar_alunos(alunos)

        elif opcao == "3":
            if not alunos:
                print("\n>>> Não possui alunos cadastrados <<<\n")
                continue

            nome = input("Digite o nome do aluno: ")

            aluno = filtro_alunos(alunos, nome)

            if aluno:
                calcular_notas(aluno)
            else:
                print("\nAluno não encontrado.\n")

        elif opcao == "0":
            print("\nSaindo...\n")
            break

        else:
            print("\nOpção inválida.\n")


main()
