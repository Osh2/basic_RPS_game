import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player('Chris', 'rock')
        
        
    def test_player_has_name(self):
        self.assertEqual('Chris', self.player1.name)

    def test_player_has_selection(self):
        self.assertEqual('rock', self.player1.selection)