while True:
    print("\nCALCULADORA PYTHON")

    numberOne = int(input("\nDigite o primeiro número: "))
    numberTwo = int(input("Digite o segundo número: "))

    print('''
            [1] Soma
            [2] Subtração
            [3] Divisão
            [4] Multiplicação
            [5] Sair do programa
            ''')                  
    choice = input("Escolha uma opção: ")

    if choice == "1": 
        print(f"{numberOne} + {numberTwo} = {numberOne + numberTwo}")

    elif choice == "2":
        print(f"{numberOne} - {numberTwo} = {numberOne - numberTwo}")

    elif choice == '3':
        print(f'{numberOne} / {numberTwo} = {numberOne / numberTwo}')
    
    elif choice == '4':
        print(f'{numberOne} * {numberTwo} = {numberOne * numberTwo}')

    elif choice == "5":
        print("Saindo do programa!")
        break

    else:
        print("Opção inválida. Tente novamente.")