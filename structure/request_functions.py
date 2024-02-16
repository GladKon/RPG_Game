import requests
import json


def check_user(login, password):
    d = {'name': login, 'password': password}
    data = requests.post('http://127.0.0.1:5002/input', data=d)
    return_data = json.loads(data.text)
    if return_data == {'response': 'input', 'status': 200}:
        return 'MENU'
    else:
        return 'error'


def input_room_req(name, password, username):
    d = {'name': name, 'password': password, 'user': username}
    data = requests.post('http://127.0.0.1:5002/input_room', data=d)
    return 'GAME_ROOM' if data.status_code == 200 else 'INPUT_ROOM'


def create_room_req(name, password, max_player=15):
    d = {'name': name, 'password': password, 'limited': max_player}
    data = requests.post('http://127.0.0.1:5002/create_room', data=d)
    return 'GAME_ROOM' if data.status_code == 201 else 'CREATE_ROOM'

