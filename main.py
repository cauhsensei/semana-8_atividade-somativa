import json


def salvar_dados_arquivo(dados, tipo_dado):
    with open(f"{tipo_dado.lower()}.json", "w") as arquivo:
        json.dump(dados, arquivo)


def recuperar_dados_arquivo(tipo_dado):
    try:
        with open(f"{tipo_dado.lower()}.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def incluir_dado(dados, tipo_dado, campos):
    while True:
        codigo = int(input(f"Digite o código do {tipo_dado}: "))
        if verificar_codigo_existente(dados, codigo):
            print(f"O código {codigo} já está em uso. Por favor, escolha outro código.")
        else:
            break

    novo_dado = {}
    for campo, tipo in campos.items():
        if campo == "Codigo":
            novo_dado[campo] = codigo
        else:
            valor = input(f"Digite {campo}: ")
            if tipo == int:
                valor = int(valor)
            novo_dado[campo] = valor

    dados.append(novo_dado)
    salvar_dados_arquivo(dados, tipo_dado)
    print(f"\n{tipo_dado} adicionado com sucesso!")


def listar_dados(dados, tipo_dado):
    if len(dados) == 0:
        print(f"Não há {tipo_dado} cadastrados.")
    else:
        print(f"\n{tipo_dado} cadastrados:")
        for dado in dados:
            print("- Código:", dado["Codigo"])
            for campo, valor in dado.items():
                if campo != "Codigo":
                    print(f"  {campo.capitalize()}: {valor}")
            print("")
        input("Pressione Enter para voltar")


def excluir_dado(dados, tipo_dado):
    codigo = int(input(f"Digite o código do {tipo_dado} a ser excluído: "))
    for dado in dados:
        if dado["Codigo"] == codigo:
            dados.remove(dado)
            salvar_dados_arquivo(dados, tipo_dado)
            print(f"{tipo_dado} excluído com sucesso!")
            break
    else:
        print(f"{tipo_dado} não encontrado.")


def editar_dado(dados, tipo_dado, campos):
    codigo = int(input(f"Digite o código do {tipo_dado} a ser editado: "))
    for dado in dados:
        if dado["Codigo"] == codigo:
            for campo, tipo in campos.items():
                novo_valor = input(f"Digite novo valor para {campo}: ")
                if tipo == int:
                    novo_valor = int(novo_valor)
                dado[campo] = novo_valor
            salvar_dados_arquivo(dados, tipo_dado)
            print(f"{tipo_dado} editado com sucesso!")
            break
    else:
        print(f"{tipo_dado} não encontrado.")


def verificar_codigo_existente(dados, codigo):
    for dado in dados:
        if dado["Codigo"] == codigo:
            return True
    return False


def gerenciar_dados(dados, tipo_dado, campos):
    while True:
        apresentar_menu_operacoes(tipo_dado)
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            incluir_dado(dados, tipo_dado, campos)
        elif opcao == "2":
            listar_dados(dados, tipo_dado)
        elif opcao == "3":
            editar_dado(dados, tipo_dado, campos)
        elif opcao == "4":
            excluir_dado(dados, tipo_dado)
        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")

def apresentar_menu_operacoes(tipo_dado):
    print("\n###########################################")
    print(f"\nMenu de Operações-- Gerenciar {tipo_dado}")
    print("\n###########################################\n")
    print("1. Incluir")
    print("2. Listar")
    print("3. Editar")
    print("4. Excluir")
    print("5. Voltar")


def menu_principal():
    estudantes = recuperar_dados_arquivo("estudantes")
    professores = recuperar_dados_arquivo("professores")
    disciplinas = recuperar_dados_arquivo("disciplinas")
    turmas = recuperar_dados_arquivo("turmas")
    matriculas = recuperar_dados_arquivo("matriculas")

    while True: 
        print("\n################")
        print("\nMenu Principal:")
        print("\n################\n")
        print("1. Gerenciar Estudantes")
        print("2. Gerenciar Professores")
        print("3. Gerenciar Disciplinas")
        print("4. Gerenciar Turmas")
        print("5. Gerenciar Matrículas")
        print("6. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            gerenciar_dados(estudantes, "Estudantes", {"Codigo": int, "Nome": str, "CPF": str})
        elif opcao == "2":
            gerenciar_dados(professores, "Professores", {"Codigo": int, "Nome": str, "CPF": str})
        elif opcao == "3":
            gerenciar_dados(disciplinas, "Disciplinas", {"Codigo": int, "Nome": str})
        elif opcao == "4":
            gerenciar_dados(turmas, "Turmas", {"Codigo": int, "Disciplina": str, "Professor": str})
        elif opcao == "5":
            gerenciar_dados(matriculas, "Matrículas", {"Codigo": int, "Estudante": str, "Turma": str})
        elif opcao == "6":
            break
        else:
            print("Opção inválida! Tente novamente.")


menu_principal()
