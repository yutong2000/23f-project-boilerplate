from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/restaurant', methods=['GET'])
def get_restaurant():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Restaurant.restaurantID, name, Restaurant.phoneNumber, Restaurant.performance, sale, revenue, Location.zip, Location.state, Location.city, Location.street, Location.apt, Restaurant.adminId '
                   'FROM Restaurant join Restaurant_foodItem on Restaurant.restaurantID = Restaurant_foodItem.RestaurantId '
                   'join Location on Restaurant.locationId = Location.locationId ' 
                   'join Admin on Restaurant.adminId = Admin.adminId')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@restaurant.route('/restaurant/promotions', methods=['GET'])
def get_restaurants_promotions():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Restaurant.restaurantID, name, sale '
                   'FROM Restaurant ')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
    

@restaurant.route('/restaurant/menu/<restaurantId>', methods=['GET'])
def get_menu(restaurantId):
    cursor = db.get_db().cursor()

    query = '''
        SELECT FoodItem_Ava_P.FoodId, FoodItem_Ava_P.FoodName, FoodItem_Ava_P.availability, FoodItem_Ava_P.Price
        FROM FoodItem_Ava_P 
        JOIN Restaurant_foodItem ON FoodItem_Ava_P.FoodId = Restaurant_foodItem.FoodItem
        WHERE Restaurant_foodItem.RestaurantId = %s
        ORDER BY FoodItem_Ava_P.Price
    '''
    cursor.execute(query, (restaurantId,))

    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
