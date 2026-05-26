def menu():
    menu = """======================================
Seja bem vindo ao sistema de nota IFB
======================================
1. Cadastrar aluno
2. Listar Alunos (Relatório)
3. Adicionar Notas
0. Sair.
\nDigite sua opção: """
    return (input(menu))   

def cadastrar_aluno(alunos):
    nome = input("\nDigite o nome do aluno: ")

    aluno_existe = filtro_alunos(alunos, nome)
    if aluno_existe == nome:
        print(f"\nO aluno {nome} já está cadastrado.\n")
        return 

    escolaridade = input("Digite a nível da educação do aluno: ")
    faltas = int(input("Digite o número de faltas: "))

    aluno_cadastrado = {
        "nome": nome,
        "escolaridade": escolaridade,
        "total_aulas": 30,
        "faltas": faltas,
        "situacao": None,
        "notas": {
            "informatica": {"n1": None, "n2": None, "media": None, "situacao": None},
            "matematica": {"n1": None, "n2": None, "media": None, "situacao": None},
            "fisica": {"n1": None, "n2": None, "media": None, "situacao": None}
        }
    }
    
    # Verificar se reprovado por faltas
    if filtro_faltas(aluno_cadastrado, faltas):
        aluno_cadastrado["situacao"] = "Reprovado por faltas"
    
    alunos.append(aluno_cadastrado)
    print(f"\nAluno {nome} cadastrado com sucesso!\n")

    return alunos

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media    

def filtro_faltas(alunos, faltas):
    if faltas > alunos['total_aulas'] * 0.25:
        return "Reprovado por faltas"

def filtro_alunos(alunos, nome):
    aluno_exitente = [aluno for aluno in alunos if aluno["nome"] == nome]
    return aluno_exitente[0]['nome'] if aluno_exitente else None

def calcular_notas(alunos):

    if filtro_faltas(alunos, alunos['faltas']):
        print("\nAluno reprovado por faltas. Não é possível adicionar notas.\n")
        alunos['situacao'] = "Reprovado por faltas"
        return  
    else:
        print("\nDeseja inserir as notas de qual matéria?")
        display = '''
1. Informática
2. Matemática
3. Física
'''
        print(display)
        opcao_materia = input("Digite sua opção: ")

        if opcao_materia == "1":
            n1_informatica = float(input("\nDigite a primeira nota de informática: "))
            if 0 > n1_informatica or 10 < n1_informatica:
                print("\nNota inválida. A nota deve ser entre 0 e 10.\n")
                return
            n2_informatica = float(input("Digite a segunda nota de informática: "))
            if 0 > n2_informatica or 10 < n2_informatica:
                print("\nNota inválida. A nota deve ser entre 0 e 10.\n")
                return

            media_informatica = calcular_media(n1_informatica, n2_informatica)

            alunos['notas']['informatica']['n1'] = n1_informatica
            alunos['notas']['informatica']['n2'] = n2_informatica
            alunos['notas']['informatica']['media'] = media_informatica

            if media_informatica < 7.0:
                situacao = "Reprovado por nota"
            else:
                situacao = "Aprovado"

            alunos['notas']['informatica']['situacao'] = situacao

            print(f"\nMédia de informática: {media_informatica}\n")
            print(f"Nota 1: {n1_informatica}\nNota 2: {n2_informatica}")
            print(f"Faltas: {alunos['faltas']}")
            print("===========================================")
            print(f"Situação: {situacao}\n")

        elif opcao_materia == "2":
            n1_matematica = float(input("\nDigite a primeira nota de matemática: "))
            if 0 > n1_matematica or 10 < n1_matematica:
                print("\nNota inválida. A nota deve ser entre 0 e 10.\n")
                return
            n2_matematica = float(input("Digite a segunda nota de matemática: "))
            if 0 > n2_matematica or 10 < n2_matematica:
                print("\nNota inválida. A nota deve ser entre 0 e 10.\n")
                return

            media_matematica = calcular_media(n1_matematica, n2_matematica)

            alunos['notas']['matematica']['n1'] = n1_matematica
            alunos['notas']['matematica']['n2'] = n2_matematica
            alunos['notas']['matematica']['media'] = media_matematica

            if media_matematica < 7.0:
                situacao = "Reprovado por nota"
            else:
                situacao = "Aprovado"

            alunos['notas']['matematica']['situacao'] = situacao

            print(f"\nMédia de matemática: {media_matematica}\n")
            print(f"Nota 1: {n1_matematica}\nNota 2: {n2_matematica}")
            print(f"Faltas: {alunos['faltas']}")
            print("===========================================")
            print(f"Situação: {situacao}\n")

        elif opcao_materia == "3":
                n1_fisica = float(input("\nDigite a primeira nota de física: "))
                if 0 > n1_fisica or 10 < n1_fisica:
                    print("\nNota inválida. A nota deve ser entre 0 e 10.\n")
                    return

                n2_fisica = float(input("Digite a segunda nota de física: "))
                if 0 > n2_fisica or 10 < n2_fisica:
                    print("\nNota inválida. A nota deve ser entre 0 e 10.\n")
                    return                

                media_fisica = calcular_media(n1_fisica, n2_fisica)

                alunos['notas']['fisica']['n1'] = n1_fisica
                alunos['notas']['fisica']['n2'] = n2_fisica
                alunos['notas']['fisica']['media'] = media_fisica

                if media_fisica < 7.0:
                    situacao = "Reprovado por nota"
                else:
                    situacao = "Aprovado"

                alunos['notas']['fisica']['situacao'] = situacao

                print(f"\nMédia de física: {media_fisica}\n")
                print(f"Nota 1: {n1_fisica}\nNota 2: {n2_fisica}")
                print(f"Faltas: {alunos['faltas']}")
                print("===========================================")
                print(f"Situação: {situacao}\n")

