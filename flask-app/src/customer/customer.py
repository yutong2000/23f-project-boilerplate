from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


customer = Blueprint('customer', __name__)

@customer.route('/customer', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute(
        'select Customer.CustomerID, Customer.Info, Location.zip, Location.state, Location.city, Location.street, Location.apt, ' +
        'Restaurant.name as FavorateRestaurant, FoodName as FavoriteFood, Customer.PhoneNumber, PaymentMethod, deliveryPreference ' +
        'from Customer join Location on Customer.addressId = Location.locationId ' +
        'join Customer_FavoriteRestaurant on Customer.customerID = Customer_FavoriteRestaurant.CustomerId ' +
        'join Restaurant on Customer_FavoriteRestaurant.RestaurantId = Restaurant.restaurantID ' +
        'join Customer_FavoriteFood on Customer.customerID = Customer_FavoriteFood.CustomerId ' +
        'join FoodItem_Ava_P on Customer_FavoriteFood.FoodId = FoodItem_Ava_P.FoodId')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customer.route('/customers/order/update-foods', methods=['PUT'])
def update_order_foods():
    data = request.json
    order_id = data.get('OrderId')
    food_items = data.get('FoodItems')

    cursor = db.get_db().cursor()
    delete_query = 'DELETE FROM Order_Foods WHERE OrderId = %s'
    cursor.execute(delete_query, (order_id,))
    insert_query = 'INSERT INTO Order_Foods (OrderId, FoodId) VALUES (%s, %s)'
    for food_id in food_items:
        cursor.execute(insert_query, (order_id, food_id))
    db.get_db().commit()

    return jsonify({'message': 'Order foods updated successfully'}), 200

@customer.route('/customer',methods=['POST'])
def add_new_location():

    the_data = request.json
    current_app.logger.info(the_data)
    
    zip_code = the_data('Zip')
    state = the_data('State')
    city = the_data('City')
    street = the_data('Street')

    query = 'insert into products (product_name, description, category, list_price) values ("'
    query += zip_code + '", "'
    query += state + '", "'
    query += city + '", '
    query += street + ')'
    current_app.logger.info(query)

    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
    