numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def somaLista(lista):
    soma = 0
    for item in lista:
        soma += item   
    return soma

print ("Este código diz respeito à análise de uma lista pré-estabelecida, onde o objetivo é informar a soma de seus elementos.\n")
print (f"O soma dos elementos da lista é: {somaLista(numeros)}")
