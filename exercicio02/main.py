""" Instituto Nacional de Telecomunicações - INATEL   (AG001- 2/2023)
Autora: Iza Lopes Ribeiro
Matricula: 316

Exercício 02 — Cálculo das equações de velocidade, deslocamento, aceleração e cálculo de aceleração em t=10: """

import sympy as sp

# Variável simbólica:
t = sp.symbols('t')

# Dados do problema:
amplitude = 0.15  # 15 centímetros convertidos para metros
frequencia_Hz = 20  # em Hertz

# Calcular a frequência angular (em rad/s):
omega = 2 * sp.pi * frequencia_Hz

# Calcular a fase (em rad), considerando n° de matrícula 316:
c = 316 % 10

# Calcular a equação de velocidade: v(t) = A * w * cos(w * t - c)
velocidade = amplitude * omega * sp.cos(omega * t - c)

# Calcular a equação de deslocamento por integração: x(t) = ∫v(t) dt
deslocamento = sp.integrate(velocidade, t)

# Calcular a equação da aceleração por derivação: a(t) = dv(t)/dt
aceleracao = sp.diff(velocidade, t)

# Calcular a aceleração em t = 10 segundos:
aceleracao_10seg = aceleracao.subs(t, 10)

# Apresentar as equações calculadas e aceleração para t=10:
print(f"\nEquação da velocidade: v(t) = {velocidade.evalf(4)} [m/s]")
print(f"\nEquação de deslocamento: x(t) = {deslocamento.evalf(4)} [m]")
print(f"\nEquação de aceleração: a(t) = {aceleracao.evalf(4)} [m/s^2]")
print(f"\nPara t = 10 segundos -> a(10) = {aceleracao_10seg.evalf(4)} [m/s^2]")
