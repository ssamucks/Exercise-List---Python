numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def listaVazia(lista):
    if len(lista)==0:
        return True
    else: 
        return False 

print ("\nEste código diz respeito à análise de uma lista pré-estabelecida, com o objetivo de mostrar 'True' se a lista estiver vazia, e 'False' caso contrário.")
print (f"\nA lista está vazia: {listaVazia(numeros)}.\n")
