numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def doisMaiores(lista):
    
    maiornumero = segundomaior = float('-inf')
    
    for num in lista:
        
        if num > maiornumero:
            segundomaior = maiornumero
            maiornumero = num
        
        elif num > segundomaior and num != maiornumero:
            segundomaior = num
    
    print(f"O segundo maior número existente na lista é: {segundomaior}")



print ("Este código diz respeito à análise de uma lista pré-estabelecida, onde o objetivo é informar o segundo maior número contido nela.\n")
doisMaiores(numeros)