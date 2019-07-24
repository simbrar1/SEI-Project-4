from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
#pylint: disable=W0611
from .year import Year


class Fact(db.Model, BaseModel):

    __tablename__ = 'facts'

    name = db.Column(db.String(100), nullable=False, unique=True)
    date_of_fact = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String(600), nullable=False)
    image = db.Column(db.Text, nullable=False)
    year_id = db.Column(db.Integer, db.ForeignKey('years.id'))
    year = db.relationship('Year', backref='facts')

class FactSchema(ma.ModelSchema, BaseSchema):

    year = fields.Nested('YearSchema', only=('year',))

    class Meta:
        model = Fact
