from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

# Testar se um conjunto de dados é uma Distribuicao Normal

# variavel dados recebe 100 valores randomicamente
dados = norm.rvs(size=100)

# setting probplot com os a variavel dados
stats.probplot(dados, plot=plt)

# exibe grafico mostrando dispersao
plt.show()

# aplica teste de shapiro para verificar se temos uma distribuicao normal
shs = stats.shapiro(dados)

# exibe valores variavel shs apos teste de shapiro
print(shs)
