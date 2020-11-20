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

    def test_game_has_winner(self):
        self.game1 = Game(self.player1, self.player2)
        self.assertEqual('Edward wins!', self.game.check_winner(self.game1))