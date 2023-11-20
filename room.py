from random import choice


class Room:
    def __init__(self):
        self.id = self.generate_id()
        self.type = None
        self.name = ""
        self.pasword = ''
        self._players_in_room = []
        self.limit_of_user = 12

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
