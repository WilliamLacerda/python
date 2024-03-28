'''Convetendo tipos
Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:
Variáveis do tipo string, que armazenam números e precisamos fazer algumas operação matemática com esse valor.'''

preço = 10
print(preço)

preço = float(preço)
print(preço)

preço = 10/2
print(preço)
'''exemplos de conversões, primeiro sendo inteiro e sendo convertido em flutuante. O float podendo ser feito de dois jeitos, um usando a o tipo float e o outro sendo divindo o número usando a divisão.'''


preço = 10.30
print(preço)

preço = int(preço)
print(preço)
''''exemplo de conversão de número flutuante para número inteiro.'''


preço = 10
print(preço)

print(preço/2)

print(preço//2)
'''exemplo de conversão de número inteiro para número flutuante usando divisão, no último está sendo divido com duas barras para fazer que o número seja preservado e assim fazendo ficar sem o ponto flutuante.'''


preço = 10.50
idade = 30
print(str(preço))

print(str(idade))
'''exemplo de conversão de número para string'''

texto = f"idade {idade}, preço {preço}"
print(texto)
'''outro exemplo de conversão de número para string, mas usando concatenação.'''


preço = "10.50"
idade = "30"

print(float(preço))

print(int(idade))
'''exemplo de conversão de string para número flutuante e número inteiro.'''


preço = "Python"
print(float(preço))
'''exemplo de erro de conversão, não é possivel converter uma string para número se não tiver um número na variável.'''


preço = 1.847235
print(int(preço))
'''exemplo de número flutuante sendo ignorado os número depois do zero por conta de estar em conversão inteira'''
