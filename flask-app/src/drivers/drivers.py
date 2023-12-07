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

@drivers.route('/adddriver', methods=['POST'])
def add_driver():
     the_data = request.json
     current_app.logger.info(the_data)
     
     driverid = the_data.get('DriverId')
     info = the_data.get('Info')
     phonenumber = the_data.get('PhoneNumber')
     license = the_data.get('License')
     insurance = the_data.get('Insurance')
     availability = the_data.get('Availability')
     adminid = the_data.get('AdminId')
     
     query = 'INSERT INTO Driver (DriverId, Info, PhoneNumber, License, Insurance, Availability, AdminId) VALUES ('
     query += f'"{driverid}", "{info}", "{phonenumber}", "{license}", "{insurance}", "{availability}", "{adminid}")'
     current_app.logger.info(query)

    
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
    
     return 'Success!'

@drivers.route('/drivers/order', methods=['GET'])
def order():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Driver_Cus.deliveryId, Driver_Cus.DriverId, Driver_Cus.OrderId, OrdersInfo.CustomerId  '
                   'FROM Driver_Cus JOIN Driver on Driver_Cus.DriverId = Driver.DriverId '
                   'JOIN OrdersInfo on Driver_Cus.OrderId = OrdersInfo.OrderId '
                   'JOIN Customer on OrdersInfo.CustomerId = Customer.CustomerId')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
'''
@drivers.route('/delivery_requests', methods=['GET'])
def get_delivery_requests():
    
    query = 
        SELECT Availability, DriverID, PhoneNumber, VehicleID
        FROM Driver
        ORDER BY DriverId
    
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
    query = 
        UPDATE Driver_Cus
        SET DeliveryTime = CURRENT_TIMESTAMP
            Delivered = %s
        WHERE DeliveryID = %s
    
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

@drivers.route('/driver/order_review/<int:DriverId>', methods=['GET'])
def review_order(DriverId):
    query = 
        SELECT Driver_Cus.DriverEarning, Driver_Cus.DriverId, Driver_Cus.DeliveryTime
        FROM Driver_Cus 
        JOIN Driver ON Driver_Cus.DriverId = Driver.DriverId
        WHERE Driver_Cus.DriverId = %s

    cursor = db.get_db().cursor()
    cursor.execute(query, (DriverId,))
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)
'''
