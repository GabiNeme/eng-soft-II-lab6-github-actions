from unittest import TestCase
from matriz_pontuacao import Matriz_pontuacao

class Test_matriz_pontuacao(TestCase):
  


    def test_tamanho_matriz_quadrada(self):
        v = "A"
        w = "T"
        m = Matriz_pontuacao(v,w)
        self.assertEqual(len(m.matriz), 2)
        self.assertEqual(len(m.matriz[0]), 2)
        self.assertEqual(len(m.matriz[1]), 2)

    def test_tamanho_matriz_v_menor_w(self):
        v = "A"
        w = "TS"
        m = Matriz_pontuacao(v,w)
        self.assertEqual(len(m.matriz), 3)
        self.assertEqual(len(m.matriz[0]), 2)
        self.assertEqual(len(m.matriz[1]), 2)
        self.assertEqual(len(m.matriz[2]), 2)

    def test_tamanho_matriz_v_maior_w(self):
        v = "AT"
        w = "S"
        m = Matriz_pontuacao(v,w)
        self.assertEqual(len(m.matriz), 2)
        self.assertEqual(len(m.matriz[0]), 3)
        self.assertEqual(len(m.matriz[1]), 3)

    def test_matriz_comeca_zerada(self):
        v = "A"
        w = "T"
        m = Matriz_pontuacao(v,w)
        self.assertEqual(m.matriz[0][0].valor, 0)
        self.assertEqual(m.matriz[0][1].valor, 0)
        self.assertEqual(m.matriz[1][0].valor, 0)
        self.assertEqual(m.matriz[1][1].valor, 0)
