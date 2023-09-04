""" Instituto Nacional de Telecomunicações - INATEL   (AG001- 2/2023)
Autora: Iza Lopes Ribeiro
Matricula: 316

Exercício 04 — Cálculo das correntes de um circuito: """

import sympy as sp

# Calcular da constante c, considerando n° da matrícula 316:
c = 316 % 10
print(f"\nValor de c:", c)

# Dados do problema:
resistor1 = 12000
resistor2 = 6000
resistor3 = 4000

# Variáveis simbólicas:
corrente1, corrente2 = sp.symbols('corrente1 corrente2')

# Calcular dos valores das fontes:
fonte1 = (c + 2) * 4
fonte2 = (c + 1) * 5

# Equações das malhas do circuito:
malha1 = -fonte1 + resistor1 * corrente1 + resistor2 * (corrente1 - corrente2)
malha2 = -fonte2 + resistor2 * (corrente2 - corrente1) + resistor3 * corrente2

# Resolver as equações para encontrar corrente1 e corrente2:
solucao = sp.solve((malha1, malha2), (corrente1, corrente2))

# Apresentar os valores das correntes:
print(f"Corrente 1:", solucao[corrente1].evalf(4), "[A]")
print(f"Corrente 2:", solucao[corrente2].evalf(4), "[A]")
