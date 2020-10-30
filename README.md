# Bitcoin-forex #

Problem Statement:
------------------------------------------------------------------------------------
To develop a service that constantly checks the currency exchange rate from Bitcoin to US Dollars (1 Bitcoin => X USD)


Approach:
------------------------------------------------------------------------------------

* Research and Analysis of Bitcoin APIs and services
* Create a flask app service around the Bitcoin wrapper function
* Create 2 REST API endpoints - getLatestRate and getHistoricalRates
* Transformation of data and mapping the API response to corresponding endpoints
* Return the JSON API results


Architecture Diagram
--------------------------------------------------------------------------------------

![Alt text](/architecture.png?raw=true "Architecture Diagram")


Overview of "Bitcoin-forex" Workflow:
------------------------------------------------------------------------------------

1. Create Flask API (GET - /api/getLatestRate)
    * An API/wrapper around the Bitcoin service
    * Gets Bitcoin's latest conversion rate of USD by calling "get_latest_price()" method
    * Returns the json data with the latest USD price
    
2. Create Flask API (GET - /api/getHistoricalRates)
    * An API/wrapper around the Bitcoin service
	* Converts startDate and endDate to corresponding datetime format to query Bitcoin service
	* Check period is configurable
    * Gets Bitcoin's historical rates by calling "get_previous_price_list()" method between startDate and endDate
    * Returns the json data with the collection of historical rates
	
3. Create tests for Bitcoin service
	* Unit test cases written by using forex bitcoin service and pytest framework
	* Covered all edge cases and failure cases for both get_latest_price() and get_previous_price_list() methods
	
	
	
API usage:
--------------------------------------------------------------------------------------
1. Get Latest Rate -- /api/getLatestRate

	```
	response:
		{
			"latest_rate": 13195.06
		}
	```

2. Get Historical Rates -- /api/getHistoricalRates?startDate="2020-10-15"&endDate="2020-10-25"

	```
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
	```
	
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


Library Installation:
------------------------------------------------------------------------------------
* Install using python package

	```
	pip install forex-python
	pip install flask_restful
	pip install flask
	pip install pytest
	```


Solution:
---------------------------------------------------------------------------------------

Hooray! Now our Bitcoin service is ready to use. To make this application production ready, we have several options:
1. _Deploying on Heroku_
	* Create a Procfile which is used to run a web app deployed on Heroku
	* Create requirements.txt file which is used as dependency libraries for the project
	* Create an app on Heroku and connect to the GitHub where the project is pushed
	* Create a deployment pipeline in Heroku
	
2. _Deploying on AWS_
	* Create API gateway REST APIs for both the endpoints
	* Additionally, API keys can be created for the REST APIs to be secured
	* Create a lambda function which corresponds to API gateway (trigger to lambda function)
	* Create a CI/CD pipeline using code build, code deploy to automatically trigger the build and deploy the service
	
```
AWS resources that can be used to deploy the service:
* API gateway -- To create REST APIs
* AWS Lambda function -- To write code without having to worry about infrastructure and scale automatically
* SSM parameter store -- To secretly store the credentials, URLs and API keys
* AWS Code Pipeline -- To automate release pipelines
* AWS CodeBuild -- To compile source code, runs tests, and produces software packages that are ready to deploy
* AWS CodeDeploy -- To deploy service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.
* AWS KMS -- Optionally we can use AWS Key Management Service to encrypt data and to automatically rotate customer master keys(CMK) if any
* AWS S3 -- Optionally we can use Simple Storage Service to store metadata information and to host any static web pages, sites.
* AWS DynamoDB -- Optionally we can use NoSql DynamoDB database to store items which has high availability and durability and to offload the administrative burden
```


PS: Bitcoin service demo screenshots available [here](/demo_screenshots/README.md)