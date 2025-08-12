numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def mediaAritmetica(lista):
    somaDosElem = sum(lista)

    totalDeElem = len(lista)
    
    media = somaDosElem / totalDeElem
    
    return media

print ("Este código diz respeito à análise de uma lista pré-estabelecida, onde o objetivo é informar a média aritmética de todos os seus valores.\n")
print (f"A média aritmética dessa lista é: {mediaAritmetica(numeros)}")
