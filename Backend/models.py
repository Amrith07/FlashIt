from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from config import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class card(db.Model):
    card_id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    deck_id = db.Column(db.Integer,ForeignKey('deck.deck_id'),nullable=False)
    key = db.Column(db.Text,nullable=False,unique=True)
    answer = db.Column(db.Text,nullable=False)
    difficulty = db.Column(db.Text,nullable=False)
    ParentDeck=relationship("deck",back_populates="cards")

    def __init__(self,p2,p3,p4,p5):
        #self.card_id = p1
        self.deck_id = p2
        self.key = p3
        self.answer = p4
        self.difficulty = p5

class deck(db.Model):
    deck_id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    deck_name = db.Column(db.Text,nullable=False)
    owner = db.Column(db.Integer,ForeignKey('user.user_id'),nullable=False)
    DeckOwner = relationship('user',back_populates = "decks")
    cards = relationship("card",back_populates="ParentDeck")

    def __init__(self,p2,p3):
        #self.deck_id = p1
        self.deck_name = p2
        self.owner = p3


class user(db.Model):
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    user_name = db.Column(db.Text,nullable=False,unique=True)
    disp_name = db.Column(db.Text,nullable=False)
    password = db.Column(db.Text,nullable=False)
    decks = relationship("deck",back_populates = "DeckOwner")

    def __init__(self,p2,p3,p4):
        #self.user_id = p1
        self.user_name = p2
        self.disp_name = p3
        self.password = generate_password_hash(p4)
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
db.create_all()
