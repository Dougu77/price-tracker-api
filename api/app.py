# Imports
from flask import Flask, render_template, jsonify
from urllib.parse import unquote
from utils.http_request import get_name, get_price, get_store_name
from utils.get_datetime import get_datetime

# Create Flask app
app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Track product - endpoint
@app.route('/track/<path:url>', methods=['GET'])
@app.route('/track/<path:url>/timezone/<path:timezone>', methods=['GET'])
def get_product(url, timezone=None):
    
    # Decode the URL
    product_url = unquote(url)
    
    # Get the necessary data
    store_name = get_store_name(product_url)
    name = get_name(product_url)
    price = get_price(product_url)
    datetime = get_datetime(timezone)
    
    # Create the dictionary (JSON)
    product = {
        'store': store_name,
        'name': unquote(str(name)),
        'price': price,
        'date': datetime[0],
        'time': datetime[1]
    }
    return jsonify(product)

# Run application
# if __name__ == '__main__':
#     app.run()
