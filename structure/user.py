from random import choice
class User:
    def __init__(self):
        self.id = self.generate_id()

        # self.clas.image = "image"
        # self.x,self.y = 0,0
        self.Xp = 0
        # self.clas = self.clas
        self.leveling = 0
        self.lvl = 0

    def Xpereance(self, result):
        self.leveling += result

    def Lvl(self):
        self.lvl = self.leveling // 100

    def generate_id(self):
        A = '1234567890!@#$%^&*"№;:?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        self.id = ''
        for i in range(30):
            self.id += choice(A)
        return self.id

