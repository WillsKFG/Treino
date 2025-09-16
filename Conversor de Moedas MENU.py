print("\n~~~~ Conversor de Real ~~~~\n")

while True:
    print('''\nDigite a opção desejada:
    [1] - Real Para Dólar
    [2] - Real Para Euro
    [3] - Real Para Peso Argentino
    [4] - Real para Libra
    [5] - Real para Iene

    [0] - Sair do programa\n''')

    escolha = int(input("Escolha uma opção: "))

    if escolha == 0:
        print("\nSaindo do programa...\n")
        print("--------------FIM DO PROGRAMA--------------\n")
        break

    elif escolha == 1:
        print("\n--- Reais para Dólares ---")
        valor = float(input("Quantos reais você tem? R$ "))
        dolar = valor / 7.52
        print(f"\nCom R${valor:.2f} você pode comprar US${dolar:.2f}.\n")

    elif escolha == 2:
        print("\n--- Reais para Euros ---")
        valor = float(input("Quantos reais você tem? R$ "))
        euro = valor / 6.46
        print(f"\nCom R${valor:.2f} você pode comprar EURO${euro:.2f}.\n")

    elif escolha == 3:
        print("\n--- Reais para Pesos Argentinos ---")
        valor = float(input("Quantos reais você tem? R$ "))
        pesoarg = valor / 0.01
        print(f"\nCom R${valor:.2f} você pode comprar PESOS${pesoarg:.2f}\n")

    elif escolha == 4:
        print("\n--- Reais para Libras ---")
        valor = float(input("Quantos reais você tem? R$ "))
        libra = valor / 7.52
        print(f"\nCom R${valor:.2f} você pode comprar LIBRA${libra:.2f}.\n")

    elif escolha == 5:
        print("\n--- Reais para Ienes ---")
        valor = float(input("Quantos reais você tem? R$ "))
        dolar = valor * 25.95
        print(f"\nCom R${valor:.2f} você pode comprar IENES${dolar:.2f}.\n")

    else:
        print("Opção inválida! Tente novamente.\n")

    print("DESEJA CONTINUAR?")
    continuar = str(input("Digite S para SIM ou N para NÃO: ")).strip().upper()
    if continuar != "S":
        print("\nSaindo do programa...\n")
        print("--------------FIM DO PROGRAMA--------------\n")
        break