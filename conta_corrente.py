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