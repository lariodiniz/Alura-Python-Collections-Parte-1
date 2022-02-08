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

conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)