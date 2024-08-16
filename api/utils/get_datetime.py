# Imports
from flask import request
import requests

# Function
def get_datetime():
    '''
    Get the time of when the search is made
    
    Returns:
        tuple: date, time
    '''
    
    try:
        client_ip = request.headers.get('X-Forwarded-For') or request.remote_addr
        url = f'https://worldtimeapi.org/api/ip/{client_ip}'
        response = requests.get(url)
        data = response.json()
        date = data.get('datetime')[:10]
        time = data.get('datetime')[11:19]
        datetime = (date, time)
        return datetime
    except:
        return None
