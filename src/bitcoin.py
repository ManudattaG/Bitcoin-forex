from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from forex_python.bitcoin import BtcConverter
from datetime import datetime

# creating the flask app and API object
app = Flask(__name__)
api = Api(app)

# creating a resource to calculate latest price, 1 Bitcoin => X USD
class BitcoinLatestPrice(Resource):
    def get(self) -> dict:
        btc_obj = BtcConverter() # create BtcConverter class to get bitcoin conversion rates
        latest_price = btc_obj.get_latest_price("USD")
        return(jsonify({"latest_rate": latest_price}))

# creating another resource to calculate historical rates between two dates
class BitcoinHistoricalPrice(Resource):
    def get(self) -> dict:
        # creating request arguments
        args = request.args
        startDate = args["startDate"]
        endDate = args["endDate"]

        # create BtcConverter class to get bitcoin conversion rates
        btc_obj = BtcConverter()
        startDate = datetime.strptime(startDate, "%Y-%m-%d")
        endDate = datetime.strptime(endDate, "%Y-%m-%d")
        historical_price = btc_obj.get_previous_price_list("USD", startDate, endDate)
        return(jsonify({"historical_rates": historical_price}))


api.add_resource(BitcoinLatestPrice, '/api/getLatestRate')
api.add_resource(BitcoinHistoricalPrice, '/api/getHistoricalRates')

if __name__ == '__main__':
    app.run(debug=True)