# Por convenção, todo atributo ou método que comece com _xxx fica reconhecido como privado, assim não é recoemndado acesso direto. Python não faz bloquei direto como em C# ou Java.
# Para o exemplo abaixo, _saldo é um atributo privado e só deve ser acessado por método próprio.

class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo 
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        #...regras
        self._saldo += valor
    
    def sacar(self, valor):
        #...regras
        self._saldo -= valor
    
    def mostrar_saldo(self):
        #...regras
        return self._saldo

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


conta = Conta("0001", 100)
conta.depositar(200)
print(conta.numero_agencia)
print(conta.mostrar_saldo())
