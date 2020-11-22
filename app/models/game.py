class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def check_winner(self, game):
        if self.player1.selection == 'rock' and self.player2.selection == 'scissors':
            return self.player1
        elif self.player1.selection == 'rock' and self.player2.selection == 'paper':
            return self.player2
        elif self.player1.selection == 'scissors' and self.player2.selection == 'rock':
            return self.player2
        elif self.player1.selection == 'scissors' and self.player2.selection =='paper':
            return self.player1
        elif self.player1.selection == 'paper' and self.player2.selection == 'scissors':
            return self.player2
        elif self.player1.selection == 'paper' and self.player2.selection == 'rock':
            return self.player2
        elif self.player1.selection == self.player2.selection:
            return None  