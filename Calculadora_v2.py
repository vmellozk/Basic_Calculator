from time import sleep

while True:
    print("\nCALCULADORA PYTHON")
    sleep(1)

    try:
        numberOne = int(input("\nDigite o primeiro número: "))
        numberTwo = int(input("Digite o segundo número: "))

        print('''
              [1] Soma
              [2] Subtração
              [3] Divisão
              [4] Multiplicação
              [5] Qual o maior valor?
              [6] Novos números
              [7] Sair do programa
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
            if numberOne > numberTwo:
                print(f"O maior valor entre esses dois números é: {numberOne}")
            elif numberTwo > numberOne:
                print(f"O maior valor entre esses dois números é: {numberTwo}")
            else:
                print("Os dois números são iguais.")

        elif choice == "6":
            print("Escolha dos novos números.")
            sleep(1)
            numberOne = int(input("Digite o primeiro número: "))
            numberTwo = int(input("Digite o segundo número: "))

        elif choice == "7":
            print("Saindo do programa!")
            break

        else:
            print("Opção inválida. Tente novamente.")
    
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números inteiros.")
