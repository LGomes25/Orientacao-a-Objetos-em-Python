class Estudante:
    escola = "DIO"                          # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome                    # Atributos de instancia
        self.matricula = matricula
    
    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Instanciando objetos
aluno1 = Estudante("Bernardo", 1)
aluno2 = Estudante("Romulado", 2)
mostrar_valores(aluno1, aluno2)

# Alterando um atributo de uma instancia
aluno1.matricula = 56

# Alterando um atributo de uma classe
Estudante.escola = "IFF"

# Novo objeto instanciado com atributo de classe modificado
aluno3 = Estudante('Cunhado',3)

mostrar_valores(aluno1, aluno2, aluno3)