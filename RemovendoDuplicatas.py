numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def numerosDiferentes(lista):
    numerosUnicos = []
    for item in lista:
        if item not in numerosUnicos:
            numerosUnicos.append(item)
    return numerosUnicos

print ("\nEste código diz respeito à análise de uma lista pré-estabelecida, com o objetivo de mostrar seus elementos sem que haja repetições de números.")
print (f"\nA lista sem números repetidos é: {numerosDiferentes(numeros)}.\n")
