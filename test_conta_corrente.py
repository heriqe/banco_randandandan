import unittest
from conta_corrente import ContaCorrente

<<<<<<< HEAD
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
=======
class TesteContaCorrent(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    # Testa pegar nome
    def test_get_nome(self):
        nome_teste = 'Gabriel'
        conta_corrente = ContaCorrente(nome_teste)

        self.assertTrue(nome_teste == conta_corrente.get_nome())
>>>>>>> 555536b47aaaca1139e2878b7a629442d55ae91d

    # Testa saldo R$ 0,00 (zero) quando criar conta_corrente
    def test_default_saldo_on_init(self):
        conta_corrente = ContaCorrente()

        self.assertTrue(conta_corrente == 0)

    # Testa saldo inicial quando criar conta_corrente
    def test_saldo_on_init(self):
        saldo_inicial_teste = '100'
        nome_teste = 'Carol'
        conta_corrente = ContaCorrente(nome_teste)

        self.assertTrue(saldo_inicial_teste == conta_corrente.get_saldo())

    # Testa depositar
    def test_sacar(self):
<<<<<<< HEAD
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
=======
        valor_deposito_teste = '300'
        nome_teste = 'John Doe'
        conta_corrente = ContaCorrente(nome_teste)
        conta_corrente.depositar(valor_deposito_teste)

        self.assertTrue(valor_deposito_teste == conta_corrente.get_saldo())

    # Testa sacar
    def test_sacar(self):
        
        self.assertTrue(False)
    
>>>>>>> 555536b47aaaca1139e2878b7a629442d55ae91d
