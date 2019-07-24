from marshmallow import fields
from app import db, ma
from .base import BaseModel, BaseSchema

class Year(db.Model, BaseModel):

    __tablename__ = 'years'

    year = db.Column(db.String(40), unique=True, nullable=False)

class YearSchema(ma.ModelSchema, BaseSchema):
    facts = fields.Nested('FactSchema', many=True, excludes=('year',))

    class Meta:
        model = Year
