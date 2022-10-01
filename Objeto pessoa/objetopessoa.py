from pessoa import Pessoa


p1 = Pessoa("Marcia", 40, 'casado')
p2 = Pessoa('Israel', 21, 'solteiro')
p3 = Pessoa('Pedro', 17, 'solteiro')
p4 = Pessoa('Juan', 46, 'casado')

p1.mudarEstadoCivil('casado')
p1.exibirdados()
p2.exibirdados()
p3.exibirdados()
p3.mudarEstadoCivil('casado')
p4.exibirdados()