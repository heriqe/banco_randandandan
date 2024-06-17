<<<<<<< HEAD
from utils import Utils
from caixinha import Caixinha

class ContaCorrente:
    def __init__(self, cliente, deposito_inicial=0):
        self.__cliente = cliente
        self.__saldo = deposito_inicial
        self.__caixinhas = {}

        self.__caixinhas['reserva'] = Caixinha(self.__cliente, 'Reserva de Emergência', 0)

    def depositar(self, valor_deposito):
        self.__saldo += valor_deposito

    def sacar(self, valor_saque):
        self.__saldo -= valor_saque

    def get_saldo(self):
        return self.__saldo

    def criar_caixinha(self, nome_caixinha, valor_deposito):
        primeira_palavra = Utils().pegar_primeira_palavra(nome_caixinha)
        chave_caixinha = primeira_palavra.lower()

        self.__caixinhas[chave_caixinha] = Caixinha(self.__cliente, nome_caixinha, valor_deposito)

    def deletar_caixinha(self, chave_caixinha):
        caixinha = self.__caixinhas[chave_caixinha]

        if caixinha.get_saldo() == 0:
            del self.__caixinhas[chave_caixinha]

    def get_caixinhas(self):
        return self.__caixinhas

    def salvar(self, chave_caixinha, valor_deposito):
        if valor_deposito > self.__saldo:
            return 'Saldo insuficiente'
        else:
            self.__caixinhas[chave_caixinha].depositar(valor_deposito)

    def retirar(self, chave_caixinha, valor_retirada):
        caixinha = self.__caixinhas[chave_caixinha]
        if valor_retirada > caixinha.get_saldo():
            return 'Saldo de caixinha insuficiente para retirada'
        else:
            self.__caixinhas[chave_caixinha].sacar(valor_retirada)
=======
class ContaCorrente():
    def __init__(self, nome_cliente, saldo_inicial = 0):
        self.__nome = nome_cliente
        self.__saldo = saldo_inicial

    def depositar(self, valor_deposito):
        self.__saldo = self.__saldo + 1

    def sacar(self, valor_saque):
        self.__saldo = self.__saldo - valor_saque

    def get_saldo(self):
        return self.__saldo
    
    def get_nome(self):
        return self.__nome
>>>>>>> 555536b47aaaca1139e2878b7a629442d55ae91d
