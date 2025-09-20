def segundo_maior(lista): 
    if len(lista) < 2:
        return None 
    conjuntos_unicos = set(lista)
    
    if len(conjuntos_unicos) < 2:
        return None 
    conjuntos_unicos.remove(max(conjuntos_unicos))
    
    return max(conjuntos_unicos)

numeros = [3, 1, 4, 4, 5, 2]
resultado = segundo_maior(numeros)
print(resultado) 