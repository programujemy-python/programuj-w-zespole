# test naszego API
import requests
import sys

requested_number = 48662144425

params = {
    'access_key': "19686b867a4226423da62bbe1c02e2e5",
    'number': requested_number,
    'country_code': "",
    'format': 1,
}

api_result = requests.get('http://apilayer.net/api/validate', params)
if api_result.status_code != 200:
    print(f"Some error on API - {api_result.status_code}!")
    sys.exit()

api_response = api_result.json()
if api_response['valid']:
    number = api_response['international_format']
    country = api_response['country_name']
    company = api_response['carrier']
    line_type = api_response['line_type']
    print(f"Number {number} is located in {country}, {line_type} from {company}.")
else:
    print(f"Requested number {requested_number} is not valid.")