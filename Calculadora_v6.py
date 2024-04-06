# Programa: Calculadora Python
# Descrição: Este programa implementa uma calculadora simples em Python que permite ao usuário realizar operações matemáticas básicas.

#Bibliotecas
from time import sleep
import os

#Função de limpar o console
def limpar_console():
    '''Detecta o sistema operacional e utiliza o comando adequado.'''
    os.system("cls" if os.name == 'nt' else 'clear')

#Variáveis
numberOne = 0
numberTwo = 0
choice = '' 
continuar = ''
valid_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') #Tupla do input permitido

#Código principal
while True:
    print("\nCALCULADORA PYTHON")
    sleep(1)

    #Bloco try except para tratar os erros
    try:
        #Solicita os números ao usuário
        numberOne_input = input("\nDigite o primeiro número: ")
        numberTwo_input = input("Digite o segundo número: ")
        '''Não declarar o input como float se não vai cair na exceção'''

        #Verifica se cada input está na tupla
        if all(char in valid_chars for char in numberOne_input) and all(char in valid_chars for char in numberOne_input):

            #Converte o input para float
            numberOne = float(numberOne_input)
            numberTwo = float(numberTwo_input)
        else:
            print("Entrada inválida. Insira apenas números.")
            sleep(3)
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                limpar_console()
                break
            limpar_console()
            continue
        
        #Converte para int se declarado int
        if numberOne.is_integer():
            numberOne = int(numberOne)
        if numberTwo.is_integer():
            numberTwo = int(numberTwo)

        #Variáveis das operações
        #Inclusive foi declarado aqui para não ter nenhum problema com os valores
        result_soma = numberOne + numberTwo
        result_sub = numberOne - numberTwo
        result_div = numberOne // numberTwo
        result_mult = numberOne * numberTwo

        #Exibindo opções para o usuário
        print('''
              [1] Soma
              [2] Subtração
              [3] Divisão
              [4] Multiplicação
              [5] Novos números
              [6] Sair do programa
              ''')         
                 
        #Solicitando escolha ao usuário
        choice = input("Escolha uma opção: ")

        #Opção de soma
        if choice == "1":
            sleep(1)
            #Verifica e converte para Int 
            if result_soma.is_integer():
                print(f'{numberOne} + {numberTwo} = {result_soma}')
            else:
                #Tratando as casas decimais
                print(f'{numberOne} + {numberTwo} =~ {result_soma:.3f}')
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                limpar_console()
                break
            limpar_console()

        #Opção de subtração
        elif choice == "2":
            sleep(1)
            #Verifica e converte para Int 
            if result_sub.is_integer():
                print(f'{numberOne} - {numberTwo} = {result_sub}')
            else:
                #Tratando as casas decimais
                print(f"{numberOne} - {numberTwo} =~ {result_sub:.3f}")
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                limpar_console()
                break
            limpar_console()

        #Opção de divisão
        elif choice == '3':
            sleep(1)
            #Verifica e converte para Int 
            if result_div.is_integer():
                print(f'{numberOne} // {numberTwo} = {result_div}')
            else:
                #Tratando as casas decimais
                print(f'{numberOne} / {numberTwo} =~ {result_div:.3f}')
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                limpar_console()
                break
            limpar_console()

        #Opção de multiplicação
        elif choice == '4':
            sleep(1)
            #Verifica se o número é zero
            if numberOne == 0 or numberTwo == 0:
                print("Multiplicação por zero não é possível! Por favor, insira dois números diferentes de zero.")
                sleep(2)
                continuar = input("\nVocê deseja continuar? [S] ou [N]")
                if continuar != "S":
                    print("OK! Reiniciando o programa.")
                    limpar_console()
                    continue
            #Verifica e converte para Int 
            if result_mult.is_integer():
                print(f"{numberOne} * {numberTwo} = {result_mult}")
            else:
                #Tratando as casas decimais
                print(f'{numberOne} * {numberTwo} =~ {result_mult:.3f}')
            continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
            if continuar != 'S':
                limpar_console()
                break
            limpar_console()

        #Opção de escolha de novos números
        elif choice == "5":
            sleep(1)
            limpar_console()
            print("OK! Só um instante")
            sleep(3)
            limpar_console()
            print("\nEscolha seus novos números.")
            sleep(1)
            continue

        #Opção para saída do programa
        elif choice == "6":
            sleep(1)
            print("Saindo do programa!")
            sleep(3)
            limpar_console()
            break

        #Trata uma entrada inválida, caso o usuário digite um número que não está dentro das opções
        else:
            limpar_console()
            print("Opção inválida. Tente novamente.")
            sleep(2)
            print("Reiniciando o programa...")
            sleep(4)
            limpar_console()

    #Trata uma entrada nula ou inválida fornecida pelo usuário
    except ValueError:
        sleep(1)
        limpar_console()
        print("\nEntrada inválida. Certifique-se de utilizar uma opção.")
        sleep(2)
        print("Reiniciando o programa...")
        sleep(4)
        limpar_console()

    #Verifica se a divisão foi feita por 0
    except ZeroDivisionError:
        print(f"\nERRO! Divisão por 0 é impossível!")
        sleep(3)
        continuar = input("\nVocê deseja continuar? [S] ou [N]: ").upper()
        if continuar != "S":
            limpar_console()
            print("OK! Reiniciando o programa.")
            limpar_console()
            continue
        
    #Trata erros inesperados
    except Exception as error:
        print(f"Ocorreu um erro inesperado: {error}")
        sleep(2)
        print(f"Por favor, tente novamente ou contate o suporte.")
        sleep(5)
        limpar_console()
        continuar = input("\nVocê deseja continuar? [S] ou [N]").upper()
        if continuar != "S":
            limpar_console()
            print(f"OK! Reiniciando o programa.")
            limpar_console()
            continue
