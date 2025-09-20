import pandas as pd
import numpy as np

data = {'valores': [10, 12, 12, 13, 12, 100, 14, 12, 13, 11]}
df = pd.DataFrame(data)

media = df['valores'].mean()
desvio_padrao = df['valores'].std()

limite_superior = media + 2 * desvio_padrao
limite_inferior = media - 2 * desvio_padrao

df['outlier'] = df['valores'].apply(lambda x: x > limite_superior or x < limite_inferior)

df['valores_tratados'] = np.where(df['outlier'], np.nan, df['valores'])

print(df)