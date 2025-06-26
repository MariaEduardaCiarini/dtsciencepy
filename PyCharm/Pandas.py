import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

df = pd.read_csv(url)
print(df)

# 5 linhas csv
print(df.head())

# informações
print(df.info())