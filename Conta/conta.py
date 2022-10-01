class Conta:
    def __init__(self, titular, ag, conta, saldo, limite):
        self.titular = titular
        self.ag = ag
        self.conta = conta
        self.saldo = saldo
        self.limite = limite

    def verificarSaldo(self):
        print(f'Titular: {self.titular}\n'f'Saldo: {self.saldo}')

    def sacar(self, valor):
        if valor > self.limite:
             print("Limite Ultrapassado")
        else:
             self.saldo = self.saldo - valor

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def transferir(self, valor, destino):
        if valor > self.saldo:
            print("Saldo Insuficiente")
        else:
            self.sacar(valor)
            destino.depositar(valor)




