import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player('Chris', 'rock')
        self.player2 = Player('Edward', 'scissors')
        self.game = Game(self.player1, self.player2)

    def test_game_player(self):
        self.assertEqual('Edward', self.game.player2.name)
        self.assertEqual('rock', self.game.player1.selection)

    def test_game_winner_rock_vs_scissors(self):
        self.assertEqual('Chris', self.game.check_winner(self.game))

    def test_game_winner_rock_vs_paper(self):
        self.player3 = Player('James', 'rock')
        self.player4 = Player('Tim', 'paper' )
        self.game = Game(self.player3, self.player4)
        self.assertEqual('Tim', self.game.check_winner(self.game))

    def test_game_winner_paper_vs_scissors(self):
        self.player1 = Player('Chris', 'paper')
        self.player2 = Player('Edward', 'scissors')
        self.game = Game(self.player1, self.player2)
        self.assertEqual('Edward', self.game.check_winner(self.game))

    def test_game_winner_draw(self):
        self.player1 = Player('Billy', 'paper')
        self.player2 = Player('Bob', 'paper')
        self.game = Game(self.player1, self.player2)
        self.assertEqual(None, self.game.check_winner(self.game))