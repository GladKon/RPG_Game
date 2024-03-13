from flask import Flask, request, jsonify


from room import Room, rooms
from UserDAO import UserDAO

app = Flask(__name__)
user_dao = UserDAO('users.db')
user_dao.create_db()



@app.route('/registration', methods=['POST'])
def registration():
    username = request.form['name']
    password = request.form['password']

    if user_dao.is_exist(username):
        return jsonify({'response': 'Aleready exist', 'status': 409})
    else:
        user_dao.add_user(username, password)
        return jsonify({'response': 'create', 'status': 201})


@app.route('/input', methods=['POST'])
def input():
    username = request.form['name']
    password = request.form['password']
    if user_dao.validate_user(username, password):
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
    username = request.form['username']
    for room in rooms:
        if room.name == name:
            # room.add_user(username)
            return jsonify({'response': 'input', 'status': 200}) if room.pasword == password else jsonify(
                {'response': 'stop', 'status': 412})
    return jsonify({'response': 'stop', 'status': 401})


@app.route('/room/<string:name>/get_users', methods=['GET'])
def get_users(name: str):
    for room in rooms:
        if name == room.name:
            return jsonify({'Response': 'Success', 'User': room.get_names()}), 200
    return jsonify({'Response': 'Not found'}), 404


app.run()
