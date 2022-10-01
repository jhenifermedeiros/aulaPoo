from conta import Conta

c1 = Conta('Jhenifer', 1002, 1, 10000, 10000)
c2 = Conta('Matheus', 1004, 1, 1500, 2000)

c1.transferir(1200, c2)
c1.verificarSaldo()
c2.verificarSaldo()
