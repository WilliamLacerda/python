'''O que são operadores lógicos?
São operadores utilizados em conjuntyo com os operadores de comparação, para montar uma expressão lógicas. Quando um operador de comparação pe utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
operador_comparação + operador_lógico + operador_comparação...N...'''

saldo = 1000
saque = 200
limite = 100
saldo >= saque
saque <= limite
'''exmplo de operação lógica.'''


saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite
'''exemplo de operador E (and).'''


saldo = 1000
saque = 200
limite = 100
saldo >= saque or saque <- limite
'''exemplo de operador OU (or).'''


contatos_emergencia = {}
1000 > 1500

contatos_emergencia

"saque 1500"

""
'''operador de negação: ele vai fazer negação (not), ele faz uma inversão, como pegando o false e o not será negação, logo será true. Quando for true, irá virar false. E em conteúdo vazio, irá dar false também.'''


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exemplo = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exemplo)
exemplo2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exemplo2)
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exemplo3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exemplo3)
'''exemplo de operador lógico com parênteses'''


'''and = para ser True tudo tem que ser True
or = para ser True apenas um tem que serr True'''

print(True and True and True)
print (True and False and False)
print(True or True)
print(True or False)
print(True or False)
print(False or False)
