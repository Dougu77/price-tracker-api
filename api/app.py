from flask import Flask, render_template, jsonify
from urllib.parse import unquote
# from http_request import *
# from get_datetime import *

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# # Track product endpoint
# @app.route('/track/<path:url>', methods=['GET'])
# def get_product(url):
    
#     # Decode the URL
#     product_url = unquote(url)
    
#     # Get the necessary data
#     name = get_name(product_url)
#     price = get_price(product_url)
#     date = get_date()
#     time = get_time()
    
#     # Create the dictionary (JSON)
#     product = {
#         'name': str(name),
#         'price': str(price),
#         'date': date,
#         'time': time
#     }
#     return jsonify(product)
