from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

driver = Blueprint('driver', __name__)

@driver.route('/drivers', methods=['GET'])
def get_drivers():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT DriverID, Availability, Insurance, Info, PhoneNumber, VehicleID, Lisence')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@driver.route('/delivery_requests', methods=['GET'])
def get_delivery_requests():
    
    query = '''
        SELECT Availability, DriverID, PhoneNumber, VehicleID
        FROM driver
        ORDER BY DriverID
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)

@driver.rount('/delivery_status/{deliveryID}', methods=['PUT'])
def update_deliver_status(deliveryID):
    query = '''
        SELECT PickupLocId, DropLocId, DeliveryTime, Delivered
        FROM Driver_Cus
        
    '''