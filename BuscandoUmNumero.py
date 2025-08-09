def temOuNao(lista, numero):
    
    if numero in lista:
        return True    
    
    else:
        return False


numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

numeroUsuario = int(input("Digite um número INTEIRO para a busca:\n→ "))

print(temOuNao(numeros, numeroUsuario))
