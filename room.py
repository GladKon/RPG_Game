from random import choice

import socket
import threading
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 19450))
server.listen()


class Room:
    def __init__(self, name_room, password, limited=12):
        self.id = self.generate_id()
        self.type = None
        self.name = name_room
        self.pasword = password
        self._players_in_room = []
        self.limit_of_user = limited
        treading = threading.Thread(target=self.listening_user, args=())
        treading.start()

    def generate_id(self):
        A = '1234567890!@#$%^&*"№;:?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        self.id = ''
        for i in range(30):
            self.id += choice(A)
        return self.id

    def add_user(self, user_id):
        self._players_in_room.append(user_id)

    def kick_user(self, user_id):
        self._players_in_room.remove(user_id)

    def show_user(self):
        return self._players_in_room

    def is_full(self):
        return len(self._players_in_room) == self.limit_of_user

    def listening_user(self):
        while True:
            client, a = server.accept()
            number = str(len(self._players_in_room)).encode('utf-8')
            self._players_in_room.append(client)
            client.send(number)
            treading = threading.Thread(target=self.handle_client, args=(client,))
            treading.start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024)
                data = json.loads(data.decode('utf-8'))

                data = json.dumps(data).encode('utf-8')
                for soct in self._players_in_room:
                    if soct != client:
                        soct.send(data)

            except ConnectionResetError:
                self._players_in_room.remove(client)
                client.close()
                break
