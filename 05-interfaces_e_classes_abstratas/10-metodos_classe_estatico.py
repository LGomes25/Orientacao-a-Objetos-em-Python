class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # Metodo de classe
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    # Metodo estatico
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1980, 5, 30, "Leonardo")
print(p.nome, p.idade)
p2 = Pessoa.criar_de_data_nascimento(2022, 10, 30, "Saul")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(10))

# Apresentação melhorada
print()
print(f'É maior de idade: {'Verdadeiro' if Pessoa.e_maior_idade(p.idade) else 'Falso'}')
print(f'É maior de idade: {'Verdadeiro' if Pessoa.e_maior_idade(p2.idade) else 'Falso'}')