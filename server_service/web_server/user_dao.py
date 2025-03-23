import bcrypt
from flask import session
from sqlalchemy.orm import sessionmaker

from db.models import Character, CharacterType, User, Room


class UserDAO:
    def __init__(self, engine):
        self.engine = engine
        self.session = sessionmaker(bind=self.engine)

    def add_user(self, username, password):
        try:
            password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=5)).decode('utf-8')
            session = self.session()

            user = User(username=username, password_hash=hashed_password)
            session.add(user)
            session.commit()
        finally:
            session.close()

    def delete_user(self, username):
        try:
            session = self.session()
            user = session.query(User).filter_by(username=username).first()

            if user:
                session.delete(user)
                session.commit()
        finally:
            session.close()

    def is_exist(self, username):
        try:
            session = self.session()
            user = session.query(User).filter_by(username=username).first()
            return user is not None
        finally:
            session.close()

    def validate_user(self, username, password):
        session = self.session()
        try:
            user = session.query(User).filter_by(username=username).first()
            if user:
                stored_password = user.password_hash
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
            return False
        finally:
            session.close()

    def get_id(self, username):
        try:
            session = self.session()
            user = session.query(User).filter_by(username=username).first()
            if user:
                return user.id
            return None
        finally:
            session.close()

    def add_character_type(self, main_type, type_name):
        try:
            session = self.session()
            character_type = CharacterType(main_type=main_type, type_name=type_name)
            session.add(character_type)
            session.commit()
        finally:
            session.close()

    def add_character(self, user_id, character_name):
        try:
            session = self.session()

            character_type = session.query(CharacterType).filter_by(type_name=character_name).first()

            if character_type:
                character = Character(user_id=user_id, character_type_id=character_type.id, character_name=character_name)
                session.add(character)
                session.commit()
        finally:
            session.close()

    def add_room(self, name_of_room: str, password_of_room: str, active: bool, creater: int, type: str, limited: int):
        try:
            session = self.session()

            room = Room(name_of_room=name_of_room, password_of_room=password_of_room, active=active, creater_id=creater,
                        type=type, limited=limited)
            session.add(room)
            session.commit()
        finally:
            session.close()

    def delete_room(self, name_of_room: str):
        try:
            session = self.session()
            room = session.query(Room).filter_by(name_of_room=name_of_room).first()

            if room:
                session.delete(room)
            session.commit()
        finally:
            session.close()


if __name__ == '__main__':
    from db.models import engine

    userdao = UserDAO(engine=engine)
    userdao.add_user('2','2')
