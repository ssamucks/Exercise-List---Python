numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def impares(lista):
    
    numerosImpares = []
        
    for item in lista:
        if item%2==1:
            numerosImpares.append(item)
    
    return numerosImpares

print (f"\nAqui estão os elementos ÍMPARES da sua lista:\n{impares(numeros)}\n")