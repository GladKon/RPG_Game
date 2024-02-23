import requests
import json


def check_users(login, password):
    try:
        d = {'name': login, 'password': password}
        data = requests.post('http://127.0.0.1:5000/input', data=d)
        return_data = json.loads(data.text)
        if return_data == {'response': 'input', 'status': 200}:
            return 'MENU'
        else:
            return 'error'
    except requests.exceptions.ConnectionError:
        return 'error_server'

def connect_to_room(name, password, username):
    d = {'name': name, 'password': password, 'username': username}
    data = requests.post('http://127.0.0.1:5000/input_room', data=d)
    return 'GAME_ROOM' if data.status_code == 200 else 'INPUT_ROOM'

def create_a_room(name, password, max_player=15):
    d = {'name': name, 'password': password, 'limited': max_player}
    data = requests.post('http://127.0.0.1:5000/create_room', data=d)
    return 'GAME_ROOM' if data.status_code == 201 else 'CREATE_ROOM'

def get_list_of_users(name):
    data = requests.get(f'http://127.0.0.1:5000/room/{name}/get_users')
    return_data = json.loads(data.text)
    return return_data['User']