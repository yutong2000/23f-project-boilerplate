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
    the_data = request.json
    current_app.logger.info(the_data)
    
    restaurantid = the_data.get('restaurantID')
    name = the_data.get('name')
    phonenumber = the_data.get('phoneNumber')
    performance = the_data.get('performance ')
    sale = the_data.get('sale')
    revenue = the_data.get('revenue')
    locationid = the_data.get('locationId')
    adminid = the_data.get('adminId')
    
    query = 'INSERT INTO Restaurant (restaurantID, name, phoneNumber, performance, sale, revenue, locationid, adminId) VALUES ('
    query += f'"{restaurantid}", "{name}", "{phonenumber}", "{performance}", "{sale}", "{revenue}", "{locationid}", "{adminid}")'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@admin.route('/adddriver', methods=['POST'])
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


@admin.route('/addcustomer', methods=['Post'])
def add_customer():
     the_data = request.json
     current_app.logger.info(the_data)
     
     customerid = the_data.get('customerID')
     info = the_data.get('info')
     phonenumber = the_data.get('phoneNumber')
     addressid = the_data.get('addressId')
     paymentmethod = the_data.get('paymentMethod')
     deliveryperference = the_data.get('deliveryPreference')
     adminid = the_data.get("adminId")
     
     query = 'INSERT INTO Customer (customerID, Info, phoneNumber, addressId, paymentMethod, deliveryPreference, adminId) VALUES ('
     query += f'"{customerid}", "{info}", "{phonenumber}", "{addressid}", "{paymentmethod}", "{deliveryperference}", "{adminid}")'
     current_app.logger.info(query)

    
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
    
     return 'Success!'

@admin.route('/admin/customer/addlocation',methods=['POST'])
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