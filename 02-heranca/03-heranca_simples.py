class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor")

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# instanciando por heranca de veiculo
moto = Motocicleta("preta", "kkk-6789", 2)
carro = Carro('Branco', "lkj-7890", 4)

# instanciando por heranca de veiculo + atributo de caminhão: carregando
caminhao = Caminhao('Roxo', 'asd-2345', 12, True)

# metodos herdados de veiculo
moto.ligar_motor()
carro.ligar_motor()
caminhao.ligar_motor()

# metodo exclusivo de caminhao
caminhao.esta_carregado()
print(caminhao)
print(carro)
print(moto)