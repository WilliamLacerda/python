'''Função input
A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo stirng, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.'''

nome = input('Informe seu nome:')
print(nome)
'''exemplo de uso do input.'''


'''Função print
A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos ára string, separados por sep e terminados por end. A string final é exibida para o usuário.'''

nome = 'Wilson'
sobrenome = 'Jacinto'

print(nome, sobrenome)
print (nome, sobrenome, sep='...\n')
print(nome, sobrenome, sep='#')
'''exemplo de uso dos argumentos opcionais.'''

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")