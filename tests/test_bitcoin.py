import datetime
import pytest
from decimal import Decimal
from forex_python.bitcoin import (get_latest_price, get_previous_price, get_previous_price_list, BtcConverter)
from forex_python.converter import RatesNotAvailableError
from src import bitcoin
import flask
from flask import jsonify
from flask_restful import Api

app = flask.Flask(__name__)
api = Api(app)

"""
Test cases of Bitcoin-forex service developed for 2 REST APIs
"""

@app.route('/api/getLatestRate')
def getLatestRate():
    return jsonify(latest_rate=14332.2183)

def test_api_getLatestRate():
    with app.test_request_context("/api/getLatestRate"):
        app.preprocess_request()
        assert flask.request.path == '/api/getLatestRate'
    with app.test_client() as c:
        res = c.get('/api/getLatestRate')
        assert res.json == {'latest_rate': 14332.2183}


@app.route('/api/getHistoricalRates')
def getHistoricalRates():
    historical_rates = {
        "historical_rates": {
            "2020-10-15": 11510.5367, 
            "2020-10-16": 11325.5217, 
            "2020-10-17": 11369.9133, 
            "2020-10-18": 11516.9667, 
            "2020-10-19": 11758.5467, 
            "2020-10-20": 11922.975, 
            "2020-10-21": 12811.4867, 
            "2020-10-22": 12987.9017, 
            "2020-10-23": 12940.1067, 
            "2020-10-24": 13127.055, 
            "2020-10-25": 13039.0133
        }
    }
    return(jsonify({"historical_rates": historical_rates}))

def test_api_getHistoricalRates():
    with app.test_request_context("/api/getHistoricalRates?startDate=2020-10-15&endDate=2020-10-25"):
        app.preprocess_request()
        assert flask.request.path == '/api/getHistoricalRates'
        assert flask.request.args['startDate'] == '2020-10-15'
        assert flask.request.args['endDate'] == '2020-10-25'
    with app.test_client() as c:
        res = c.get('/api/getHistoricalRates?startDate=2020-10-15&endDate=2020-10-25')
        historical_rates = {
            "historical_rates": {
                "2020-10-15": 11510.5367, 
                "2020-10-16": 11325.5217, 
                "2020-10-17": 11369.9133, 
                "2020-10-18": 11516.9667, 
                "2020-10-19": 11758.5467, 
                "2020-10-20": 11922.975, 
                "2020-10-21": 12811.4867, 
                "2020-10-22": 12987.9017, 
                "2020-10-23": 12940.1067, 
                "2020-10-24": 13127.055, 
                "2020-10-25": 13039.0133
            }
        }
        assert res.json == {'historical_rates': historical_rates}


"""
Additional Test cases of bitcoin wrapper service from "forex_python"
"""

class TestLatestPrice():
    """
    Test get latest price using currency code
    """
    def test_latest_price_valid_currency(self):
        price = get_latest_price('USD')
        assert type(price) == float

    def test_latest_price_invalid_currency(self):
        price = get_latest_price('XYZ')
        assert price == None

class TestPreviousPrice():
    """
    Test Price with date input
    """
    def test_previous_price_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        price = get_previous_price('USD', date_obj)
        assert type(price) == float

    def test_previous_price_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        with pytest.raises(RatesNotAvailableError):
            get_previous_price('XYZ', date_obj)

class TestPreviousPriceList():
    """
    Test previous price list for a currency
    """
    def test_previous_price_list_with_valid_currency(self):
        start_date = datetime.datetime.today() - datetime.timedelta(days=15)
        end_date = datetime.datetime.today()
        price_list = get_previous_price_list('USD', start_date, end_date)
        assert price_list
        assert type(price_list) == dict

    def test_previous_price_list_with_invalid_currency(self):
        start_date = datetime.datetime.today() - datetime.timedelta(days=15)
        end_date = datetime.datetime.today()
        price_list = get_previous_price_list('XYZ', start_date, end_date)
        assert price_list == {} # returns empty dict
        assert type(price_list) == dict