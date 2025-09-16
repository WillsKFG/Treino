import math

def end2():
    print("\n--- Programa Finalizado ---\n")

def menu():
    while True:
        print("\n---------- VAMOS CALCULAR ----------\n")
        print("Selecione qual forma geométrica você deseja calcular a área\n")
        print("1 - CÍRCULO")
        print("2 - QUADRADO")
        print("3 - TRIÂNGULO")
        print("4 - RETÂNGULO")
        print("\n5- SAIR\n")

        opcao = int(input("\nDigite a opção desejada: "))
        if opcao == 5:
            print("--- Programa Finalizado ---")
            break

        if opcao == 1:
            r = int(input("\nDigite o raio do círculo: "))
            area_circulo(r)

        elif opcao == 2:
            lado = int(input("\nDigite o lado do quadrado: "))
            area_quadrado(lado)

        elif opcao == 3:
            base = int(input("\nDigite a base do triângulo: "))
            altura = int(input("\nDigite a altura do triângulo: "))
            area_triangulo(base, altura)

        elif opcao == 4:
            base = int(input("\nInsira a base do retângulo: "))
            altura = int(input("\nInsira a altura do retângulo: "))
            area_retangulo(base, altura)

        else:
            print("Opção inválida. Tente novamente.")
            continue

        # Pergunta se o usuário deseja continuar
        if not menu2():
            break

def menu2():
    while True:
        print("\nVOCÊ DESEJA CONTINUAR REALIZANDO ALGUM CÁLCULO?\n")
        escolha = input("Responda com (S/N): ").strip().upper()

        if escolha == "S":
            return True
        elif escolha == "N":
            end2()
            return False
        else:
            print("Resposta Inválida, TENTE NOVAMENTE")

def area_circulo(r):
    print("\nCALCULANDO A ÁREA DO CÍRCULO\n")
    pi = math.pi
    area = pi * r**2
    print(f"A área do círculo mede: {area:.2f}")

def area_quadrado(lado):
    print("\nCALCULANDO A ÁREA DO QUADRADO\n")
    area = lado * lado
    print(f"A Área do Quadrado é: {area:.2f}")

def area_triangulo(base, altura):
    print("\nCALCULANDO A ÁREA DO TRIÂNGULO\n")
    area = base * altura / 2
    print(f"A área do triângulo mede: {area:.2f}")

def area_retangulo(base, altura):
    print("\nCALCULANDO A ÁREA DO RETANGULO\n")
    area = base * altura
    print(f"A área do retangulo mede: {area:.2f}")

menu()

#| Passo | O que fazer                                                |
#| ----- | ---------------------------------------------------------- |
#| 1     | Veja onde usa `input()` e troque por `CTkEntry`            |
#| 2     | Veja onde usa `print()` e troque por `CTkLabel`            |
#| 3     | Crie funções para executar ações (ex: salvar, calcular)    |
#| 4     | Use `CTkButton` para chamar essas funções                  |
#| 5     | Organize a interface (pode usar `.pack()`, `.grid()` etc.) |