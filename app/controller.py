from app import app
from flask import render_template, request
from app.models.game import Game
from app.models.player import Player
from app.models.player_list import game

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/player1')
def player1_selected():
    return render_template('player1_selected.html', game= game)

@app.route('/result')
def result():
    return render_template('result.html', game = game)