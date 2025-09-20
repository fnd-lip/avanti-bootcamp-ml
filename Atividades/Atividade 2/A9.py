import pandas as pd
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [24, 30, 22, 35],
    'Salario': [50000, 60000, 45000, 70000]
}
df = pd.DataFrame(data)

coluna_nome = df['Nome']
filtro_idade = df[df['Idade'] > 25]

print("Coluna 'Nome':\n", coluna_nome)
print("\nFiltrando linhas onde 'Idade' > 25:\n", filtro_idade)