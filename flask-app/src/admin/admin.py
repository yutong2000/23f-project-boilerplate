from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


admin = Blueprint('admin', __name__)

# Get all the products from the database
@admin.route('/admin', methods=['GET'])
def get_restaurant():
    cursor = db.get_db().cursor()
    cursor.execute('')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)