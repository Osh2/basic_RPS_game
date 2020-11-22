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
        winner = self.game.check_winner(self.game)
        self.assertEqual('Chris', winner.name)

    def test_game_winner_rock_vs_paper(self):
        self.player3 = Player('James', 'rock')
        self.player4 = Player('Tim', 'paper' )
        self.game = Game(self.player3, self.player4)
        winner = self.game.check_winner(self.game)
        self.assertEqual('Tim', winner.name)

    def test_game_winner_paper_vs_scissors(self):
        self.player1 = Player('Chris', 'paper')
        self.player2 = Player('Edward', 'scissors')
        self.game = Game(self.player1, self.player2)
        winner = self.game.check_winner(self.game)
        self.assertEqual('Edward', winner.name)

    def test_game_winner_draw(self):
        self.player1 = Player('Billy', 'paper')
        self.player2 = Player('Bob', 'paper')
        self.game = Game(self.player1, self.player2)
        winner = self.game.check_winner(self.game)
        self.assertEqual(None, winner)