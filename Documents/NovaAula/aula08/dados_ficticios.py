"""
Pessoas com idade maior que 40 anos
com renda maior de 5 mil
com renda maior de 15 mil
"""

import pandas as pd

dados = pd.read_csv('C:/Users/georg/Documents/NovaAula/aula08/dados_ficticios.csv')

df = pd.DataFrame(data=dados)

print(df[df['idade'] > 40])
print(df[df['renda'] > 5.000])
print(df[df['renda'] > 15.000])


