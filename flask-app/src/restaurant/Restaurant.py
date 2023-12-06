from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


restaurants = Blueprint('restaurants', __name__)

@restaurants.route('/restaurant', methods=['GET'])
def get_restaurant():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Availability, Name, Location, Rating')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@restaurants.route('/restaurants/<promotions>', methods=['GET'])
def get_restaurants_promotions (RestaurantID):

    query = 'Availability, Name, Location, Rating, RestaurantsID FROM Restaurant WHERE RestaurantID = ' + str(RestaurantID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)
    

@restaurants.route('/foodname', methods=['GET'])
def get_manu():
    cursor = db.get_db().cursor()
    query = '''
        SELECT FoodItem, Price
        FROM restaurants
        ORDER BY price
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)