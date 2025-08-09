numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def maiorNumero(lista):
    if not lista:
        return None
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

print ("Este código diz respeito à análise de uma lista pré-estabelecida, onde o objetivo é informar o maior número contido nela.\n")
print (f"O maior número existente na lista é: {maiorNumero(numeros)}")