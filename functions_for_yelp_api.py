# -*- coding: utf-8 -*-

import argparse
import json
import pprint
import sys
import urllib
import urllib2
import oauth2



API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 100
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = "18yM4kxmp6M97RZCtAn-xw"
CONSUMER_SECRET = "MnJXLlaUm3h1W4W_R0jtFSPf1js"
TOKEN = "XO5BmqAzc0yVlPHqS7CBXd2m5hpq2iHV"
TOKEN_SECRET = "tzaswqeMhqPo0bt1X79bnInToE4"


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(
        method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(
        oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response


#def search(term, location):
#    """Query the Search API by a search term and location.
#    Args:
#        term (str): The search term passed to the API.
#        location (str): The search location passed to the API.
#    Returns:
#        dict: The JSON response from the request.
#    """
#
#    url_params = {
#        'term': term.replace(' ', '+'),
#        'location': location.replace(' ', '+'),
#        'limit': SEARCH_LIMIT
#    }
#    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def search2(term, location, resultsnumber):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': resultsnumber
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)


def get_business(business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search2(term, location)

    businesses = response.get('businesses')

    if not businesses:
        print u'No businesses for {0} in {1} found.'.format(term, location)
        return

    business_id = businesses[0]['id']

    print u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id)
    response = get_business(business_id)

    print u'Result for business "{0}" found:'.format(business_id)
    pprint.pprint(response, indent=2)

def get_latitude(jsonitem):        
    "Return latitude from json entry"
    return jsonitem['location']['coordinate']['latitude']
    
def get_longitude(jsonitem):        
    "Return latitude from json entry"
    return jsonitem['location']['coordinate']['longitude']       

def property_getter(name, jsonitem):
    "Enter name as string"
    return jsonitem[name]

def get_name(jsonitem):
    return property_getter("name",jsonitem)
    
def get_price_range(jsonitem):
    return property_getter('RestaurantsPriceRange2',jsonitem)
    
def get_id(jsonitem):
    return property_getter('id',jsonitem)    
            
def get_image_url_original(jsonitem)    :        
    return property_getter('images_url_original',jsonitem)
    
def get_rating(jsonitem):
    return property_getter('rating',jsonitem)
    
def get_country_code(jsonitem):
    "Returns Unicode eg DE"
    return jsonitem['location']['country_code']
    
def get_city(jsonitem):
    return jsonitem['location']['city']
    
def get_postal_code(jsonitem):
    return jsonitem['location']['postal_code']
    
def get_address(jsonitem):
    return jsonitem['location']['address']
    
def make_query(term,location,number_of_results):
    "return list of responses of len (number)_of_results"
    response3 = search2(term,location,number_of_results)
    list_of_responses = []
    for i in response3['businesses']:
        list_of_responses.append(i)
    
    return list_of_responses

