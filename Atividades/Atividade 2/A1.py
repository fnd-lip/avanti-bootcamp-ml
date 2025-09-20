def filtrar_impares(numeros):
    impares = [] 
    for num in numeros:  
        if num % 2 != 0:impares.append(num)  
    return impares  

numeros = [1, 2, 3, 4, 5, 6, 7]
impares = filtrar_impares(numeros)
print(impares) 