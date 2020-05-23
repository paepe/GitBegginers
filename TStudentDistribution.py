from scipy.stats import t
from math import sqrt as sqt

# Exemplo de Distribuição T de Student
# Aula 48
# Por que usamos T de Student: Temos uma amostra pequena que não se assemelha a uma distribuição normal.
# Condições e consequências ao aplicarmos T de Student

# 1 - Utilizar quando a amostra é pequena (menor que 30)
# 2 - Também podemos aplicar quando não conhecemos o desvio padrão
# 3 - Impacto ou custo de usra T de Student: a variabilidade irá aumentar
# 4 - Haverá uma tendência maior de encontrarmos valores em caudas maiores ou mais longas e maior variação
# 5 - Para n>= a 30 já teríamos provavelmente uma distribuição NORMAL e não a T de Student

# Exercicio nr. 1 - Teste de hipótese
# Uma pesquisa afirma que o salario de um cientista de dados é de R$ 75,00 hora, uma
# amostra de 9 cientistas foram questionados para confirmar teste. Sabe-se que o desvio padrão da amostra é de 10.
# Qual é a probabilidade do salário ser MENOR que R$ 80,00?

m = 75  # salario médio por hora apresentado na 1a. pesquisa
S = 10  # desvio padrao da amostra na 1a. pesquisa
n = 9  # tamanho da amostra para o teste de hipótes - atende a T Student (n<=30)
to = 8  # graus de liberdade - definido por: (to = n-1)
X = 80  # Média que queremos testar

# Primeiro Calcule t

t1 = (X - m) / (S / sqt(n))
print(t1)

# Em seguida verifique a probabilidade (%) a partir de t - na tabela T de Studente ou
# pela função pt (probabilidade de t) no R
# Use os parametros t e to (graus de liberdade)

result = t.cdf(t1, to)
print(result)

# Exercicio nr. 2 - Teste de hipótese
# Uma pesquisa afirma que o salario de um cientista de dados é de R$ 75,00 hora, uma
# amostra de 9 cientistas foram questionados para confirmar teste. Sabe-se que o desvio padrão da amostra é de 10.
# Qual é a probabilidade do salário ser MAIOR que R$ 80,00?

m2 = 75  # salario médio por hora apresentado na 1a. pesquisa
S2 = 10  # desvio padrao da amostra na 1a. pesquisa
n2 = 9  # tamanho da amostra para o teste de hipótes - atende a T Student (n<=30)
to2 = 8  # graus de liberdade - definido por: (to = n-1)
X2 = 80  # Média que queremos testar

result2 = t.sf(t1, to2)
print(result2)
