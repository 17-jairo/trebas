import pandas as pd

df = pd.read_csv(r'C:\Users\Jairo\OneDrive\Documentos\emissions-ges-transport.csv')

print(df['Secteur'])

print(df.head(12))

print(df.tail(5))

print(df.shape)

print(df.info())

print(df.describe())

print(df. columns)

pivot_table = df.pivot_table(values='CO2(b)', index='Année', columns='Secteur', aggfunc='sum')

print(pivot_table)

print(df['Secteur'].isnull())



