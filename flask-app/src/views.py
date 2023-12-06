from flask import Blueprint

view = Blueprint('views', __name__)

@view.route('/')
def home():
    return ('<h1>Hi FROM THE WEB APP!</h1>')

@view.route('/test')
def tester():
    return "<h1>this is a test<h1>"