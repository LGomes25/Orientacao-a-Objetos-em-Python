# importando classe/metodo abc para permitir fazer classe abstrada
from abc import ABC, abstractmethod

# herdando de ABC - abstracao da classe
class ControleRemoto(ABC):

    # abstracao dos metodos
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    # abstracao de uma propriedade
    @property
    @abstractmethod
    def marca(self):
        pass

# imposicao de implementacao dos metodos da classe abstrada por herancao
class ControleTV(ControleRemoto):
    
    def ligar(self):
        print('Ligando TV....')
        print('TV ligada')
    
    def desligar(self):
        print('Desligando TV....')
        print('TV desligada')
    
    @property
    def marca(self):
        return 'LG'

# imposicao de implementacao dos metodos da classe abstrada por herancao
class ControleArCondicionado(ControleRemoto):
    
    def ligar(self):
        print('Ligando Ar Condicionado....')
        print('Ar Condicionado ligado')
    
    def desligar(self):
        print('Desligando Ar Condicionado....')
        print('Ar Condicionado desligado')

    @property
    def marca(self):
        return 'Spring'

# Instanciando e testando 
controle = ControleTV()
print(controle.marca)
controle.ligar()
controle.desligar()
print('-'*50)
controle = ControleArCondicionado()
print(controle.marca)
controle.ligar()
controle.desligar()