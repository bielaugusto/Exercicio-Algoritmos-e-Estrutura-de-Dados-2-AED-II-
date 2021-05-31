
def exibeMenu():
    print("### MENU ###")
    print("0 - SAIR\n")
    print("1 - Exercício 1")
    print("2 - Exercício 2")
    print("3 - Exercício 3")
    print("4 - Exercício 4")
    print("5 - Exercício 5")
    print("6 - Exercício 6")
    print("7 - Exercício 7")
    print("8 - Exercício 8")
    print("9 - Exercício 9\n")
    
    opcao = int(input("Escolha qual exercício vc deseja mostrar: "))

    return opcao

exibeMenu()

def escrever1():
    
    print("# (1) Escreva um algoritmo que imprima todos os números pares no intervalo")
    print("# aberto ]1..20[, ou seja, a saída é: 2, 4, 6, ..., 18. É obrigatória a")
    print("# Utilização de um comando de repetição")

    print('Números Pares no intervalo ]1; 20[')
    n = 0
    for n in range(1, 20):
      if n % 2 == 0:
        print(n, end='\n')
    print('FIM')

def escrever2():
    print("# (2) Escreva uma programa que recebe uma palavra e uma letra do teclado.")
    print("# Tal função deve contar quantas vezes a letra aparece na palavra e ")
    print("#retornar o valor. Obs: Não podem utilizar a função count. Utilize For.")

    palavra = 'teste'
    letra = 'e'
    quantidade = 0
    for c in palavra:
        if (c==letra):
            quantidade = quantidade+1

    print(quantidade)

def escrever3():
    print("# (3) Implemente um programa que leia 3 nomes e imprima a palavra ")
    print("# pelas duas primeiras letras de cada um dos nomes. Os nomes devem ")
    print("# armazenados em uma lista. Obs: A ordem dos fatores altera o produ")
    
    print("(#) para nomes=['julio', julieta', barbara'] a saida deve ser jujuba")
    nomes= []
    newName=""
    for i in range(3):
        nome=input('Digite o nome %d '%(i+1))
        nomes.append(nome)
    print(nomes)
    for nome in nomes:
        newName=newName+nome [0]+nome [1]
    print(newName)

def escrever4():
    print("# (4) Um professor possui 2 turmas, e cada turma possui 10 alunos")
    print("# Construa um algorítmo que leia a nota dos alunos de cada uma das turmas")
    print("# e exiba a média das notas por turmas. Utilizar WHILE dentro de WHILE ou FOR")
    print("# dentro de FOR  e matriz")
    
    notas= []
    for turma in range(2):
      notas.append([0] * 10)
      print (notas)
    for turma in range(2):
      print ('preencha as notas da turma ', turma+1)
      for aluno in range(10):
        print('nota do aluno ', aluno+1, end=": ")
        notas[turma] [aluno] = float(input())
    for turma in range(2):
      soma = 0
      for aluno in range(10):
        soma = soma + notas [turma] [aluno]
      print("Média da turma ", turma, ": ", soma/len(notas[turma]))

def escrever5():
    print("# (5) Explique como funciona a função range.")
    print("")
    print("A funcão range() permite gerar sequências de valores em progressão")
    print("aritmética. Muito útil para gerar as listas de valores pa") 
    print("")
    print("formas de uso: ")
    print("")
    print("range(N): gera valores inteiros de 0 até N-1 ")
    print("range (i, N): gera valores inteiros de i até N-1")
    print("range(i, N,D): gera os valores inteiros i, i+D, i+2D, ...")

def escrever6():
    print("# (6) Diferencie o while do for e exemplifique o uso de cada um deles")
    print("# com um código")
    print("")
    print("#O laco for é geralmente usado quando vc sabe, inicialmente, o número")
    print("#de interações. Por exemplo, para percorrer um vetor de 10 elementos.")
    print("#Por outro lado, o while é usado quando vc tem uma noção sobre a faixa")
    print("#de valores para fazer uma interação, mas não sabe o número exato de")
    print("#interações que ocorrerão. Por exemplo, imprima na tela os elementos")
    print("#de um vetor, formado por números em ordem aleatória, até que o número")
    print("#5 seja encontrado.")
    
    print('"- WHILE -"\n')
    
    contador = 0
    while (contador < 5):
           print(contador)
           contador   = contador + 1
    
    print('"- FOR -"\n')
    
    numero = int(input("Digite um numero de 1 a 10 para a tabuada: "))
    
    print("Tabuada do ",numero,": ")
    for i in range(1,11):
        print(numero," X ", i, " = ", numero*i)

