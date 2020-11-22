from app.models.player import Player
from app.models.game import Game

# player1 = Player('Chris', 'rock')
# player2 = Player('Edward', 'scissors')

# game = Game(player1, player2)

players = []

def add_player(player1):
    players.append(player1)

def clear_players(players):
    players.clear()