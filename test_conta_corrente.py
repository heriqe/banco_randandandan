import unittest
from conta_corrente import ContaCorrente
from cliente import Cliente

class TesteContaCorrent(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.__cliente = Cliente('John Doe', 25, 0)
        self.__conta_corrente = ContaCorrente(self.__cliente, 0)

    def get_saldo(self):
        self.assertTrue(False)

    def test_depositar(self):
        self.assertTrue(False)

    def test_sacar(self):
        self.assertTrue(False)

    def test_sacar(self):
        self.assertTrue(False)

    def test_criar_caixinha(self):
        self.assertTrue(False)

    def test_get_caixinhas(self):
        self.assertTrue(False)

    def test_sacar(self):
        self.assertTrue(False)
    