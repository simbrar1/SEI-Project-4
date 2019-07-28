from flask import Blueprint, jsonify, request, g
from models.fact import Fact, FactSchema, Comment, CommentSchema
from models.year import Year
from lib.secure_route import secure_route
from lib.helpers import is_unique

api = Blueprint('facts', __name__)
fact_schema = FactSchema()
comment_schema = CommentSchema()

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
@secure_route
def create():
    data = request.get_json()
    fact, errors = fact_schema.load(data)
    if not is_unique(model=Fact, key='name', value=data.get('name')):
        errors['name'] = errors.get('name', []) + ['Fact name already taken']
    if errors:
        return jsonify(errors), 422
    fact.year = Year.query.filter_by(year=data['year_number']).first()
    fact.creator = g.current_user
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

#create comment
@api.route('/facts/<int:fact_id>/comments', methods=['POST'])
def comment_create(fact_id):
    fact = Fact.query.get(fact_id)
    if not fact:
        return jsonify({'message': 'Not Found'}), 404
    data = request.get_json()
    comment, errors = comment_schema.load(data)
    if errors:
        return jsonify(errors), 422
    comment.fact = fact
    comment.save()
    return comment_schema.jsonify(comment), 202


#DELETE COMMENT
@api.route('/facts/<int:fact_id>/comments/<int:comment_id>', methods=['DELETE'])
def comment_delete(**kwargs):
    comment = Comment.query.get(kwargs['comment_id'])
    if not comment:
        return jsonify({'message': 'not found'}), 404
    comment.remove()
    return '', 204
