"""
idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)
"""

idades = [39, 30, 27, 18]
print(idades)

print('Tamanho da lista')
tamanho_lista = len(idades)
print(tamanho_lista)

print('adiciona no final da lista um valor')
idades.append(15)
print(idades)

print('passar por todo os elementos da lista')
for idade in idades:
    print(idade)

print('Removendo um elemento')
idades.remove(30)

print(idades)

print('Remove todos os objetos de uma lista')
idades.clear()

print(idades)
