import np
import statistics
from fractions import Fraction as F
from decimal import Decimal as D

# Onde está o erro de np
# np.random.choice(a = [0, 1], size = 50, replace = True, p = [0.5, 0.5, 0.2])

# Calcular a Mediana
x = statistics.median([22, 10, 12, 14, 13, 15])
print(x)
