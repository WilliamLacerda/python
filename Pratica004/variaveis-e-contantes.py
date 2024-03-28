'''Variáveis
Em linguagem de programação podemos definir valores  que podem sofrer alterações no decorrer da execução do programa. Esses valores  recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.'''

idade = 20
nome = 'William'

nome, idade = 'Giovanna', 30
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')

idade, nome = (20, 'William')
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')
'''dois tipos de exemplos de variáveis.
uma sendo padrão e a outra sendo colocando as variáveis separando com virgula e deixando na mesma linha ao invés de separar cada uma em linhas'''


'''Constantes
Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.'''

'''Python não tem constantes
Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos 'final' e 'const', respectivamente para declarar uma constante.
Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maiúsculas:'''

'''ABS_PATH = 'home/willi/Documents/python_course/'
DEBUG = True
STATES = {'SP','RJ','MG',}
AMOUNT = 30.2
Exemplos de que esses códigos estão em uma constante para se manter sem mudar que nem uma variável'''

'''Dicas de bons usos:
O padrão de nomes em Python, deve ser em underline. (eexemplo: botar underline nos espaços em branco ao invés de deixar vazios em nomes, mas também tem outras formas como fazer misto entre maiúsculas e minúsculas junto com underline.)
Escolher nomes sugestivos. (exemplo: colocando uma variável para representar os nomes sendo como Nome, ou colocando variável que representa a idade, sendo Idade.)
Nome de constatnes todo em maiúsculo. (exemplo: colocar em constante uma variável de usuário único, colocar como: NOME_DE_USUÀRIO)'''

