from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

engine = create_engine('postgresql://GladKon:546372819r@localhost:15432/rpggame_db')

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password_hash = Column(String(220), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    characters = relationship("Character", back_populates="user")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=True)
    character_type_id = Column(Integer, ForeignKey("character_types.id"), nullable=False)

    user = relationship("User", back_populates="characters")
    character_type = relationship("CharacterType", back_populates="character")
    room = relationship("Room", back_populates="characters")


class CharacterType(Base):
    __tablename__ = "character_types"

    id = Column(Integer, primary_key=True)
    main_type = Column(String(20), nullable=False)
    type_name = Column(String(20), nullable=False, unique=True)

    character = relationship("Character", back_populates="character_type")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    name_of_room = Column(String(20), nullable=False)
    password_of_room = Column(String(20), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    active = Column(Boolean, nullable=False)
    creater_id = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)

    characters = relationship("Character", back_populates="room")
