def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[0])

lista_pessoas = [("Felipe", 33), ("Alice", 30),("Charlie", 35), ("Bob", 25)]
lista_ordenada = ordenar_por_nome(lista_pessoas)
print(lista_ordenada)  

