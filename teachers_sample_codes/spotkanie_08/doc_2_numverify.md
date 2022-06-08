### Dostęp do API:

```
http://apilayer.net/api/validate
    ? access_key = YOUR_ACCESS_KEY
    & number = 14158586273
```

### Common API Errors:

```markdown
Type	Message	Description
404	"404_not_found"	User requested a resource which does not exist.
101	"missing_access_key"	User did not supply an Access Key.
101	"invalid_access_key"	User entered an invalid Access Key.
103	"invalid_api_function"	User requested a non-existent API function.
210	"no_phone_number_provided"	User did not provide a phone number.
```

### API Response:

```markdown
All numverify validation data is returned in universal and lightweight JSON format. Find below a standard API result set:

{
  "valid": true,
  "number": "14158586273",
  "local_format": "4158586273",
  "international_format": "+14158586273",
  "country_prefix": "+1",
  "country_code": "US",
  "country_name": "United States of America",
  "location": "Novato",
  "carrier": "AT&T Mobility LLC",
  "line_type": "mobile"
}      
```


#### Important: Please do not specify an additional `country_code` parameter when working with international numbers (e.g. `14158586273`).

----

### Sample code:

```python
import requests

params = {
    'access_key': 'YOUR_ACCESS_KEY',
    'number': 4158586273
}

api_result = requests.get('http://apilayer.net/api/validate', params)

api_response = api_result.json()

if api_response["valid"]:
    print(f"Number {api_response['number']} is located in {api_response['country_name']}")
    print(f"Type is {api_response['line_type']}, carrier: {api_response['carrier']}")
else:
    print(f"Number {api_response['number']} is invalid!")

```