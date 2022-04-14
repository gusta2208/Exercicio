import exercicio1
import exercicio2
import this
this.opcao = 0
num1 = 0

def mostrarMenu():
    print('Escolha uma das opções abaixo: '+
          '\n1 Exercicio 1' +
          '\n2 Exercicio 2' +
          '\n3 Exercicio 3' +
          '\n4 Exercicio 4' +
          '\n0 Sair')
    this.opcao = int(input())#coletar a digitação do usuario

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input())

def operecao():
    #Mostrar o menu em tela
    while this.opcao != 5:
        mostrarMenu()
        if this.opcao == 1:
            print(exercicio1.exercicioum(this.num1))
        elif this.opcao == 2:
            coletarNum1(exercicio2.exerciciodois(this.num1))
            print()
        elif this.opcao == 2:
            
        elif this.opcao == 0:
            print('Obrigado!')
        else:
            print('Opção escolha inválida, tente novamente!')


