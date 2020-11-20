class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def check_winner(self, game):
        if self.player1.selection == 'rock' and self.player2.selection == 'paper':
            return f'{self.player1.name} wins!'
        elif self.player1.selection == 'rock' and self.player2.selection == 'scissors':
            return f'{self.player2.name} wins!'
        elif self.player1.selection == self.player2.selection:
            return "DRAW"
        else: 
            return None   