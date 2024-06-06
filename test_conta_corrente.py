import unittest
from conta_corrente import ContaCorrente
from cliente import Cliente

class TesteContaCorrente(unittest.TestCase):
    def setUp(self):
        self.__cliente = Cliente('John Doe', 25, 0)
        self.__conta_corrente = ContaCorrente(self.__cliente, 0)

    def test_get_saldo(self):
        saldo_inicial = self.__conta_corrente.get_saldo()
        self.assertEqual(saldo_inicial, 0)

    def test_depositar(self):
        valor_deposito = 100
        self.__conta_corrente.depositar(valor_deposito)
        saldo_atual = self.__conta_corrente.get_saldo()
        self.assertEqual(saldo_atual, valor_deposito)

    def test_sacar(self):
        valor_saque = 50
        self.__conta_corrente.depositar(100)
        self.__conta_corrente.sacar(valor_saque)
        saldo_atual = self.__conta_corrente.get_saldo()
        self.assertEqual(saldo_atual, 100 - valor_saque)

    def test_criar_caixinha(self):
        pass

    def test_get_caixinhas(self):
        pass

if __name__ == '__main__':
    unittest.main()
