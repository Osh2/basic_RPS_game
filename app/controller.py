from app import app
from flask import render_template, request
from app.models.game import *
from app.models.player import Player
from app.models.player_list import game

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/add_player', methods = ['POST'])
def add_player():
    player1_name = request.form['name']
    player1_selection = request.form['selector']
    player1 = Player(player1_name, player1_selection)
    player2 = Player('place', 'holder')
    game = Game(player1, player2)
    return render_template('add_player1.html', game= game)

@app.route('/add_player2_get_results', methods = ['POST'])
def add_player2():
    player2_name = request.form['name']
    player2_selection = request.form['selector']
    player2 = Player(player2_name, player2_selection)
    player1 = Player(player1_name, player1_selection)
    game = Game(player1, player2)
    winner = game.check_winner(game)
    return render_template('result.html', game = game, winner = winner)

@app.route('/result')
def result():
    return render_template('result.html', game = game)


    #  # take data from form
    # task_title = request.form["title"]
    # task_description = request.form["description"]
   
    # # make a new instance of a task using the data as constructor values
    # task = Task(task_title, task_description, False)
   
    # # add that new task object to the tasks list
    # add_new_task(task)
    # return redirect('/')