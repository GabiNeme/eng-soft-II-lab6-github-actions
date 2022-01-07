# Classe onde é armazenado o valor de uma célula da matriz
# ex: 11_ ou 46\ ou 35|
class Celula():
  # inicia a célula com 0 e sem ponteiro
  def __init__(self, col):
    self.valor = 0
    if col == 0:
      self.ponteiro = "|"
    else:
      self.ponteiro = "_"


  # ao utilizar a função 'print', imprime o que foi definido aqui
  def __str__(self):
    return str(self.valor)+str(self.ponteiro)