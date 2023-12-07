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
    query = '''
        SELECT FoodItem_Ava_P.FoodId, FoodItem_Ava_P.FoodName, FoodItem_Ava_P.availability, FoodItem_Ava_P.Price
        FROM FoodItem_Ava_P 
        JOIN Restaurant_foodItem ON FoodItem_Ava_P.FoodId = Restaurant_foodItem.FoodItem
        WHERE Restaurant_foodItem.RestaurantId = ''' + str(restaurantId)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@restaurant.route('/restaurant/addlocation',methods=['POST'])
def add_new_location():

    the_data = request.json
    current_app.logger.info(the_data)
    
    zip_code = the_data['zip']
    state = the_data['state']
    city = the_data['city']
    street = the_data['street']
    apt = the_data['apt']

    query = 'INSERT INTO Location (zip, state, city, street, apt) VALUES ('
    query += f'"{zip_code}", "{state}", "{city}", "{street}", "{apt}")'

    current_app.logger.info(query)

    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@restaurant.route('/restaurant/addrestaurant', methods=['POST'])
def add_restaurant():
    the_data = request.json
    current_app.logger.info(the_data)
    
    restaurantid = the_data.get('restaurantID')
    name = the_data.get('name')
    phonenumber = the_data.get('phoneNumber')
    performance = the_data.get('performance ')
    sale = the_data.get('sale')
    revenue = the_data.get('revenue')
    locationid = the_data.get('locationid')
    adminid = the_data.get('adminId')
    
    query = 'INSERT INTO Restaurant (restaurantID, name, phoneNumber, performance, sale, revenue, locationid, adminId) VALUES ('
    query += f'"{restaurantid}", "{name}", "{phonenumber}", "{performance}", "{sale}", "{revenue}", "{locationid}", "{adminid}")'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
