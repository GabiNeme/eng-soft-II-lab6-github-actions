from celula import Celula

# Classe que armazena a matriz de pontuação
class Matriz_pontuacao():

    # inicia a matriz com zeros em todas as células
    def __init__(self, seq_v, seq_w):
        # salva as sequências v e w e adiciona um * no início
        self.seq_v = "*" + seq_v
        self.seq_w = "*" +  seq_w

        self.linhas = len(seq_w) + 1
        self.colunas = len(seq_v) + 1

        # cria a matriz zerada
        self.matriz = []
        for i in range(self.linhas):
            line = []
            for j in range(self.colunas):
                line.append(Celula(j))
            self.matriz.append(line)
    
    # imprime a matriz (basta usar print(m))
    def __str__(self):
        print_str="w\\v\t"
        for j in range(self.colunas):
            print_str += self.seq_v[j] + "\t"
            print_str += "\n"  
        for i in range(self.linhas):
            print_str += self.seq_w[i] + "\t"
            for j in range(self.colunas):
                print_str += str(self.matriz[i][j]) + "\t"
                print_str += "\n"
        return print_str

    def gera_alinhamento(self):
        # alinhamentos começam zerados
        alinh_v = "" 
        alinh_w = ""

        # começa do fim da matriz
        lin = self.linhas - 1
        col = self.colunas - 1

        # enquanto não chegar ao início
        while lin != 0 or col != 0:
            if self.matriz[lin][col].ponteiro == "\\": # diagonal
                alinh_v = self.seq_v[col] + alinh_v
                alinh_w = self.seq_w[lin] + alinh_w
                lin -= 1
                col -= 1
            elif self.matriz[lin][col].ponteiro == "_": # esquerda
                alinh_v = self.seq_v[col] + alinh_v
                alinh_w = "-" + alinh_w
                col -= 1
            elif self.matriz[lin][col].ponteiro == "|": # cima
                alinh_v = "-" + alinh_v
                alinh_w = self.seq_w[lin] + alinh_w
                lin -= 1
        
        # imprime alinhamentos
        print(alinh_v)
        print(alinh_w)