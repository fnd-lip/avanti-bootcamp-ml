import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', None, 'David'],
    'Idade': [24, None, 22, 35],
    'Salario': [50000, 60000, None, 70000]
}
df = pd.DataFrame(data)

valores_ausentes = df.isnull()
print("Valores ausentes:\n", valores_ausentes)

df_sem_nan = df.dropna()
print("\nDataFrame sem linhas ausentes:\n", df_sem_nan)

df_sem_colunas_nan = df.dropna(axis=1)
print("\nDataFrame sem colunas ausentes:\n", df_sem_colunas_nan)

df_preenchido = df.fillna(0)
print("\nDataFrame preenchido com 0:\n", df_preenchido)

media_idade = df['Idade'].mean()
df['Idade'] = df['Idade'].fillna(media_idade)
print("\nDataFrame com idade preenchida pela média:\n", df)


df_interpolado = df.interpolate()
print("\nDataFrame após interpolação:\n", df_interpolado)