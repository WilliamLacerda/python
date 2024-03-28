'''O que são estruturas de repetição?
São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado atráves de uma expressão lógica.'''
#receba um número do teclado e exiba os 2 números seguintes

a = int(input("Informe um número inteiro: "))
print(a)

a+= 1
print(a)

a+= 1
print(a)
'''exemplo de uma estrutura de repetição sem repetição. Isso faz com que seja manual o modo de fazer a repetição.'''

'''a = int(input("Informe um número inteiro: "))
print(a)

repita 2 vezes:
a += a
print(a) |adiciona uma quebra de linha
exemplo de uma estrutura de repetição com repetição. Isso faz com que apenas coloca uma X quantidade de vezes sem precisar usar o print várias vezes.'''


'''Comando for
O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.'''

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()
    print("Executa no final do laço") #adiciona uma quebra de linha
'''exemplo de uso de for. Neste exemplo o for irá fazer atribuição de letra por letra e vai separar as vocais que estão na lista da qualquer palavra ou frase.'''


'''Comando range.
Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para umf fim (exclusivo). Se usarmos range(i, j) será produzido:
i, i+1, i+2, i+3, ..., j-1.
Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.'''

list(range(4))
[0,1, 2, 3]

for numero in range(0, 11):
    print(numero, end=" ")

for numero in range(0, 51, 5):
    print(numero, end=" ")
    ''''exemplos do uso do range em lista. Ele irá fazer uma lista começando por 0 e ir até o númmero próximo do qual foi selecionado para ser o último, logo no exemplo será de 0 até 11 no primeiro, e no segundo foi programado para ir de 0 até 50 indo de 5 em 5.
    O 0 seria o start, o 51 sendo o end e o 5 sendo o step,'''


'''Comando while.
O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando sabemos o número exato de vezes que nosso bloco de código deve ser executado.'''

opção = -1

while opção != 0:
    opção = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opção == 1 :
        print("Sacando...")
    elif opção == 2:
        print("Exibindo o extrato...")
'''exemplo do uso de while. O while seria parecido com o if, tendo uma condição para que funcione, mas diferente do if, o while irá ser executado diversas vezes até que seja executado para encerrar o código.'''


'''Comando while/else.
Como o if/else, o while/else será bem parecido os processo de comando, mas ainda terá o elemento de while que irá fazer o código ser executado até que o else seja executado como forma de encerrar.'''

opção = -1

while opção != 0:
    opção = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opção == 1 :
        print("Sacando...")
    elif opção == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")


'''Comando break.
Este comando é usado quando se quer que o código seja encerrado caso ele seja executado, o break irá fazer o código se encerrar caso for executado.'''

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)
'''exemplo do uso de break, fará com que o código só pare quando o número 10 que está com o comando break seja executado.'''

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")
'''exemplo de uso de continue, ele irá fazer com que pule o número adicionado e continuar proseguindo com o restante, isso pode ser usado também para outro tipo de comando.'''

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero, end=" ")
'''método de uso de break e continue juntos, o break deve ser usado antes de continue, se não irá fazer criar um looping caso use o continue primeiro e o break depois.'''