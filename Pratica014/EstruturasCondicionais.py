'''O que são estruturas condicionais?
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.'''

'''if
Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.'''

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Seu saque foi realizado com sucesso!")

if saldo < saque:
    print("Seu saldo é insuficiente!")
'''exemplo do uso do if para realizar um saque, o if seria uma forma para botar um requisito para permitir o saque'''


'''if/else
Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.'''

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Seu saque foi realizado com sucesso!")
else:
    print("Seu saldo é insuficiente!")
'''exemplo do uso do if/else, os dois juntos causam uma condição multipla, o if quando é executado, significa que o saque irá acontecer. Enquanto se o if não foi acionado, o else será acionado como forma de contrapartida e o saque será recusado por falta de saldo.'''


'''if/elif/else
Em alguns cénarios queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.'''

''''opção = int(input("Informe uma opção: [1]Sacar \n[2]Extrato: "))

if opção == 1:
    valor = float(input("Informe a quantia que deseja sacar: "))

elif opção == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
exemplo de uso de if/elif/else. O if é o requisito, o elif seria como um elseif em Java que seria como um se ou se não juntos, e por fim o else sendo o se não.
Neste saque o if é executado se for pressionado o 1 e caso for o 2, o elif vai ser extramo, se nenhum deles forem pressionados, o else será executado.'''


MaiorIdade = 18
IdadeEspecial = 16
idade = int(input("Informe sua idade: "))
if idade >= MaiorIdade:
    print("Maior de idade, pode tirar a CNH.")

if idade <= MaiorIdade:
    print("Ainda não pode tirar a CNH.")


if idade >= MaiorIdade:
    print("Maior idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MaiorIdade:
    print("Maior idade, pode tirar a CNH.")
elif idade == IdadeEspecial:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")


'''if aninhado
Podemos criar estruturas condicionais aninhadasm para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.'''

'''if ContaNormal:
    if saldo >= saque:
        print("Seu saque foi realizado com sucesso!")
    elif saque <= (saldo + ChequeEspecial):
        print("Saque realizado com uso do cheque especial!")
elif ContaUniversitaria:
    if saldo >= saque:
        print("Seu saque foi realizado com sucesso!")
    else:
        print("Seu saldo é insuficiente!")

exemplo de uso aninhado de if/elif/else. Este uso aninhado deixa ser possivel de criar vários tipos de requisitos ou opções de interação. Assim podendo adicionar como neste exemplo várias opções de contas bancarias.'''

ContaNormal = False
ContaUniversitaria = False
ContaEspecial = True

saldo = 2000
saque = 1500
ChequeEspecial = 500

if ContaNormal:
    if saldo >= saque:
        print("Seu saque foi realizado com sucesso!")
    elif saque <= (saldo + ChequeEspecial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, seu saldo é insuficiente!")

elif ContaUniversitaria:
    if saldo >= saque:
        print("Seu saque foi realizado com sucesso!")
    else:
        print("Seu saldo é insuficiente!")

elif ContaEspecial:
    print("Acesso a conta especial realizada com sucesso!")
else:
    print("Falha no sistema, seu tipo de conta não foi reconhecida, por favor contate o gerente. ")


'''if ternário
O if ternário permite escrever uma confição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.'''

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
'''exemplo do uso de if ternário, na qual tudo fica na mesma linha de forma mais curta e simples.'''

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")