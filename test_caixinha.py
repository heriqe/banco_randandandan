import unittest
from caixinha import Caixinha
from cliente import Cliente

class TesteCaixinha(unittest.TestCase):

    def setUp(self):
        self.__cliente = Cliente('John Doe', 25, 0)

    def test_get_nome(self):
        nome = 'Moto randandandan'
        caixinha = Caixinha(self.__cliente, nome, 100)
        self.assertEqual(caixinha.get_nome(), nome)

    def test_depositar(self):
        valor_inicial = 100
        valor_deposito = 200
        caixinha = Caixinha(self.__cliente, 'Carro', valor_inicial)
        caixinha.depositar(valor_deposito)
        valor_esperado = valor_inicial + valor_deposito
        self.assertEqual(caixinha.get_saldo(), valor_esperado)

    def test_sacar(self):
        caixinha = Caixinha(self.__cliente, 'Carro', 20)
        caixinha.sacar(200)
        self.assertEqual(caixinha.get_saldo(), 0)

if __name__ == '__main__':
    unittest.main()
