'''A estética
Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

Bloco de comando
As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e o fim do bloco. Em Java e C po exemplo, utilizamos chaves.'''

'''void sacar(double valor) { Início do bloco do método
    if (this.saldo >= valor) { Início do bloco do if
        this.saldo -=;
    } Fim do boco do if
} Fim do bloco do if
exemplo de bloco em Java'''

'''void sacar(double valor) {
if (this.saldo >= valor){
this.saldo -= valor;
} Fim do bloco do if
} Fim do bloco do método
exemplo de bloco em Java sem formatar'''


'''Utilizando espaços
Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem, Nesse documento é indicado utilizar 4 espaços em branco por nível de indetação, ou seja, a cada novo bloco adicionamos 4 novos espaçoes em branco.

def sacar(self, valor: float) Nome: |Início do bloco de método

    if self.saldo >= valor: |Início do bloco if
    
        self.saldo -=

    |Fim do bloco do if

|Fim do bloco do método
exemplo de bloco em Python'''

'''
def sacar(self, valor: float) Nome: |Início do bloco do método
if self.saldo >= valor: |Início do bloco do if
self.saldo -= valor
|Fim do bloco do if
|Fim do bloco do método
exemplo de bloco de Python sem formatar, mas isso não funciona nele e vai dar erro.'''

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

    
sacar(1000)