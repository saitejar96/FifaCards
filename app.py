#!flask/bin/python
from flask import Flask,jsonify,request
from random import randint

app = Flask(__name__)

game = {}
cards=[]
num_players=0
stat_selected=False
round_winner_decided=False
ready = []

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/getgame/<int:task_id>', methods=['GET'])
def get_game(task_id):
    global game
    global num_players
    global stat_selected
    global round_winner_decided
    game_obj = {
        'turn': game['turn'],
        'card_set': game['cards_dist'][game['players'].index(task_id)],
        'stat_selected': stat_selected,
        'stat': game['stat'],
        'round_winner_decided': round_winner_decided,
        'round_winner': game['round_winner']
    }
    return jsonify({'game_obj': game_obj}),200

@app.route('/ready', methods=['POST'])	
def ready():
	global ready
    if not request.json or not 'id' in request.json:
        abort(400)
    ready[ready.index(request.json['id'])]=True
    return jsonify({'task': "done"}), 201


@app.route('/creategame', methods=['POST'])
def create_game():
	global game
	global num_players
	global ready
    if not request.json or not 'players' in request.json:
        abort(400)
    num_players = len(request.json['players'])
    for x in range(0,num_players):
    	temp=[]
        for y in range(0,int(x/num_players)):
            z = randint(0, len(cards)-1)
            temp.append(cards[z])
            cards.pop(z)
        cards_dist.append(temp)
        ready.append(False)

    game = {
        'players': request.json['players'],
        'turn': 0,
        'cards_dist': cards_dist,
        'stat': -1,
        'round_winner': -1
    }
    return jsonify({'task': "done"}), 201

if __name__ == '__main__':
    app.run(debug=True)