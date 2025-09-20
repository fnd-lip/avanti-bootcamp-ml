import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

df_empilhado_linhas = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Concatenado por linhas:\n", df_empilhado_linhas)

df_empilhado_colunas = pd.concat([df1, df2], axis=1)
print("\nConcatenado por colunas:\n", df_empilhado_colunas)