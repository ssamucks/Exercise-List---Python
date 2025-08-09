numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

numerosPares = []

def pares(lista):
    
    numerosPares = []
        
    for item in lista:
        if item%2==0:
            numerosPares.append(item)
    
    return numerosPares

print (f"\nAqui estão os elementos PARES da sua lista:\n{pares(numeros)}\n")