from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


admin = Blueprint('admin', __name__)

@admin.route('/addrestaurant', methods=['POST'])
def add_restaurant():
    cursor = db.get_db().cursor()
    Availability = request.form('Availability')
    Name = request.form('Name')
    Rating = request.form('Rating')
    RestaurantID = request.form('RestaurantID')
    PhoneNumber = request.form('PhoneNumber')
    Location = request.form('Location')
    FoodItem = request.form('FoodItem')
    Price = request.form('Price')
    query = 'INSERT INTO Restaurant(Availability, Name, Rating, RestaurantID, PhoneNumber, Location, FoodItem, Price) values(%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(query)
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

     