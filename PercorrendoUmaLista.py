listaUsuario = []

def percorrerLista(lista):
    print ("\n\nAqui estão os elementos da sua lista:")
    for item in lista:
        print(item)


def montarLista():
    print("OLÁ! SEJA BEM-VINDO AO CRIADOR DE LISTA.\n")
    print("- Digite os elementos da lista.\n- Digite 'fim' para encerrar.")
    
    while True:
        entrada = input("→ ")
        if entrada.lower() == 'fim':
            break
        listaUsuario.append(entrada)
    
    return listaUsuario

montarLista()
percorrerLista(listaUsuario)