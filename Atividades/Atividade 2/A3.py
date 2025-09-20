def elementos_unicos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    elementos_unicos = list(conjunto1.symmetric_difference(conjunto2))
    return elementos_unicos  

lista1 = [1, 2, 3, 4, 5, 8]
lista2 = [2, 4, 5, 6, 7, 8]
unicos = elementos_unicos(lista1, lista2)
print(unicos) 
