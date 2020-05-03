from scipy.stats import binom

# Sucesso 3 vezes em 5 tentativas de lançamento de 1 moeda
prob = binom.pmf(3,5,0.5)
print(prob, "Probabilidade de sucesso no lancamento da moeda")

# Atravessar 4 sinais de 4 tempos, probabilidade de pegar (1,2,3,4) sinais verdes
ss = float(input('Entre o nr. de sucesso esperado: '))
es = float(input('Entre o nr. de tentativas: '))
ps = float(input('Entre a Probabilidade p/ 1 evento: '))
sinal = binom.pmf(ss,es,ps)
print(sinal, "Probabilidade de sucesso de atravessar os sinais")

