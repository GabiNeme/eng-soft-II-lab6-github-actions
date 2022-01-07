import requests

class BLOSSUM():

    def __init__(self):
        BLOSSUM62 = requests.get("https://raw.githubusercontent.com/carbo6ufmg/Needleman-Wunsch/main/BLOSSUM62.txt")
        BLOSSUM62 = str(BLOSSUM62.text)

        BLOSSUM62_ROWS = []
        BLOSSUM62_ROWS = BLOSSUM62.split("\n")

        self.keys = BLOSSUM62_ROWS.pop(0).split("  ")

        self.matrix = []
        for row in BLOSSUM62_ROWS:
            self.matrix.append([int(x) for x in row.split()])
        
    # Calcula a pontuação de duas proteínas
    def pontuacao(self, caracter_v, caracter_w):
        # descobre qual coluna da matriz BLOSSUM está aquela proteína
        indice_carc_v = self.keys.index(caracter_v) 
        indice_carc_w = self.keys.index(caracter_w)
        return self.matrix[indice_carc_v][indice_carc_w] # consulta matriz blossum