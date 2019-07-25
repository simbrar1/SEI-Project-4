from flask import Blueprint

from models.breed import Year, YearSchema

api = Blueprint('years', __name__)
year_schema = YearSchema()

@api.route('/years', methods=['GET'])
def index():
    years = Year.query.all()
    return year_schema.jsonify(years, many=True), 200
