def faz_processamento_de_visualizacao(lista):
    print(len(lista))

idades = [39, 30, 27, 18, 15]
faz_processamento_de_visualizacao(idades)
print(idades)

# Ao criar uma função que recebe um objeto mutavel como parametro padrão
# é uma boa pratica usar None e verificar depois.

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