def escrever7():
    print("# (7) Qual a diferença entre utilizar list e numpy para definir vetores python.")
    print("")
    print("Numpy é uma biblioteca para computação científica em Phyton, para utilizá-la é necessário importá-la. Essa biblioteca")
    print("fornece alto desempenho e ferramentas para manipulação de arrays multidimensionais. Um array Numpy deve ser composto")
    print("por elementos do mesmo tipo. Já uma lista (list) é nativa do python, ou seja, não é necessário que uma biblioteca seja")
    print("importada para ela ser utilizada. Além disso, uma lista em Python é equivalente a um array, mas é redimensionável")
    print("e pode conter elementos de diferentes tipos. Vejam o exemplo abaixo para somar duas matrizes.")
    print("")
    print("- programa para somar duas matrizes utilizando listas:")

    X = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]

    Y = [[5, 8, 1],
        [46, 7, 3],
        [4, 5, 9]]

    result = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    #iterar ao longo das linhas
    for i in range(len(X)):
        print(X[i])
        #iterar ao longo das colunas
        for j in range(len(X[i])):
            result[i][j] = X[i][j] + Y[i][j]

    for r in result:
        print(r)

    print("- Programa para somar duas matrizes utilizando Numpy")
    import numpy as np
    A = np.array([[2, 4], [5, -6]])
    B = np.array([[9, -3], [3, -6]])
    print("A: ", A)
    print("B :", B)
    C = A + B
    print("C: ", C)

def escrever8():
    print("# (8) Qual a diferença conceitual entre vetores e matrizes? Exemplifique o uso de cada um deles com um código phyton.")
    print("# Vetores e matrizes são coleções de variáveis contínuas na memória e acessadas por meio de um número de índice. A diferença entre vetores e matrizes é que vetores são uma única dimensão, enquanto matrizes podem conter várias dimensões")
    print("")
    print("- Programa com vetor")
    #Números ímpares com numpy em um array de única dimensão
    import numpy as np 

    arr = np.array([0,1,2,3,4,5,6,7,8,9])
    arr[arr % 2 == 1]

    print("- Programa com matrizes")
    #Importando Numpy para operações de matrizes 
    import numpy 

    #Inicialização de matrizes de duas dimensões 
    x = numpy.array([[1, 2], [4, 5]])
    y = numpy.array([[7, 8], [9, 10]])

    #Uso do add() para adicionar 
    print ("Adição de cada elemento da matriz: ")
    print (numpy.add(x,y))

    #Uso do subtract() para subtrair
    print ("Subtração de cada elemento da matriz: ")
    print (numpy.subtract(x,y))

    #Uso do divide() para dividir 
    print ("Divisão de cada elemento da matriz: ")
    print (numpy.divide(x, y))

    #Uso do multiply para multiplicar cada elemento 
    print("Multiplicação de cada elemento da matriz: ")
    print (numpy.multiply(x,y))

def escrever9():
    print("# (9) Modifique o exercício 1 para imprimir os números ímpares e salve em exercicio9.py.")

    print(' Números Pares no intervalo ]1; 20[')
    n = 0
    for n in range(1, 20):
      if n % 2 != 0:
        print(n, end='\n')
    print('FIM')


while opcao != 0:
    opcao = exibeMenu()
    if opcao <= 0:
        break
    elif opcao == 1:
        escrever1()
    elif opcao == 2:
        escrever2()
    elif opcao == 3:
        escrever3()
    elif opcao == 4:
        escrever4()
    elif opcao == 5:
        escrever5()
    elif opcao == 6:
        escrever6()
    elif opcao == 7:
        escrever7()
    elif opcao == 8:
        escrever8()
    elif opcao == 9:
        escrever9()
    else:
        print("### ERRO ###")
        break
    