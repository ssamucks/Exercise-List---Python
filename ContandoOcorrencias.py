numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def ocorrencias(lista, nusuario):
    ocorrencia = 0
    for item in lista:
        if item == nusuario:
            ocorrencia += 1
    return ocorrencia

print ("Este código diz respeito à análise de uma lista pré-estabelecida, com o objetivo de informar quantas vezes determinado número aparece na lista.\n")
nusuario = int (input("Digite o número desejado: "))
print (f"A quantidade de ocorrências desse número é de: {ocorrencias(numeros, nusuario)} vez(es).")
