from flask import Blueprint, request, jsonify, make_response
import json
from src import db


customer = Blueprint('customer', __name__)

@customer.route('/customer', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute(
        'select CustomerID, zip, state, city, street, apt, FavoriteRestaurant, FavoriteFood, PhoneNumber, PaymentMethod, DeliveryPerference from Customer join Location on Customer.addressId = Location.locationId')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customer.route('/customers/<CostomerID>', methods=['GET'])
def get_customer(CustomerID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers where id = {0}'.format(CustomerID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response