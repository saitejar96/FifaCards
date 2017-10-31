#!flask/bin/python
from flask import Flask,jsonify,request
from random import randint

app = Flask(__name__)

game = {}
cards=[]
num_players=0

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/creategame', methods=['POST'])
def create_game():
	global game
	global num_players
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

    game = {
        'players': request.json['players']
        'turn': 0
    }
    return jsonify({'task': "done"}), 201

if __name__ == '__main__':
    app.run(debug=True)