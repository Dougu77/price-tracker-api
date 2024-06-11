# Imports
from utils.get_datetime import *
from utils.http_request import *
from flask import Flask, jsonify, request

# Definition of the app
app = Flask(__name__)

# Endpoint
@app.route('/tracker/', methods=['GET'])
def get_product():
    
    # Get the necessary data
    url = request.args.get('url')
    name = get_name(url)
    price = get_price(url)
    date = get_date()
    time = get_time()
    
    # Create the dictionary (JSON)
    product = {
        'name': str(name),
        'price': str(price),
        'date': date,
        'time': time
    }
    return jsonify(product)
