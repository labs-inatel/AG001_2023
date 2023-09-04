""" Instituto Nacional de Telecomunicações - INATEL   (AG001- 2/2023)
Autora: Iza Lopes Ribeiro
Matricula: 316

Exercício 01 — Cálculo dos limites: """

import sympy as sp

# Calcular da constante C para n° da matricula 316:
c = 316 % 10
print(f"Variavel c: ", c)

# Variável simbólica:
x = sp.symbols('x')

# Expressões dos limites:
limExpr_a = (1 + ((c + 4) / x ** 3)) ** x ** 3
limExpr_b = (1 + ((c + 4) / x ** 3)) ** x ** 3
limExpr_c = (1 + ((c + 4) / x ** 3)) ** x ** 3

# Calcular dos limites:
limite_a = sp.limit(limExpr_a, x, 0)
limite_b = sp.limit(limExpr_b, x, sp.oo)
limite_c = sp.limit(limExpr_c, x, -sp.oo)

# Verificar se existe ou não existe limite:
if sp.limit(limExpr_a, x, 0, dir='-') == sp.limit(limExpr_a, x, 0, dir='+') == sp.oo:
    print("Não existe limite.")
else:
    print(f"Valor encontrado para Limite tendendo a 0:", limite_a)

if sp.limit(limExpr_b, x, sp.oo, dir='-') == sp.limit(limExpr_b, x, sp.oo, dir='+') == sp.oo:
    print("Não existe limite.")
else:
    print(f"Valor encontrado para Limite tendendo a +infinito:", limite_b)

if sp.limit(limExpr_c, x, -sp.oo, dir='-') == sp.limit(limExpr_c, x, -sp.oo, dir='+') == sp.oo:
    print("Não existe limite.")
else:
    print(f"Valor encontrado para Limite tendendo a -infinito:", limite_c)
