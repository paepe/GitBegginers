# Aula 59
# Por Regressao Linear, prever a velocidade (speed) de um carro no
# momento da sua freada apos percorrida certa distancia (dist)

# Manipula arquivos externos
import pandas as pd
# Modelos matematicos
import numpy as np
# Plota gráficos
import matplotlib.pyplot as plt
# Machine Learning
from sklearn.linear_model import LinearRegression

# Carregar arquivo CSV
base = pd.read_csv(
    '/Users/PPERES/Documents/PESSOAIS/CURSOS/Udemy/Cientista de Dados/Material do Curso/Estatística '
    'II/Dados/cars.csv')

# Eliminar 1a. coluna com informacao desnecessaria
base = base.drop(['Unnamed: 0'], axis=1)
print(base)

# Carregar variaveis X e Y para checar correlacao
X = base.iloc[:, 1].values
# transforme x em uma matriz n x 2 (exigido no modelo)
X = X.reshape(-1, 1)
y = base.iloc[:, 0].values

# # carregar o coeficiente de correlacao para x e y para evitar erro
# comente a linha x.reshape(-1,1) para que x seja novamente um vetor univoco
# correlacao = np.corrcoef(x,y)

# Fazer o treinamento
# Criar modelo de regressao linear a submeter a Machine learning
modelo = LinearRegression()
modelo.fit(X, y)

# Mostra a inteceptacao e o coeficiente do modelo
intercept = modelo.intercept_
coeficient = modelo.coef_

# # Plota gráfico com as variaveis x e y
plt.scatter(X, y)
plt.plot(X, modelo.predict(X), color='red')
plt.show()

# Se o carro parar numa distância x (var independente)
# teremos y (var dependente ou exploratória)
y_predicao_calc = modelo.coef_ + modelo.intercept_ * 22

# Ou diretamente no predict()
y_predicao = modelo.predict([[22]])

print(intercept, coeficient, y_predicao_calc, y_predicao)
