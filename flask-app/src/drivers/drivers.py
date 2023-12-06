from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

drivers = Blueprint('drivers', __name__)

@drivers.route('/drivers', methods=['GET'])
def get_drivers():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Driver.DriverId, Availability, Insurance, Info, Driver.PhoneNumber, Driver_VehicleId.VehicleID, License '
                   'FROM Driver join Driver_VehicleId '
                   'on Driver.DriverId = Driver_VehicleId.DriverId')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@drivers.route('/delivery_requests', methods=['GET'])
def get_delivery_requests():
    
    query = '''
        SELECT Availability, DriverID, PhoneNumber, VehicleID
        FROM Driver
        ORDER BY DriverId
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@drivers.route('/delivery_status/{deliveryID}', methods=['PUT'])
def update_deliver_status(deliveryID):
    Delivered = False
    query = '''
        UPDATE Driver_Cus
        SET DeliveryTime = CURRENT_TIMESTAMP
            Delivered = %s
        WHERE DeliveryID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (Delivered, deliveryID))
    db.get_db().commit()


@drivers.route('/driver/<driver_id>/availability', methods=['PUT'])
def update_driver_availability(driver_id):
    availability = request.json['availability']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Driver SET Availability = %s WHERE DriverID = %s', (availability, driver_id))
    db.get_db().commit()
    return jsonify({'message': 'Driver availability updated successfully'})
