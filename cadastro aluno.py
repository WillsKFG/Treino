listaAlunos = []

def menu():
    print("\n\t----- LISTA ALUNOS -----\n")
    print('Deseja Realizar qual ação?')
    print("1- Cadastrar um(a) Aluno(a)")
    print("2- Consultar Aluno(a)")
    print("3- Alterar Aluno")
    print("4- Excluir Aluno(a)")
    print("5- Lista de Alunos")
    print("\n6- Sair do Programa")

#1
def cadastro():
    while True:
        print("\n\t~~ CADASTRO DE ALUNO(A) ~~")
        nome = str(input("Digite o nome do(a) aluno(a) que deseja cadastrar: ")).lower()
        if nome in listaAlunos:
            print("\n\tO nome já está cadastrado")
            break
        
        else:
         listaAlunos.append(nome)
         print(f"\nAluno(a) {nome.capitalize()} cadastrado com sucesso!!!")

        while True:
            opcaocadastro = str(input("\n\tDeseja cadastrar mais alguém? (S/N): ")).upper()
            if opcaocadastro == "S":
                break
            elif opcaocadastro == "N":
                return
            else:
                print("\n\topção inválida, tente novamente.")
            
#2
def consulta():
    print("\n\t~~ CONSULTA DE ALUNO(A) ~~\n")
    nomeConsulta = str(input("Insira o nome do(a) aluno(a) que deseja consultar: ")).lower()
    if nomeConsulta in listaAlunos:
        print("\n\tO(A) Aluno(a) está na na lista de cadastro")
    else:
        print(f"\nO(A) Aluno(a) {nomeConsulta.capitalize()} não está na na lista de cadastro\n")
        while True:    
            cadastrar = str(input(f"Deseja cadastrar o(a) aluno(a) {nomeConsulta.capitalize()}? (S/N): ")).upper()
            if cadastrar == "S":
                listaAlunos.append(nomeConsulta)
                print(f"\nO(a) Aluno(a) {nomeConsulta.capitalize()} foi cadastrado com sucesso!!!")
                break

            elif cadastrar =="N":
                break
            
            else:
                print("\t\nResposta Inválida, tente novamente")
           
#3
def alterar():
    print("\n\t~~ ALTERAR ALUNOS ~~\n")
    nomeAtual= str(input("Digite o Nome do(a) Aluno(a) que deseja alterar: "))
    if nomeAtual in listaAlunos:
        print("\n\t! Nome encontrado !\n")
        novoNome = str(input(f"Deseja alterar o nome {nomeAtual.capitalize()} para qual?: "))
        if novoNome in listaAlunos:
            print("\n\tEste nome já está cadastrado!!!\n")
        else:
            nomeAntigo = listaAlunos.index(nomeAtual)
            listaAlunos[nomeAntigo] = novoNome
            print(f"O nome: {nomeAtual.capitalize()}, foi alterado para {novoNome.capitalize()}.")
    else:
        print("\n\tAluno(a) não foi encontrado(a) na lista.")

#4
def excluir():
    print("\n\t~~ EXCLUIR ALUNOS ~~\n")
    excluirNome = str(input("Deseja excluir o nome de qual aluno(a)?: "))
    if excluirNome in listaAlunos:
        listaAlunos.remove(excluirNome)
        print(f'\n\tO(a) aluno(a) {excluirNome} foi excluído da lista!')
    else:
        print("\n\tO(a) Aluno(a) não está na lista, portanto não é possível excluir\n")

#5
def lista():
    print("\t~~ LISTA DE ALUNOS ~~\n")
    listaAlunos.sort()
    print("")
    for lista in listaAlunos:
        print(lista)


while True:
    menu()

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        consulta()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        lista()
    elif opcao == 6:
        print("\n\t FIM DO PROGRAMA\n")
        break
    else:
        print("Opção Inválida, Tente Novamente.")