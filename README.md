# Orientação a Objetos em Python

Este módulo introduz os conceitos fundamentais da **programação orientada a objetos (POO)** aplicados em Python.  
O objetivo é compreender como estruturar programas de forma mais organizada, reutilizável e próxima da realidade dos problemas que queremos resolver.

## Conteúdo previsto
- Conceito de **classes** e **objetos**
- Diferença entre **atributos** e **métodos**
- Uso de **construtores** (`__init__`)
- Encapsulamento e visibilidade de dados
- Herança e reutilização de código
- Polimorfismo e sobrescrita de métodos
- Abstração e implementação
- Boas práticas na modelagem orientada a objetos

---

## Estrutura 

```
📂 Orientacao-a-Objetos-em-Python
├── 01-introducao_POO_python
├── 02-heranca
├── 03-encapsulamento
├── 04-polimorfismo
├── 05-interfaces_e_classes_abstratas
├── 06-sistema_bancario_POO (desafio)
└── README.md
```

---

## Desafio: Sistema Bancário em Python

Este desafio consiste na implementação de um **sistema bancário simples** em Python, utilizando funções, estruturas condicionais e listas para simular operações básicas de uma conta corrente.

### Funcionalidades
- **Depósito**: permite adicionar valores ao saldo e registrar no extrato.
- **Saque**: realiza retiradas com validações de saldo, limite por operação e limite diário de saques.
- **Extrato**: exibe todas as movimentações realizadas e o saldo atual.
- **Usuário**: possibilita criar novos usuários com dados pessoais.
- **Conta**: permite criar contas vinculadas a usuários existentes.
- **Listagem de contas**: mostra todas as contas cadastradas com seus respectivos titulares.

### Objetivo
O sistema busca reproduzir o funcionamento básico de um caixa eletrônico, garantindo regras de negócio como limite de saques e validação de usuários.  
Esse exercício reforça conceitos de:
- Estruturas de repetição e condicionais
- Funções com parâmetros posicionais e nomeados
- Manipulação de listas e dicionários
- Organização de código em blocos reutilizáveis

---

## Para rodar os arquivos no terminal

Em cada pasta do projeto:
```
    > python -i <nome_do_arquivo>
```

para sair do modo de execução python, digitar: 
```
    >>> close()
```