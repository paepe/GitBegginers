from scipy.stats import norm

# Conjunto de objetos numa cesta, a media é 8 e o desvio padrao é 6
# Qual a probabilidade de tirar um objeto menor de 6kg

x = norm.cdf(6,8,2)
print(x)

# Qual a probabilidade de tirar um objeto maior de 6kg
y = norm.sf(6,8,2)
print(y)

# Qual a probabilidade de tirar um objeto menor de 6kg ou maior que 10 kg
z = norm.cdf(6,8,2) + norm.sf(10,8,2)
print(z)

# Qual a probabilidade de tirar um objeto menor de 10kg e maior que 8kg
t = norm.cdf(10,8,2) - norm.cdf(8,8,2)
print(t)