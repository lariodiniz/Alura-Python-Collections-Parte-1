lista = [15,8,32,65,56,32,49,57]

#ordena
print(sorted(lista))

#inverte
print(list(reversed(lista)))

#ordena invertido
print(sorted(lista, reverse=True))

print(lista)
#reverter a propria lista
lista.sort()
print(lista)

from functools import total_ordering

@total_ordering
class ContaSalario:

    def __init__(self, codigo: int) -> None:
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor: float):
        self._saldo += valor
    
    def __str__(self) -> str:
        return f'[>>Conta  {self._codigo} Sando {self._saldo}<<]'

    def __eq__(self, __o) -> bool:
        if not isinstance(__o, ContaSalario):
            return False
        return self._codigo == __o._codigo

    def __lt__(self, __o) -> bool:
        if self._saldo != __o._saldo:
            return self._saldo < __o._saldo
        return self._codigo < __o._codigo

conta1 = ContaSalario(1)
conta1.deposita(500)

conta2 = ContaSalario(2)
conta2.deposita(500)

conta3 = ContaSalario(3)
conta3.deposita(500)

contas = [conta2, conta3, conta1]

#ordenando usando função
def extrai_saldo(conta):
    #reduzindo o objeto a um objeto comparavel
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

#ordenando acessando um atributo
from operator import attrgetter
for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

#ordenando com sorted por ter o metodo __lt__ imprementado
for conta in sorted(contas):
    print(conta)

#total_ordering nos da todas as ordenações desde que tenha sido
#implementado __lt__ e __eq__
print(conta1 <= conta2)