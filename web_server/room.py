from random import choice, randint
from users import User

import socket
import threading
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 19451))
server.listen()


class Room:
    def __init__(self, name_room, password, limited=12):
        self._start = False
        self.id = self.generate_id()
        self.type = None
        self.name = name_room
        self.pasword = password
        self._players_in_room = []
        self.limit_of_user = limited

    def generate_id(self):
        A = '1234567890!@#$%^&*"№;:?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        self.id = ''
        for i in range(30):
            self.id += choice(A)
        return self.id

    def add_user(self, user):
        self._players_in_room.append(user)

    def get_amount(self):
        return len(self._players_in_room)

    def kick_user(self, user_id):
        self._players_in_room.remove(user_id)

    def show_user(self):
        return self._players_in_room

    def get_names(self):
        names = []

        for u in self._players_in_room:
            names.append(u.name)

        return names

    def is_full(self):
        return len(self._players_in_room) == self.limit_of_user

    def start(self):
        d = {}
        for user in self._players_in_room:
            d[user.number] = randint(30, 300), randint(30, 300)

        for user in self._players_in_room:
            user.socket.send(json.dumps(d).encode('utf-8'))

            t = threading.Thread(target=self.handle_client, args=(user.socket,))
            t.start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024)
                data = json.loads(data.decode('utf-8'))

                data = json.dumps(data).encode('utf-8')
                for user in self._players_in_room:
                    if user.socket != client:
                        user.socket.send(data)

            except ConnectionResetError:
                self._players_in_room.remove(client)
                client.close()
                break

    def start_game(self):
        self._start = True


rooms = []


def listening_user():
    while True:
        client, a = server.accept()
        data = json.loads(client.recv(1024).decode('utf-8'))
        for room in rooms:
            if room.name == data['name_of_room']:
                number = str(room.get_amount()).encode('utf-8')
                user = User(data['name'], client, str(room.get_amount()))
                room.add_user(user)
                client.send(number)


treading = threading.Thread(target=listening_user, args=())
treading.start()
