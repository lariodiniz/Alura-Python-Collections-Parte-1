idades = [39, 30, 27, 18, 15]
print('Lista:', idades)

print('Verifica se tem um elemento dentro de uma lista')
print('28 esta na lista?',28 in idades)
print('15 esta na lista?',15 in idades)

print('Removendo um elemento se ele esta dentro da lista (Removendo o elemento 15)')
if 15 in idades:
    idades.remove(15)
print('15 esta em idades?',15 in idades)

print('Inserir um item em uma posição (inserindo o numero 15 na posição 0)')
idades.insert(0,15)
print('Lista:', idades)

print('adiciona no final da lista varios itens')
idades.extend([27,19])
print('Lista:', idades)

print('Criando uma lista a partir de uma outra lista (list comprehension')
nova_lista = [(idade+1) for idade in idades]
print('Nova lista:', nova_lista)


print('Criando uma lista a partir de uma outra lista filtrando')
nova_lista2 = [(idade) for idade in idades if idade > 21]
print('Nova lista 2:', nova_lista2)
