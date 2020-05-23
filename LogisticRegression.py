import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

# carrega arquivo
base = pd.read_csv(
    '/Users/PPERES/Documents/PESSOAIS/CURSOS/Udemy/Cientista de Dados/Material do Curso/Estatística '
    'II/Dados/eleicao.csv', sep=";")

# # exibe grafico
# plt.scatter(base.DESPESAS, base.SITUACAO)
# plt.show()

# mostra estatisticas
print(base.describe())

# exibe correlacao forte - quanto mais gasta maior a possibilidade de ser eleito
print(np.corrcoef(base.SITUACAO, base.DESPESAS))

# carrega valores para variavel explanatoria
X = base.iloc[:, 2].values

# faz o reshape com funcao newaxis do numpay
X = X[:, np.newaxis]

# carrega valores para variavel dependente
y = base.iloc[:, 1].values

# inicializa e treina o modelo de regressao logistica
modelo = LogisticRegression()
modelo.fit(X, y)

# # exibe coeficientes de inclinacao e interceptacao do modelo
# print(modelo.coef_, modelo.intercept_)

# # gera arquivo aleatorio com valor de despesas para predicao do modelo
# # a partir do valor 10 até o valor 3000 gere 100 casos
# base_despesas_aleatorias = np.linspace(10, 3000, 100)

# # O python tem limitacoes para plotar regressoes logisticas
# # entao precisamos fazer alguns ajustes
#
# # criar funcao para gerar o SIGMOIDE
# def sigmoide(x):
#     return 1 / (1 + np.exp(-x))
#
#
# # chamar funcao simoide e armazena na matriz mtz_sigm gerada por ravel()
# mtz_sigm = sigmoide(base_despesas_aleatorias * modelo.coef_ + modelo.intercept_).ravel()
#
# # exiber valores de sigmoide
# print(mtz_sigm)
#
# # exibir grafico de sigmoide
# plt.plot(base_despesas_aleatorias, mtz_sigm, color = 'red')
# plt.show()


# agora carregaremos dados reais para predicao
base_previsao = base = pd.read_csv(
    '/Users/PPERES/Documents/PESSOAIS/CURSOS/Udemy/Cientista de Dados/Material do Curso/Estatística '
    'II/Dados/NovosCandidatos.csv', sep=";")

x_despesas = base_previsao.iloc[:, 1].values

# fazer reshape para adicionar uma coluna
x_despesas = x_despesas.reshape(-1, 1)

# fazer as previsoes com base no arquivo NovosCandidados - base_previsao
y_previsoes = modelo.predict(x_despesas)
print(y_previsoes)

# concatenar y_previsoes com a base_previsao
base_previsao = np.column_stack((base_previsao, y_previsoes))
print(base_previsao)

  