import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

tratamento = pd.read_csv(
    '/Users/PPERES/Documents/PESSOAIS/CURSOS/Udemy/Cientista de Dados/Material do Curso/Estatística '
    'III/Dados/anova.csv', sep=';')

tratamento.boxplot(by='Remedio', grid=False)

