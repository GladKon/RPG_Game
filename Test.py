from flask import Flask, request, jsonify

from RPG_Game.structure.bssa_data import add_user, is_exist, validate_user
from RPG_Game.structure.room import Room, rooms


app = Flask(__name__)



@app.route('/')
def func1():
    return 'Привет!'


@app.route('/registration', methods=['POST'])
def registration():
    username = request.form['name']
    password = request.form['password']

    if is_exist(username):
        return jsonify({'response': 'Aleready exist', 'status': 409})
    else:
        add_user(username, password)
        return jsonify({'response': 'create', 'status': 201})


@app.route('/input', methods=['POST'])
def input():
    username = request.form['name']
    password = request.form['password']
    if validate_user(username, password):
        return jsonify({'response': 'input', 'status': 200})
    else:
        return jsonify({'response': 'exsit', 'status': 401})


@app.route('/create_room', methods=['POST'])
def create_room():
    name_room = request.form['name']
    password = request.form['password']
    limited = request.form['limited']
    r = Room(name_room, password, limited)
    rooms.append(r)
    return jsonify({'response': 'create', 'status': 201}), 201

@app.route('/input_room', methods=['POST'])
def input_room():
    name = request.form['name']
    password = request.form['password']
    for room in rooms:
        if room.name == name:
            return jsonify({'response': 'input', 'status': 200}) if room.pasword == password else jsonify({'response': 'stop', 'status': 412})
        else:
            return jsonify({'response': 'stop', 'status': 401})

app.run()
