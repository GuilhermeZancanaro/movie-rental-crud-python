import json


class Filme:  # criando uma classe para guardar os dados dos filmes

    def __init__(self, nome: str, genero: str, ano: int, status: str = "Disponível"):
        self.nome = str(nome)
        self.genero = str(genero)
        self.ano = int(ano)  # Garante que o ano seja sempre armazenado como número inteiro
        self.status = str(status)  # Status do filme: 'Disponível' ou 'Alugado'

    def to_dict(self):
        # Converte o objeto Filme em dicionário para facilitar salvar em JSON
        return {
            "nome": self.nome,
            "genero": self.genero,
            "ano": self.ano,
            "status": self.status
        }


class Locadora:  # a locadora será responsável por manipular os dados e gerenciar os filmes

    def __init__(self, arquivo="filmes.json"):
        self.filmes = []  # criando a lista de filmes
        self.arquivo = arquivo  # arquivo onde os dados serão persistidos em JSON
        
        # Tupla com gêneros fixos e imutáveis da locadora em ordem alfabética
        self.generos = (
            "Ação",
            "Animação",
            "Comédia",
            "Documentário",
            "Drama",
            "Ficção Científica",
            "Romance",
            "Suspense",
            "Terror"
        )

        # Tupla com status fixos e imutáveis
        self.status_opcoes = (
            "Disponível",
            "Alugado"
        )

    def escolher_genero(self):
        # Permite selecionar um gênero a partir da lista de gêneros pré-definidos
        print("\nEscolha o gênero:")
        for i in range(len(self.generos)):
            print(f"{i + 1} - {self.generos[i]}")

        while True:
            try:
                opcao = int(input("\nDigite o número do gênero: "))
                if 1 <= opcao <= len(self.generos):
                    return self.generos[opcao - 1]
                else:
                    print("Opção inválida! Escolha um número da lista.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    def escolher_status(self):
        # Permite selecionar o status a partir da lista fixa de opções
        print("\nEscolha o status:")
        for i in range(len(self.status_opcoes)):
            print(f"{i + 1} - {self.status_opcoes[i]}")

        while True:
            try:
                opcao = int(input("\nDigite o número do status: "))
                if 1 <= opcao <= len(self.status_opcoes):
                    return self.status_opcoes[opcao - 1]
                else:
                    print("Opção inválida! Escolha um número da lista.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    def carregar_filmes(self):
        # Carrega os filmes do arquivo JSON
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                self.filmes = []
                # Percorre cada item (dicionário) lido do JSON e cria o objeto Filme
                for item in dados:
                    status = item.get("status", "Disponível")
                    filme = Filme(item["nome"], item["genero"], item["ano"], status)
                    self.filmes.append(filme)
                print(f"Dados carregados com sucesso! ({len(self.filmes)} filme(s) encontrado(s)).")
        except FileNotFoundError:
            # Caso o arquivo ainda não exista, inicia com a lista vazia
            self.filmes.clear()
        except json.JSONDecodeError:
            self.filmes.clear()

    def salvar_filmes(self):
        # Salva os filmes da lista no arquivo JSON
        with open(self.arquivo, "w", encoding="utf-8") as arq:
            dados = []
            # Percorre cada filme e converte em dicionário para salvar no JSON
            for filme in self.filmes:
                dados.append(filme.to_dict())
            # Grava a lista de dicionários no arquivo JSON formatado (indent=2 para legibilidade e ensure_ascii=False para preservar acentos)
            json.dump(dados, arq, indent=2, ensure_ascii=False)

    def adicionar_filme(self):  # função para adicionar um filme
        nome = input("\nDigite o nome do filme que deseja adicionar: ")
        genero = self.escolher_genero()
        
        # Validação do ano: deve ser inteiro e ter exatamente 4 dígitos
        # Loop while True: Se o usuário digitar algo inválido (ex: letras, 99 ou 20244), o programa exibe uma mensagem de erro e solicita a digitação novamente até que um valor correto seja fornecido
        while True:
            ano = input("\nDigite o ano de lançamento do filme (4 dígitos): ").strip()
            # isdigit(): Garante que o valor contenha apenas números inteiros (evita textos, espaços vazios ou símbolos) e len == 4 garante 4 dígitos
            if ano.isdigit() and len(ano) == 4:
                break
            print("[ERRO] Ano inválido! Digite exatamente 4 dígitos numéricos (ex: 1999).")

        # Todo novo filme cadastrado inicia com status padrão "Disponível"
        filme = Filme(nome, genero, ano, status="Disponível")
        self.filmes.append(filme)  # adicionando na lista da locadora

        print(f"\nFilme '{filme.nome}' adicionado com sucesso (Status: {filme.status})!")

    def listar_filme(self):  # função responsável por listar os filmes cadastrados
        print("\n===== Filmes Cadastrados =====")
        if not self.filmes:
            print("Não há filmes cadastrados na locadora!")
            return

        for i in range(len(self.filmes)):
            filme = self.filmes[i]
            print(f"\n[{i + 1}] Filme: {filme.nome}")
            print(f"    Gênero: {filme.genero}")
            print(f"    Ano de lançamento: {filme.ano}")
            print(f"    Status: {filme.status}")

    def alterar_filme(self):  # função para alterar os dados de um filme
        if not self.filmes:
            print("\nNão há filmes na locadora para alterar!")
            return

        self.listar_filme()  # Exibe os filmes cadastrados com detalhes

        try:
            escolha = int(input("\nDigite o número do filme que deseja editar: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            return

        if 1 <= escolha <= len(self.filmes):
            filme = self.filmes[escolha - 1]

            print(f"\nEditando o filme: {filme.nome}")
            print("1 - Nome")
            print("2 - Gênero")
            print("3 - Ano de lançamento")
            print("4 - Status (Disponível / Alugado)")

            opcao = input("\nDigite sua opção: ")

            match opcao:
                case '1':
                    filme.nome = input("\nDigite o novo nome: ")
                    print("\nNome alterado com sucesso!")

                case '2':
                    filme.genero = self.escolher_genero()
                    print("\nGênero alterado com sucesso!")

                case '3':
                    # Validação do ano: deve ser inteiro e ter exatamente 4 dígitos
                    while True:
                        novo_ano = input("\nDigite o novo ano (4 dígitos): ").strip()
                        if novo_ano.isdigit() and len(novo_ano) == 4:
                            filme.ano = int(novo_ano)
                            break
                        print("[ERRO] Ano inválido! Digite exatamente 4 dígitos numéricos (ex: 1999).")
                    print("\nAno de lançamento alterado com sucesso!")

                case '4':
                    filme.status = self.escolher_status()
                    print(f"\nStatus alterado com sucesso para '{filme.status}'!")

                case _:
                    print("\nOpção inválida!")
        else:
            print("\nFilme inválido!")

    def remover_filme(self):  # função para remover um filme
        if not self.filmes:
            print("\nNão há filmes na locadora para remover!")
            return

        self.listar_filme()  # Exibe os filmes cadastrados com detalhes

        try:
            opcao = int(input("\nDigite o número do filme que deseja remover: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            return

        if 1 <= opcao <= len(self.filmes):
            remover = self.filmes.pop(opcao - 1)
            print(f"\nFilme '{remover.nome}' removido com sucesso!")
        else:
            print("\nFilme inválido!")


def fazer_login():
    # Login simulado
    usuario_correto = "admin"
    senha_correta = "1234"

    print("=" * 35)
    print("   SISTEMA DE GESTÃO DE LOCADORA   ")
    print("           TELA DE LOGIN           ")
    print("=" * 35)

    while True:
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        if usuario == usuario_correto and senha == senha_correta:
            print(f"\nLogin realizado com sucesso! Bem-vindo(a), {usuario}!\n")
            break
        else:
            print("\n[ERRO] Usuário ou senha incorretos. Tente novamente.\n")


# Início do programa
if __name__ == "__main__":
    # 1. Autenticação inicial (Login Simulado)
    fazer_login()

    # 2. Inicialização da Locadora e carregamento dos dados persistidos
    locadora = Locadora("filmes.json")
    locadora.carregar_filmes()

    # 3. Menu principal (CRUD)
    while True:
        print("\n===== Bem-vindo à Locadora =====")
        print("1. Adicionar um filme")
        print("2. Listar filmes cadastrados")
        print("3. Alterar dados de um filme")
        print("4. Remover um filme")
        print("5. Sair")

        indice = input("\nEscolha uma opção: ")

        match indice:
            case '1':
                locadora.adicionar_filme()

            case '2':
                locadora.listar_filme()

            case '3':
                locadora.alterar_filme()

            case '4':
                locadora.remover_filme()

            case '5':
                # Salva os filmes no arquivo JSON ao encerrar
                locadora.salvar_filmes()
                print("\nDados salvos em 'filmes.json'. Saindo do programa...")
                break

            case _:
                print("\nOpção inválida! Escolha uma opção de 1 a 5.")
