from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET'])
def get_admin():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Admin.AdminId, Performance, Rating, Admin.PhoneNumber, TransactionFee, SupportPolicy, LegalStatus, Admin_FeedBack.FeedBackId, Admin_FeedBack.FeedBack '
                   'FROM Admin join Admin_FeedBack on Admin.AdminId = Admin_FeedBack.AdminId ')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@admin.route('admin/drivers', methods=['GET'])
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


@admin.route('/admin/customer', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute(
        'select Customer.CustomerID, Location.zip, Location.state, Location.city, Location.street, Location.apt, ' +
        'Restaurant.name as FavorateRestaurant, FoodName as FavoriteFood, Customer.PhoneNumber, PaymentMethod, deliveryPreference, Customer.adminId ' +
        'from Customer join Location on Customer.addressId = Location.locationId ' +
        'join Customer_FavoriteRestaurant on Customer.customerID = Customer_FavoriteRestaurant.CustomerId ' +
        'join Restaurant on Customer_FavoriteRestaurant.RestaurantId = Restaurant.restaurantID ' +
        'join Customer_FavoriteFood on Customer.customerID = Customer_FavoriteFood.CustomerId ' +
        'join FoodItem_Ava_P on Customer_FavoriteFood.FoodId = FoodItem_Ava_P.FoodId '
        'join Admin on Customer.AdminId = Admin.AdminId')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@admin.route('/admin/restaurant', methods=['GET'])
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

@admin.route('/addrestaurant', methods=['POST'])
def add_restaurant():
    cursor = db.get_db().cursor()


    location_id = cursor.lastrowid

    name = request.form.get('name')
    phoneNumber = request.form.get('phoneNumber')
    performance = request.form.get('performance')  
    sale = request.form.get('sale')      
    revenue = request.form.get('revenue')          
    locationId = request.form.get('locationId')    
    adminId = request.form.get('adminId')

    restaurant_query = '''
        INSERT INTO Restaurant(name, phoneNumber, locationId, performance, sale, revenue, adminId)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(restaurant_query, (name, phoneNumber, location_id, performance, sale, revenue, adminId))

    db.get_db().commit()

    return 'The restaurant and its location have been added'


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
     