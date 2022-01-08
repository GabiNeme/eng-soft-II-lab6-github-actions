from unittest import TestCase

from main import needleman_wunsch

class Test_needleman_wunsch(TestCase):

    def test_alinhamento_sequencias_iguais(self):
        v = "AGTCA"

        m = needleman_wunsch(v,v)
        alin_v, alin_w = m.gera_alinhamento()

        self.assertEqual(alin_v, v)
        self.assertEqual(alin_w, v)

    def test_pontuacao_alinnhamentos_iguais(self):
        v = "DRQT"

        m = needleman_wunsch(v,v)
        
        self.assertEqual(m.matriz[4][4].valor , 21)
        self.assertEqual(m.matriz[4][4].ponteiro , "\\")

    def test_alinhamento_sequencias_diferentes(self):
        v = "DRQTAQAAGTTTIT"
        w = "DRNTAQLLGTDTT"
        m = needleman_wunsch(v,w)
        alin_v, alin_w = m.gera_alinhamento()

        self.assertEqual(alin_v, "DRQTAQ--AAGT-TTIT")
        self.assertEqual(alin_w, "DRNTAQLL--GTD-T-T")

    def test_pontuacao_sequencias_diferentes(self):
        v = "DRQTAQAAGTTTIT"
        w = "DRNTAQLLGTDTT"
        m = needleman_wunsch(v,w)
        
        self.assertEqual(m.matriz[13][14].valor , 46)
        self.assertEqual(m.matriz[13][14].ponteiro , "\\")