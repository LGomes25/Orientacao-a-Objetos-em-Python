class Passaro:
    def voar(self):
        print("Voando...")

# Herança
class Pardal(Passaro):
    def voar(self):
        super().voar()

# Herança
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# Herança (exemplo ruim de exemplo)
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando....')

# Polimorfismo
def plano_voo(obj):
    obj.voar()

#Instanceando
pardal = Pardal()
avestruz = Avestruz()
aviao = Aviao()

# Chamando metodos
print("Pardal: ", end="")
plano_voo(pardal)
print("Avestruz: ", end="")
plano_voo(avestruz)
print("Avião: ", end="")
plano_voo(aviao)
