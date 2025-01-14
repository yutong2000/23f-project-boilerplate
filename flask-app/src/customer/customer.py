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

@customer.route('/customer/order', methods=['GET'])
def get_order():
    cursor = db.get_db().cursor()
    cursor.execute(''' select Order_Foods.FoodId, OrdersInfo.PaymentMethod, OrdersInfo.TransactionDate, OrdersInfo.Cost
                        from OrdersInfo join Order_Foods on OrdersInfo.OrderId = Order_Foods.OrderId
''')
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

@customer.route('/customer/addlocation',methods=['POST'])
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

@customer.route('/addcustomer', methods=['Post'])
def add_customer():
     the_data = request.json
     current_app.logger.info(the_data)
     
     customerid = the_data.get('customerID')
     info = the_data.get('info')
     phonenumber = the_data.get('phoneNumber')
     addressid = the_data.get('addressId')
     paymentmethod = the_data.get('paymentMethod')
     deliveryperference = the_data.get('deliveryPreference')
     adminid = the_data.get('adminId')
     
     query = 'INSERT INTO Customer (customerID, Info, phoneNumber, addressId, paymentMethod, deliveryPreference, adminid) VALUES ('
     query += f'"{customerid}", "{info}", "{phonenumber}", "{addressid}", "{paymentmethod}", "{deliveryperference}", "{adminid}")'
     current_app.logger.info(query)

    
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
    
     return 'Success!'

@customer.route('/updatecustomer/<customerID>', methods=['PUT'])
def update_restaurant(customerID):
    the_data = request.json
    current_app.logger.info(the_data)

    info = the_data.get('info')
    phoneNumber = the_data.get('phoneNumber')
    addressid = the_data.get('addressId')
    paymentmethod = the_data.get('paymentMethod')
    deliveryperference = the_data.get('deliveryPerference')
    adminId = the_data.get('adminId')

    query = '''  
        UPDATE Customer
        SET info = %s, phoneNumber = %s, addressId = %s, paymentMethod = %s, deliveryPerference = %s, adminId = %s
        WHERE customerID = %s
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()


    return 'Info has updated.'

@customer.route('/deletecustomer/<int:customerID>', methods=['DELETE'])
def delete_customer(customerID):
    cursor = db.get_db().cursor()
    query = 'DELETE FROM Customer WHERE customerID = %s'
    cursor.execute(query, (customerID,))
    db.get_db().commit()
    return jsonify({'message': 'Customer deleted successfully'}), 200
