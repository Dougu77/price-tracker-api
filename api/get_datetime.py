# Imports
from datetime import datetime

# Functions
def get_date():
    '''
    Get the date of when the search is made
    
    Returns:
        str: Date
    '''
    
    try:
        return datetime.now().strftime('%y-%m-%d')
    except:
        return None

def get_time():
    '''
    Get the time of when the search is made
    
    Returns:
        str: Time
    '''
    
    try:
        return datetime.now().strftime('%H:%M:%S')
    except:
        return None
