personagens = [
{"Nome": "Thor", "Habilidades": "Força e Dignidade" , "Armamento": "Martelo"},
{"Nome": "Capitão América", "Habilidades": "Liderança e Defesa Pessoal", "Armamento": "Escudo"},
{"Nome": "Gavião Arqueiro", "Habilidades": "Mira e Precisão", "Armamento": "Arco e Flechas"},
{"Nome": "Homem de Ferro", "Habilidades": "Grana e Vôo", "Armamento": "Armadura"},
{"Nome": "Pantera Negra", "Habilidades": "Instintos e Caça", "Armamento": "Vibranium"}
]

def nomes(lista):
    for personagem in lista:
        print ("-", personagem["Nome"])

print("Código criado com uma função que escreve apenas a característica 'nome' dos personagens.\nSegue abaixo os nomes:")
nomes(personagens)
