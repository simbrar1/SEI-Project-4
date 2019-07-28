from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
#pylint: disable=W0611
from .year import Year
from .user import User


class Fact(db.Model, BaseModel):

    __tablename__ = 'facts'

    name = db.Column(db.String(100), nullable=False, unique=True)
    location = db.Column(db.String(100), nullable=False)
    date_of_fact = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String(3000), nullable=False)
    image = db.Column(db.Text, nullable=False)
    year_id = db.Column(db.Integer, db.ForeignKey('years.id'))
    year = db.relationship('Year', backref='facts')
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_facts')

class FactSchema(ma.ModelSchema, BaseSchema):

    year = fields.Nested('YearSchema', only=('year',))

    class Meta:
        model = Fact

    comments = fields.Nested('CommentSchema', many=True, exclude=('fact',))
    creator = fields.Nested('UserSchema', only={'id', 'username'})

class Comment(db.Model, BaseModel):
    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    fact_id = db.Column(db.Integer, db.ForeignKey('facts.id'))
    fact = db.relationship('Fact', backref='comments')

class CommentSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Comment
