class Pessoa:
    def __init__(self, nome, idade, estadoCivil):
         self.nome = nome
         self.idade = idade
         self.estadoCivil = estadoCivil

    def aumentaridade(self):
        self.idade = self.idade + 1

    def exibirdados(self):
        print(f'Nome:{self.nome} \n'
              f'Idade: {self.idade} \n'
              f'Estado Civil:{self.estadoCivil} \n'
              f'_____________________________')
    def mudarEstadoCivil(self, ec):
        if self.estadoCivil == 'casado':
           print(f'{self.nome} já é casado(a)')
        self.estadoCivil = ec

