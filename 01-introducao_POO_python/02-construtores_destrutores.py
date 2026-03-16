class Cachorro:
    # A cada vez que é instanciado um bjeto, roda a função
    def __init__(self, nome, cor, raca, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.acordado = acordado
    
    # Remove as instancias da classe assim que o programa acaba de ser executado, limpando a memoria
    def __del__(self):
        print("Removendo a instancia da classe")
    
    def falar(self):
        print('Au-au')
    
c1 = Cachorro("Jujuba", "Caramelo", "SRD")
c2 = Cachorro("Lobão", "Preto", "Pincher")

print(f'Nome: {c1.nome} - som: ',end= "")
c1.falar()
print(f'Nome: {c2.nome} - som: ',end= "")
c2.falar()

