from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

admin = Blueprint('admin', __name__)

@admin.route('/addrestaurant', methods=['POST'])
def add_restaurant():
    cursor = db.get_db().cursor()
    Availability = request.form.get('Availability')
    Name = request.form.get('Name')
    Rating = request.form.get('Rating')
    RestaurantID = request.form.get('RestaurantID')
    PhoneNumber = request.form.get('PhoneNumber')
    Location = request.form.get('Location')
    FoodItem = request.form.get('FoodItem')
    Price = request.form.get('Price')
    query = '''
        INSERT INTO Restaurant(Availability, Name, Rating, RestaurantID, PhoneNumber, Location, FoodItem, Price) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (Availability, Name, Rating, RestaurantID, PhoneNumber, Location, FoodItem, Price))
    db.get_db().commit()
    return 'The restaurant has been added'

@admin.route('/adddriver', methods=['POST'])
def add_driver():
     cursor = db.get_db().cursor()
     Availability = request.form('Availability')
     Info = request.form('Info')
     DriverID = request.form('DriverID')
     Insurance = request.form('Insurance')
     PhoneNumber = request.form('PhoneNumber')
     License = request.form('License')
     VehicleID = request.form('VehicleID')
     query = 'INSERT INTO Driver(Availability, Info, DriverID, Insurance, PhoneNumber, License, VehicleID) values(%s, %s, %s, %s, %s, %s, %s)'
     cursor.execute(query)
     db.get_db().commit()
     return 'The driver has been added'

@admin.route('/addcustomer', methods=['Post'])
def add_customer():
     cursor = db.get_db().cursor()
     Info = request.form('Info')
     Address = request.form('Address')
     PaymentMethod = request.form('PaymentMethod')
     PhoneNumber = request.form('PhoneNumber')
     CustomerID = request.form('CustomerID')
     DeliveryPerference = request.form('DeliveryPerference')
     query = 'INSERT INTO Customer(Info, CustomerID, Address, PhoneNumber, DeliveryPerference) values(%s, %s, %s, %s, %s)'
     cursor.execute(query)
     db.get_db().commit()
     return 'The costomer has been added'
     