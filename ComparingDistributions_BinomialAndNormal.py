from scipy.stats import norm
from scipy.stats import binom

# Quiz Question 6:

# Os preços de diversos modelos de celulares no estoque de uma loja são normalmente distribuídos,
# com média = 1250 e desvio padrão igual a 480.
# Qual a chance de escolher aleatoriamente um aparelho que custe menos que 1500?
# # Atenção: É uma distribuição normal então usamos norm()

xalvo = 1500
xmedia = 1250
xdesvio = 480

p = norm.cdf(xalvo, xmedia, xdesvio)
print(p, 'é a Probabilidade tirar celular $ maior que', str(xalvo))

# Complementar - Comparando funções norm e binom
# O desvio padrão não é parametro neste problema com moedas
# - não é uma distribuição normal, então vamos resolver por binom()
# Qual a Probabilidade de acertar 8 vezes cara em 10 lançamentos de moeda e 0.5 para 1 lançamento

zsuccess = 8
zmedia = 10
zumlan = 0.5

z = binom.pmf(zsuccess, zmedia, zumlan)
print(z, 'é a probabilidade de acertar', str(zsuccess), 'vez(es) em', str(zmedia), ' lançamento(s)')
