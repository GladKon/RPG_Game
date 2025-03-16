import bcrypt
from sqlalchemy.orm import sessionmaker

from db.models import Character, CharacterType, User, Room


class UserDAO:
    def __init__(self, engine):
        self.engine = engine
        self.session = sessionmaker(bind=self.engine)

    def add_user(self, username, password):
        password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=5)).decode('utf-8')
        session = self.session()

        user = User(username=username, password_hash=hashed_password)
        session.add(user)
        session.commit()

    def delete_user(self, username):
        session = self.session()
        user = session.query(User).filter_by(username=username).first()

        if user:
            session.delete(user)
            session.commit()

    def is_exist(self, username):
        session = self.session()
        user = session.query(User).filter_by(username=username).first()
        return user is not None

    def validate_user(self, username, password):
        session = self.session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            stored_password = user.password_hash
            return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
        return False

    def get_id(self, username):
        session = self.session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            return user.id
        return None

    def add_character_type(self, main_type, type_name):
        session = self.session()
        character_type = CharacterType(main_type=main_type, type_name=type_name)
        session.add(character_type)
        session.commit()

    def add_character(self, user_id, character_name):
        session = self.session()

        character_type = session.query(CharacterType).filter_by(type_name=character_name).first()

        if character_type:
            character = Character(user_id=user_id, character_type_id=character_type.id, character_name=character_name)
            session.add(character)
            session.commit()

    def add_room(self, name_of_room: str, password_of_room: str, active: bool, creater: int, type: str, limited: int):
        session = self.session()

        room = Room(name_of_room=name_of_room, password_of_room=password_of_room, active=active, creater_id=creater,
                    type=type, limited=limited)
        session.add(room)
        session.commit()

    def delete_room(self, name_of_room: str):
        session = self.session()
        room = session.query(Room).filter_by(name_of_room=name_of_room).first()

        if room:
            session.delete(room)
            session.commit()


if __name__ == '__main__':
    from db.models import engine

    userdao = UserDAO(engine=engine)
    # userdao.add_room('1', '2', True, 2, '4')
    # userdao.delete_room('1')
    # userdao.add_character(1, 1, 'Mage')
    # userdao.add_character_type('Archer', 'Sniper')
    # userdao.drop_table_character_types()
    # userdao.create_table_characters()
    # userdao.create_table_character_types()
    # userdao.create_table_users()
    # userdao.add_user('1','1')
    userdao.add_user('2','2')
