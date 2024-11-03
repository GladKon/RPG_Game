import sqlite3
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Character, CharacterType, User, engine


class UserDAO:
    def __init__(self, engine):
        # self.engine = create_engine(db_url)
        # Base.metadata.create_all(self.engine)
        self.engine = engine
        self.session = sessionmaker(bind=self.engine)

    def add_user(self, username, password):
        password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=5))
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
            return bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8'))
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


if __name__ == '__main__':
    userdao = UserDAO(engine=engine)
    # userdao.add_character(1, 1, 'Mage')
    # userdao.add_character_type('Archer', 'Sniper')
    # userdao.drop_table_character_types()
    # userdao.create_table_characters()
    # userdao.create_table_character_types()
    # userdao.create_table_users()
    userdao.add_user('1','1')
    # userdao.add_user('2','2')
