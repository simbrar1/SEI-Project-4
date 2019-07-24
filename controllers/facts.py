from flask import Blueprint, jsonify, request
from models.fact import Fact, FactSchema
from models.year import Year

api = Blueprint('facts', __name__)
fact_schema = FactSchema()

#index
@api.route('/facts', methods=['GET'])
def index():
    facts = Fact.query.all()
    return fact_schema.jsonify(facts, many=True), 200

#SHOW
@api.route('/facts/<int:fact_id>', methods=['GET'])
def show(fact_id):
    fact = Fact.query.get(fact_id)
    if not fact:
        return jsonify({'message': 'not found'}), 404
    return fact_schema.jsonify(fact), 200

#CREATE
@api.route('/facts', methods=['POST'])
def create():
    data = request.get_json()
    fact, errors = fact_schema.load(data)
    if errors:
        return jsonify(errors), 422
    fact.year = Year.query.filter_by(year=data['year_number']).first()
    fact.save()
    return fact_schema.jsonify(fact), 201


#EDIT
@api.route('/facts/<int:fact_id>', methods=['PUT'])
def update(fact_id):
    fact = Fact.query.get(fact_id)
    if not fact:
        return jsonify({'message': 'not found'}), 404
    data = request.get_json()
    fact, errors = fact_schema.load(data, instance=fact, partial=True)
    if errors:
        return jsonify(errors), 422
    fact.save()
    return fact_schema.jsonify(fact), 202

#DELETE
@api.route('/facts/<int:fact_id>', methods=['DELETE'])
def delete(fact_id):
    fact = Fact.query.get(fact_id)
    if not fact:
        return jsonify({'message': 'Not found'}), 404
    fact.remove()
    return '', 204
