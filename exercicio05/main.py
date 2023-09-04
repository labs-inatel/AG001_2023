""" Instituto Nacional de Telecomunicações - INATEL   (AG001- 2/2023)
Autora: Iza Lopes Ribeiro
Matricula: 316

Exercício 05 — Cálculo das equações: """

import sympy as sp

# Calcular da constante c, considerando o número da matrícula 316:
c = 316 % 10
print("\nValor de c:", c)

# Variáveis simbólicas:
x1, x2, x3 = sp.symbols('x1 x2 x3')

# Equações para serem calculadas em relação a x:
equacao1 = 2 ** x1 + 2 ** (4 * x1) - (c + 1)
equacao2 = 5 * sp.sqrt(x2) - 4 * x2 ** 2 + (x2 / 2) - c
equacao3 = (3 * sp.tan((c - 3) * x3) + 2) ** 2

# Resolver as equações para encontrar x:
solucao1 = sp.solve(equacao1, x1)
solucao2 = sp.solve(equacao2, x2)
solucao3 = sp.solve(equacao3, x3)

# Imprimir as soluções:
print(f"Valor de X1 para equacao1:", solucao1[0].evalf(2))
print(f"Valor de X2 para equacao2:", solucao2[0].evalf(2))
print(f"Valor de X3 para equacao3:", solucao3[0].evalf(2))
