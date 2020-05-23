import numpy as np
from scipy.stats import chi2_contingency

# Calculando o Coeficiente de Correlacao
x = [15, 18, 20, 25, 30, 44]
y = [240, 255, 270, 283, 300, 310]

correlation = np.corrcoef(x, y)
print(correlation)

# calculando Qui.Quadrado
netflix = np.array([[19, 6], [43, 32]])
var_QSquare = chi2_contingency(netflix)
print(var_QSquare)
