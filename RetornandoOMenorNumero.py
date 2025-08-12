numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def menorNumero(lista):
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

print ("Este código diz respeito à análise de uma lista pré-estabelecida, onde o objetivo é informar o menor número contido nela.\n")
print (f"O menor número existente na lista é: {menorNumero(numeros)}")
