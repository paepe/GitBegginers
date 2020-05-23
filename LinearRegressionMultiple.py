# importa pacote para manipulacao de dados
import pandas as pd
# importa pacote de funções matriciais matemáticas
import numpy as np
# importa pacote para plotting
import matplotlib.pyplot as plt
# inclui pacote de aprendizado de maquina
from sklearn.linear_model import LinearRegression
# inclui pacote para rodar formulas do R Cran no Python
import statsmodels.formula.api as sm

# --- EXERCICIO COM REGRESSAO LINEAR PELO ARQUIVO mt_cars.csv ---
# 1 - Preparando modelo para uma regressão linear SIMPLES

# carrega arquivo mt_cars.csv
base = pd.read_csv(
    '/Users/PPERES/Documents/PESSOAIS/CURSOS/Udemy/Cientista de Dados/Material do Curso/Estatística '
    'II/Dados/mt_cars.csv')

# elimina coluna Unnamed: 0 - (texto com o nome dos carros)
base = base.drop(['Unnamed: 0'], axis=1)

# seleciona a matrix de x a 3a. coluna
x = base.iloc[:, 2].values

# seleciona a matrix de y a 1a. coluna
y = base.iloc[:, 0].values

# coeficientes de correlacao
correlacao = np.corrcoef(x, y)

# reshape de x (-1) vamos conservar todas as linhas - teremos uma matriz coluna
# e (1) vamos incluir + uma coluna para a variavel explanatoria / idenpendente (x)

x = x.reshape(-1, 1)

# inicializa o modelo
modelo = LinearRegression()
modelo.fit(x, y)

# mostra o a intercepção e o coeficiente
intercept = modelo.intercept_
coeficiente = modelo.coef_

# mostra valor de R2
r2 = modelo.score(x, y)

# # plota o grafico com o modelo
# plt.scatter(x, y)
# plt.plot(x, modelo.predict(x), color='red')
# plt.show()

# usando a sintaxe do R Cran no Python pelo statsmodels para visualizar o r2 ajustado
# preparando modelo ajustado (r2 ajustado) com comandos do R Cran
# esta é uma demonstracao que nao impacta o exercicio acima
modelo_ajustado = sm.ols(formula='mpg ~ disp', data=base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

print(modelo_treinado.summary())

# Fazendo a predicáo
# passando o valor de x diretamente para predict() como matriz
x_predicao = modelo.predict([[200]])

# Fazendo a predicao passando x como uma variavel matricial x_new_val
x_new_val = [200]
x_predicao_new_val = modelo.predict([x_new_val])

print(intercept, coeficiente, r2, x_predicao, x_predicao_new_val)

# --- EXERCICIO COM REGRESSAO LINEAR PELO ARQUIVO mt_cars.csv ---
# 2 - Preparando modelo para uma regressão linear MULTIVARIDA

# seleciona a matriz de x a 2a.(cyl) 3a.(disp) e 4a. (hp) colunas
x1 = base.iloc[:, 1:4].values

# seleciona a matriz de y a 1a. coluna
y1 = base.iloc[:, 0].values

# inicializa o modelo
modelo2 = LinearRegression()
modelo2.fit(x1, y1)

# # plota o grafico com o modelo
# plt.scatter(x1, y1)
# plt.plot(x1, modelo.predict(x1), color='blue')
# plt.show()

# usando a sintaxe do R Cran no Python pelo statsmodels para visualizar o r2 ajustado
# preparando modelo ajustado (r2 ajustado) com comandos do R Cran
# esta é uma demonstracao que nao impacta o exercicio acima
modelo_ajustado2 = sm.ols(formula='mpg ~ cyl + disp + hp', data=base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()

# Fazendo a predicáo passando x como uma matriz para predict()
# note a necessidade de reshape invertido onde (1) vamos tratar como matriz linha
# e (-1) nao incluiremos coluna para a variavel explanatoria / independente (x)
# 2a.(cyl) 3a.(disp) e 4a. (hp) colunas
x_new_mtx = np.array([4, 200, 100]).reshape(1, -1)
x_predicao_new_mtx = modelo2.predict(x_new_mtx)

print(x_predicao_new_mtx)
