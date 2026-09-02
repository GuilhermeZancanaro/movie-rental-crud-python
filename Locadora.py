class Filme: # criando uma classe para guardar os dados dos filmes

    def __init__(self, nome, genero, ano):

        self.nome = nome
        self.genero = genero
        self.ano = ano


class Locadora: # a locadora será responsavel por manipular os dados da classe Filme

    def __init__(self):
        self.filmes = [] # criando a lista de filmes

    def adicionar_filme(self): # função para adicionar um filme, o usuario precisa por nome, genero e ano de lançamento
        nome = input("\nDigite o nome do filme que deseja adicionar: ")
        genero = input("\nDigite o gênero desse filme: ")
        ano = input("\nDigite o ano de lançamento do filme: ")

        filme = Filme(nome, genero, ano) # fazendo a relação das variaveis com a classe filme

        self.filmes.append(filme) # adicionando as informações na lista da locadora

        print("\nfilme adicionado com sucesso!")



    def listar_filme(self):# criando a função responsavel para listar os filmes cadastrados
        print("\n=====Filmes Cadastrados=====\n")

        for filme in self.filmes: # loop para ele pegar as informações na 'lista' da Locadora. Exibindo todas informações de cada filme separando por filmes
            print(f"Filme: {filme.nome}\nGênero: {filme.genero}\nAno de lançamento: {filme.ano}\n") # retorna as informações da 'lista' da Locadora fazendo sua respectiva relação com cada dado da classe Filme

    def alterar_filme(self): #Criando função para alterar 
        print("\nEscolha um filme para editar: \n")
        for i, filme in enumerate(self.filmes): 
           print(f"{i+1} - {filme.nome}") # loop para listar de maneira numerada cada item que seja um nome de filme na 'lista' começando pelo 1 (mesmo o indice sendo 0)

        escolha = int(input("\nDigite o numero do filme que deseja editar: ")) #criando a variavel escolha para o if/else

        if 1 <= escolha <= len(self.filmes): # Caso a escolha do usuario seja maior ou igual a 1 e ao mesmo tempo menor ou igual ao tamanho da 'lista', ele procede
           filme = self.filmes[escolha - 1] # Aqui ajustando para que subtraia 1 de qualquer opção que o usuario escolher, assim indo para a opção que estaria correta no indice da 'lista'

           print("\nO que deseja alterar?")
           print("1 - Nome")
           print("2 - Gênero")
           print("3 - Ano de lançamento")

           opcao = input("Digite sua opção: ")

           match opcao: # pequeno match para que a ação que o usuario escolheu aconteça. Substituindo o valor antigo do indice, pelo valor novo apresentado no input

            case '1':
                filme.nome = input("Digite o novo nome: ")

            case '2': 
                filme.genero = input("Digite o novo gênero: ")

            case '3':
                filme.ano = input("Digite o novo ano: ")

            case _:
                print("opção invalida")

        else:
            print("filme inválido") # Caso o if não proceda


    def remover_filme(self): # Criando função para Remover um filme
        if not self.filmes: #Caso ele não nada na 'lista'
            print("\nNão ha filmes na locadora!")

        else:
            for i, filme in enumerate(self.filmes):
                print(f"{i + 1} - {filme.nome}") #listando apenas os nomes dos filmes na 'lista' aumentando o indice em 1 para que a lista comece em 1

            opcao = int(input("\nDigite o numero do filme ao qual deseja remover da locadora: "))

            if 1 <= opcao <= len(self.filmes): #confirmando que o filme esta na lista
                remover = self.filmes.pop(opcao - 1) #subtraindo 1 da escolha do usuario para casar com o indice original da 'lista'
                print(f"\nFilme '{remover.nome}' removido com sucesso!")

            else:
                print("Filme inválido")


locadora = Locadora() # Definindo a classe Locadora

while True:
        print("\n=====Bem vindo à locadora=====")
        print("\n1. Adicionar um filme")
        print("\n2. Listar filmes adicionados")
        print("\n3. Alterar dados de um filme")
        print("\n4. Remover um filme")
        print("\n5. Sair\n")

        indice = input("Escolha uma opção: ")

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
                print("Saindo...")

                break # Quebrando o loop

            case _: # caso o usuario escreva algo que nao consata nas opções
                print("Opção invalida")

