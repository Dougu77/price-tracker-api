# Imports
import requests
from bs4 import BeautifulSoup

# Functions
def request_url(url:str):
    '''
    Make the HTTP request
    
    Args:
        url (str): URL of the product
        
    Returns:
        BeautifulSoup: HTML content of the URL
    '''
    try:
        if url.find('://') == -1:
            url = url.replace(':/', '://')
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')
    except:
        return None

def get_store(url:str):
    '''
    Get the store of product
    
    Args:
        url (str): URL of the product

    Returns:
        str: First 5 letters of the store name
    '''
    
    try:
        index = url.find('www.') + 4
        return url[index:index + 5]
    except:
        return None

def get_store_name(url:str):
    '''
    Get the name of the store
    
    Args:
        url (str): URL of the product
    
    Returns:
        str: Full name of the store
    '''
    try:
        store = get_store(url)
        if store == 'kabum':
            name = 'Kabum'
        elif store == 'magaz':
            name = 'Magazine Luiza'
        elif store == 'eneba':
            name = 'Eneba'
        else:
            name = 'Website not supported'
        return name
    except:
        return None

def get_price(url:str):
    '''
    Get the price of the product

    Args:
        url (str): URL of the product

    Returns:
        str: Price of the product
    '''
    
    # Get the required data
    html = request_url(url)
    store = get_store(url)
    price = None
    
    # Find and format the price
    try:
        if store == 'kabum':
            price = format_price(html.find(class_ = 'finalPrice'))
        elif store == 'magaz':
            print(html.find_all(class_ = 'sc-kpDqfm eCPtRw sc-camqpD cFgZBi'))
            price = format_price(html.find(class_ = 'sc-kpDqfm eCPtRw sc-camqpD cFgZBi'))
        elif store == 'eneba':
            print(html.find_all(class_ = 'L5ErLT'))
            price1 = format_price(html.find(class_ = 'dXrfjQ'))
            price2 = format_price(html.find(class_ = 'L5ErLT'))
            if float(price1) > float(price2): price = price2
            else: price = price1
        return str(price)
    except:
        return None

def format_price(price:str):
    return price.text[3:].replace('.', '').replace(',', '.')

def get_name(url:str):
    '''
    Get the name of the product

    Args:
        url (str): URL of the product

    Returns:
        str: Name of the product
    '''
    
    # Get the required data
    html = request_url(url)
    store = get_store(url)
    
    # Find the name
    try:
        if store == 'kabum':
            name = html.find(class_ = 'sc-58b2114e-6').contents[0]
        elif store == 'magaz':
            name = html.find(class_ = 'gXZPqL').contents[0]
        elif store == 'eneba':
            name = html.find(class_ = 'C68dpx').contents[0]
        else:
            name = 'Website not supported'
        return name
    except:
        return 'API blocked by the website'
