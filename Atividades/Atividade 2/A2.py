def e_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(numeros):

    primos = []  
    for num in numeros:  
        if e_primo(num): 
            primos.append(num)  
    return primos  

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
primos = filtrar_primos(numeros)
print(primos)  