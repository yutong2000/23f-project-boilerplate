# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'console'

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 project</h1>"

    # Import the various Beluprint Objects
    from src.drivers.drivers import drivers
    from src.admin.admin import admin
    from src.customer.customer import customer
    from src.restaurant.restaurant import restaurant

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(drivers,   url_prefix='/d')
    app.register_blueprint(admin,    url_prefix='/a')
    app.register_blueprint(customer, url_prefix = '/c')

    # Don't forget to return the app object
    return app