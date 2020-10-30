# Bitcoin-forex #

Problem Statement:
------------------------------------------------------------------------------------
To develop a service that constantly checks the currency exchange rate from Bitcoin to US Dollars (1 Bitcoin => X USD)


Approach:
------------------------------------------------------------------------------------

* Requirement Gathering
* Research and Analysis of Bitcoin APIs and services
* Creating 2 REST APIs for getLatestRate and getHistoricalRates using Flask app
* Transformation of data and mapping the API response to corresponding endpoints
* Return the JSON API results around the wrapper API


Overview of "d2d-vehicle-simulator" Workflow:
------------------------------------------------------------------------------------

1. Create Flask API (GET - /api/getLatestRate)
    * An API/wrapper around the Bitcoin service
    * Gets Bitcoin's latest conversion rate of USD by calling "get_latest_price()" method
    * Returns the json data with the latest USD price
    
2. Create Flask API (GET - /api/getHistoricalRates)
    * An API/wrapper around the Bitcoin service
	* Converts startDate and endDate to corresponding datetime format to query Bitcoin service
    * Gets Bitcoin's historical rates by calling "get_previous_price_list()" method between startDate and endDate
    * Returns the json data with the collection of historical rates
	
3. Create tests for Bitcoin service
	* Unit test cases written by using forex bitcoin service and pytest framework
	* Covered all edge cases and failure cases for both get_latest_price() and get_previous_price_list() methods
	
	
Installation:
------------------------------------------------------------------------------------
* Install using python package

	```pip install forex-python```
	
	
API usage:
--------------------------------------------------------------------------------------
1. Get Latest Rate -- /api/getLatestRate

	response:
		{
			"latest_rate": 13195.06
		}

2. Get Historical Rates -- /api/getHistoricalRates?startDate=<startDate>&endDate=<endDate>

	response:
		{
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
	
Project Structure:
--------------------------------------------------------------------------------------

1. src/bitcoin.py -- _An API/wrapper function for the Bitcoin service_
2. tests/test_bitcoin.py -- _Provides unit testing for Bitcoin service_
3. architecture.png -- _Approach and architecture of the project_


Pre requisites:
---------------------------------------------------------------------------------------

* Python 3.7 or Python 3.8
* Flask


Libraries Used:
---------------------------------------------------------------------------------------

1. _flask_restful_ -- Extension for Flask that adds support for quickly building REST APIs.
2. _forex-python_ -- Service that provides Foreign exchange rates and currency conversion.
3. _pytest_ -- Testing framework based on Python


PS: API screenshots available in /demo_screenshots/README.md