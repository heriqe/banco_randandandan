import unittest
from conta_corrente import ContaCorrente

class TesteContaCorrent(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    # Testa pegar nome
    def test_get_nome(self):
        nome_teste = 'Gabriel'
        conta_corrente = ContaCorrente(nome_teste)

        self.assertTrue(nome_teste == conta_corrente.get_nome())

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
        valor_deposito_teste = '300'
        nome_teste = 'John Doe'
        conta_corrente = ContaCorrente(nome_teste)
        conta_corrente.depositar(valor_deposito_teste)

        self.assertTrue(valor_deposito_teste == conta_corrente.get_saldo())

    # Testa sacar
    def test_sacar(self):
        
        self.assertTrue(False)
    