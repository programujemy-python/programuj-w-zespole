### Dostęp do API:

```
https://api.aviationstack.com/v1/flights?access_key = YOUR_ACCESS_KEY
```

### Common API Errors:

```
401	invalid_access_key	An invalid API access key was supplied.
401	missing_access_key	No API access key was supplied.
401	inactive_user	The given user account is inactive.
403	https_access_restricted	HTTPS access is not supported on the current subscription plan.
403	function_access_restricted	The given API endpoint is not supported on the current subscription plan.
404	invalid_api_function	The given API endpoint does not exist.
404	404_not_found	Resource not found.
429	usage_limit_reached	The given user account has reached its monthly allowed request volume.
429	rate_limit_reached	The given user account has reached the rate limit.
500	internal_error	An internal error occurred.
```

### Pparameters:

```
access_key    [Required] Your API access key, which can be found in your acccount dashboard. 
```

### Sample code:

```python
import requests

params = {
    'access_key': 'YOUR_ACCESS_KEY'
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
if api_result.status_code != 200:
    print(f"Some error on API - {api_result.status_code}!")
    sys.exit()

api_response = api_result.json()
```