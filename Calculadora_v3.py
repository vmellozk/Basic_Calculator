#Bibliotecas
from time import sleep
import os

#Função de limpar o console
def limpar_console():
    os.system("cls" if os.name == 'nt' else 'clear')

#Variáveis
numberOne = 0
numberTwo = 0
choice = ''
continuar = ''
result_soma = 0
result_sub = 0
result_div = 0
result_mult = 0

#Código principal
while True:
    print("\nCALCULADORA PYTHON")
    sleep(1)

    try:
        numberOne = float(input("\nDigite o primeiro número: "))
        numberTwo = float(input("Digite o segundo número: "))

        print('''
              [1] Soma
              [2] Subtração
              [3] Divisão
              [4] Multiplicação
              [5] Novos números
              [6] Sair do programa
              ''')         
                 
        choice = input("Escolha uma opção: ")

        if choice == "1":
            #Verifica e converte para int 
            sleep(1)
            result_soma = numberOne + numberTwo
            if result_soma.is_integer():
                result_soma = int(result_soma)
                print(f'{numberOne} + {numberTwo} = {result_soma}')
            #Tratando as casas decimais
            else:
                print(f'{numberOne} + {numberTwo} = {result_soma:.3f}')
    
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                break


        elif choice == "2":
            #Verifica e converte para Int 
            sleep(1)
            result_sub = numberOne - numberTwo
            if result_sub.is_integer():
                result_sub = int(result_sub)
                print(f'{numberOne} - {numberTwo} = {result_sub}')

            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                break


        elif choice == '3':
            #Verifica e converte para Int 
            sleep(1)
            result_div = numberOne / numberTwo
            if result_div.is_integer():
                print(f'{numberOne} // {numberTwo} = {result_div}')

            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                break
        

        elif choice == '4':
            #Verifica e converte para Int 
            sleep(1)
            result_mult = numberOne * numberTwo
            if result_mult.is_integer():
                print(f"{numberOne} * {numberTwo} = {result_mult}")
                
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                break


        elif choice == "5":
            sleep(1)
            limpar_console()
            print("\nEscolha dos novos números.")
            sleep(1)
            numberOne = int(input("\nDigite o primeiro número: "))
            numberTwo = int(input("Digite o segundo número: "))


        elif choice == "6":
            sleep(1)
            print("Saindo do programa!")
            break


        else:
            print("Opção inválida. Tente novamente.")


    except ValueError:
        sleep(1)
        print("Entrada inválida. Certifique-se de utilizar uma opção.")
