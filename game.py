
class Game:
    def __init__(self):
        self.board = [["","",""],["","",""],["","",""]]

    def play(self,s,x,y):
        self.board[x][y] = s

    def get_pos(self,x,y):
        return self.board[x][y]

    def check_row(self,x):
        return (self.board[x][0] == self.board[x][1]) and (self.board[x][1] == self.board[x][2]) and (self.board[x][0]!='') 

    def check_column(self,y):
        return (self.board[0][y] == self.board[1][y]) and (self.board[1][y]== self.board[2][y]) and (self.board[0][y]!='')

    
    def check_diagonales(self):
        if (self.board[1][1]!=''):
            return (len(set([self.board[i][i] for i in range(0,3)]))==1) or (len(set([self.board[i][2-i] for i in range(0,3)]))==1) 
        else:
            return False
