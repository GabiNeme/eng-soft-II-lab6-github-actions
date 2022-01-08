from matriz_pontuacao import Matriz_pontuacao
from blossum import BLOSSUM

# parâmetros
PENALIDADE_GAP = 0



# Algoritmo de Needleman-Wuncsh, recebe duas sequências
# e imprime a matriz de pontuações e o alinhamento obtido
def needleman_wunsch(seq_v, seq_w):

  # Devemos adicionar '*' no início de cada sequência
  lin = len(seq_w) + 1
  col = len(seq_v) + 1

  # cria matriz de pontuação zerada
  m = Matriz_pontuacao(seq_v, seq_w)

  # percorre cada linha e coluna calculando seus valores
  for i in range(1, lin):
    for j in range(1, col):
      calcula_e_atribui_maximo(m, i, j)
  
  return m


# Calcula o valor de uma nova célula, descobrindo
# qual o máximo (diagonal, cima, esquerda)

def calcula_e_atribui_maximo(m, lin, col):
  caracter_v = m.seq_v[col] # obtém caracter v
  caracter_w = m.seq_w[lin] # obtém caracter w

  # obtém os valores da diagonal (blossum), cima e baixo
  blossum = BLOSSUM()
  diagonal = m.matriz[lin-1][col-1].valor + blossum.pontuacao(caracter_v, caracter_w)
  cima = m.matriz[lin-1][col].valor + PENALIDADE_GAP
  esq = m.matriz[lin][col-1].valor + PENALIDADE_GAP

  # descobre qual o maior e atribui novo valor à matriz
  if diagonal >= cima and diagonal >= esq:
    m.matriz[lin][col].valor = diagonal
    m.matriz[lin][col].ponteiro = "\\"
  elif esq >= cima:
    m.matriz[lin][col].valor = esq
    m.matriz[lin][col].ponteiro = "_"
  else:
    m.matriz[lin][col].valor = cima
    m.matriz[lin][col].ponteiro = "|"


if __name__ == "__main__":
  v = "DRQTAQAAGTTTIT"
  w = "DRNTAQLLGTDTT"

  needleman_wunsch(v, w)