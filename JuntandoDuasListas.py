def concatenacao(lista1, lista2):
    concatenada = lista1 + lista2
    unicos = []
    for item in concatenada:
        if item not in unicos:
            unicos.append(item)
    return unicos

print ("\nEste código tem como finalidade receber duas listas diferentes, e exibir a concatenação das mesmas.")

print("\nDigite sua PRIMEIRA lista (digite 'fim' para encerrar):")
lista1 = []
while True:
    valor = input("- ")
    if valor.lower() == "fim":
        break
    lista1.append(valor)

print("\nDigite sua SEGUNDA lista (digite 'fim' para encerrar):")
lista2 = []
while True:
    valor = input("- ")
    if valor.lower() == "fim":
        break
    lista2.append(valor)

print(f"\nA lista concatenada ficou: {concatenacao(lista1, lista2)}\n")
