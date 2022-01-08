from unittest import TestCase
from celula import Celula

class Test_celula(TestCase):

    def test_celula_comeca_zerada(self):
        celula = Celula(0)
        self.assertEqual(celula.valor, 0)

    
    def test_ponteiro_vertical_na_primeira_coluna(self):
        celula = Celula(0)
        self.assertEqual(celula.ponteiro, "|")

    def test_ponteiro_horizontal_fora_da_primeira_coluna(self):
        celula = Celula(4)
        self.assertEqual(celula.ponteiro, "_")