def listar_alunos(alunos):
    if not alunos:
        print("\n>>> Não possui alunos cadastrados <<<\n")
        return

    print("Alunos cadastrados:")
    for aluno in alunos:
        nome = aluno['nome']
        escolaridade = aluno['escolaridade']
        print(f"\nNome: {nome}\nEscolaridade: {escolaridade}")
        
        if aluno['faltas'] is not None:
            print(f"Faltas: {aluno['faltas']}")
        
        # Mostrar situação geral se existir
        if aluno.get('situacao'):
            print(f"Situação: {aluno['situacao']}")
            print()
            continue
        
        notas = aluno['notas']
        if notas['informatica']['media'] is not None:
            print(f"Informática - N1: {notas['informatica']['n1']}, N2: {notas['informatica']['n2']}, Média: {notas['informatica']['media']}, Situação: {notas['informatica']['situacao']}")
        if notas['matematica']['media'] is not None:
            print(f"Matemática - N1: {notas['matematica']['n1']}, N2: {notas['matematica']['n2']}, Média: {notas['matematica']['media']}, Situação: {notas['matematica']['situacao']}")
        if notas['fisica']['media'] is not None:
            print(f"Física - N1: {notas['fisica']['n1']}, N2: {notas['fisica']['n2']}, Média: {notas['fisica']['media']}, Situação: {notas['fisica']['situacao']}")
        print()

def main():
    
    alunos = []

    while True: 
        opcao = menu()
        print("\n===========================================\n")

        if opcao == "1":
            cadastrar_aluno(alunos)
        
        elif opcao == "2":
            listar_alunos(alunos)
        
        elif opcao == "3":
            if not alunos:
                print("\n>>> Não possui alunos cadastrados <<<\n")
                continue

            print("\nQual aluno deseja adicionar a nota?\n")
            listar_alunos(alunos)
            
            nome_aluno = input("Digite o nome do aluno: ")
            aluno_encontrado = None
            
            for aluno in alunos:
                if aluno['nome'] == nome_aluno:
                    aluno_encontrado = aluno
                    break
            if aluno_encontrado:
                calcular_notas(aluno_encontrado)
            else:
                print("\nAluno não encontrado. Tente novamente.\n")
                
        elif opcao == "0":
            print("\nSaindo...\n")
            break
        else:
            print("\nOpção inválida, tente novamente.\n")

main()