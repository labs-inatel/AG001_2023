""" Instituto Nacional de Telecomunicações - INATEL   (AG001- 2/2023)
Autora: Iza Lopes Ribeiro
Matricula: 316

Exercício 03 — Cálculo da área sob a curva de uma função entre os valores 0 e 5: """

import sympy as sp

# Calcular da constante c, considerando n° da matrícula 316:
c = 316 % 10
print(f"Valor de c:", c)

# Variável simbólica:
x = sp.symbols('x')

# Definir a função:
funcao = x**3 - 4*x**2 + 5*x - c

# Calcular a integração da função:
integral = sp.integrate(funcao, x)

# Calcular a integral definida com limites de 0 a 5:
limite_superior = integral.subs(x, 5)
limite_inferior = integral.subs(x, 0)

# Calcular a diferença entre os limites de integração:
area = limite_superior - limite_inferior

# Apresentar o valor da area:
print(f"Area sob a curva da funcao dada no intervalo [0,5]:", area)
