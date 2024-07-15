
################################################# Interface das transações ######################################################################
from abc import ABC, abstractmethod

class Transacao(ABC):
    def __init__(self, valor, historicos=''):
        self._valor = valor
        self._historicos = historicos
    
    @abstractmethod
    def sacar(self, valor, historicos=''):
        historicos += f'Ocorreu um saque no valor de R${valor:.2f}'
        historico = Historico(historicos)
        historico.adicionar_historico(historicos)
        return True if self._saldo > valor else False
   
    @abstractmethod
    def depositar(self, valor, historicos=''):
        historicos += f'Ocorreu um saque no valor de R${valor:.2f}'
        historico = Historico(historicos)
        historico.adicionar_historico(historicos)        
        return True if valor > 0 else False

################################################# Cliente ######################################################################
class Cliente:
    def __init__(self, endereco, contas):
        self._contas = contas
        self._endereco = endereco

    def criar_conta(self):
        return 'Sua conta foi criada com sucesso!'

 ################################################# Pessoa Fisica ######################################################################       
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"{__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
        
################################################# CONTA ######################################################################
class Conta(Transacao):
    def __init__(self, saldo, numero, agencia, cliente, historico=''):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def ver_saldo(self):
        return self._saldo 
    
    def nova_conta(self):
        return f'A conta foi criada em nome de {self._cliente}\nO número da conta é: {self._numero}'
    
    def sacar(self, valor, historicos=''):
      historicos += f'Ocorreu um saque no valor de R${valor:.2f}'
      historico = Historico(historicos)
      historico.adicionar_historico(historicos)
      return True if self._saldo > valor else False
    
    def depositar(self, valor, historicos=''):
      historicos += f'Ocorreu um saque no valor de R${valor:.2f}'
      historico = Historico(historicos)
      historico.adicionar_historico(historicos)        
      return True if valor > 0 else False
    
################################################# CONTA CORRENTE ######################################################################
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, n_saques=0, LIMITE_SAQUES = 3):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = LIMITE_SAQUES
        self._n_saques = n_saques

    def sacar(self, valor):
      self._n_saques += 1
      return True if self._saldo > valor and self._n_saques <= self._limite_saques else False
    
################################################# Histórico ######################################################################
class Historico:
    def __init__(self, transacao):
        self._transacao = transacao


    def adicionar_historico(self, transacao):
        historico = '########### Historico ###########' 
        historico += f'\n{transacao}'
    