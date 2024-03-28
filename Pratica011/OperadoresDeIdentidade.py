'''O que são operadores de identidade?
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.'''

curso = "Curso de Python"
NomeCurso = curso
saldo, limite = 200, 200

curso is NomeCurso
curso is not NomeCurso
saldo is limite
'''exmplo de operadores de identidade
o is e o is not, comparam os valores para saber se é verdadeiro ou falso a ocupação da mesma região de memórias.'''


saldo = 1000
limite = 500
print(saldo is limite)
print(saldo is not limite)