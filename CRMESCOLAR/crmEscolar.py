nome_arquivo = "Registro.txt"

# Procura se o arquivo existe, caso não exista ele cria um novo.
try:
    with open(nome_arquivo, "a") as arquivo:
        pass
except Exception as e:
    print(f"Erro ao manipular o arquivo {nome_arquivo}: {e}")

# Função para cadastrar um aluno e nota
def add_aluno(nome, nota):
    try:
        nota = int(nota)
        if not (0 <= nota <= 100):
            print("Nota inválida! Deve ser um número entre 0 e 100.")
            return
        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(f"{nome},{nota}\n")
        print(f"Aluno {nome} com nota {nota} adicionado com sucesso!")
    except ValueError:
        print("Erro: A nota deve ser um número.")
    except Exception as e:
        print(f"Erro ao tentar escrever os dados de {nome}: {e}")

# Função para excluir o registro de um aluno
def excluir_aluno(nome):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = arquivo.readlines()

        lista_atualizada = [linha for linha in lista if linha.split(",")[0] != nome]
        with open(nome_arquivo, "w") as arquivo:
            arquivo.writelines(lista_atualizada)
        print(f"Registros de: {nome} apagados com sucesso.")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não existe ou foi excluído.")
    except Exception as e:
        print(f"Erro ao acessar o arquivo: {e}")

# Função para exibir as informações dos alunos
def exibir_informacoes():
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                nome, nota = linha.strip().split(",")
                print(f"Aluno: {nome:<20} Nota: {nota:>5}")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    except Exception as e:
        print(f"Erro ao acessar o arquivo: {e}")

# Função para atualizar todo o registro do aluno
def update_registro(nome_antigo, nome, nota):
    try:
        nota = int(nota)
        if not (0 <= nota <= 100):
            print("Nota inválida! Deve ser um número entre 0 e 100.")
            return

        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        with open(nome_arquivo, "w") as arquivo:
            for linha in linhas:
                nome_atual, nota_atual = linha.strip().split(",")
                if nome_atual == nome_antigo:
                    arquivo.write(f"{nome},{nota}\n")
                else:
                    arquivo.write(linha)
        print(f"Registro de '{nome_antigo}' atualizado para Nome: {nome}, Nota: {nota}.")
    except ValueError:
        print("Erro: A nota deve ser um número.")
    except Exception as e:
        print(f"Erro ao tentar atualizar os dados: {e}")

# Função para atualizar o nome do aluno
def update_nome(nome_antigo, nome_novo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        with open(nome_arquivo, "w") as arquivo:
            for linha in linhas:
                nome, nota = linha.strip().split(",")
                if nome.strip() == nome_antigo:
                    arquivo.write(f"{nome_novo},{nota}\n")
                else:
                    arquivo.write(linha)
        print(f"Nome do aluno atualizado de '{nome_antigo}' para '{nome_novo}' com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar atualizar os dados: {e}")

# Função para atualizar a nota do aluno
def update_nota(nome_aluno, nota_nova):
    try:
        nota_nova = int(nota_nova)
        if not (0 <= nota_nova <= 100):
            print("Nota inválida! Deve ser um número entre 0 e 100.")
            return

        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        with open(nome_arquivo, "w") as arquivo:
            for linha in linhas:
                nome, nota = linha.strip().split(",")
                if nome.strip() == nome_aluno:
                    arquivo.write(f"{nome_aluno},{nota_nova}\n")
                else:
                    arquivo.write(linha)
        print(f"Nota do aluno {nome_aluno} atualizada para '{nota_nova}' com sucesso.")
    except ValueError:
        print("Erro: A nota deve ser um número.")
    except Exception as e:
        print(f"Erro ao tentar atualizar os dados: {e}")

# Menu de opções
def menu():
    while True:
        print("""
        ========================
        Menu de Registro Escolar
        ========================
                
        Ações:
        1 - Exibir Alunos e Notas
        2 - Cadastrar Aluno e Nota
        3 - Excluir Registro de Aluno
        4 - Atualizar Registro
        5 - Sair
        """)
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                exibir_informacoes()
            case "2":
                nome = input("Digite o nome: ")
                nota = input("Digite a nota do aluno (0-100): ")
                add_aluno(nome, nota)
            case "3":
                nome = input("Digite o nome que deseja excluir: ")
                excluir_aluno(nome)
            case "4":
                exibir_informacoes()
                nome_anterior = input("Qual aluno você deseja atualizar?\n")
                opcao = input("""
                              Ações:
                              1 - Atualizar Registro completo
                              2 - Atualizar nome
                              3 - Atualizar nota
                              4 - Menu anterior\n""")
                if opcao == "1":
                    new_nome = input("Digite o novo nome: ")
                    new_nota = input("Digite a nova nota: ")
                    update_registro(nome_anterior, new_nome, new_nota)
                elif opcao == "2":
                    new_nome = input("Digite o novo nome: ")
                    update_nome(nome_anterior, new_nome)
                elif opcao == "3":
                    new_nota = input("Digite a nova nota: ")
                    update_nota(nome_anterior, new_nota)
                elif opcao == "4":
                    continue
            case "5":
                print("Até mais!")
                break
            case _:
                print("Opção inválida! Tente novamente.")

menu()