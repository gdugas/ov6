# Quickstart

- install the module  

```bash
python setup.py install
```

- get your application keys (https://api.ovh.com/g934.first_step_with_api#creating_identifiers_creation_of_your_application_keys)  

```python
app_key = 'MY_APP_KEY'
app_secret = 'MY_APP_SECRET'
```

- now you can get your consumer key by making a token request

```python
import ov6

# Calling the request_token function will return an httplib.HTTPResponse object (or http.client.HTTPResponse for python3)
response = ov6.request_token(app_key,
                             redirect_url=None,
                             GET=['/*'],
                             POST=['/*'],
                             PUT=['/*'],
                             DELETE=['/*'])
import json
data = json.loads(response.read())

validation_url = data['validationUrl']
consumer_key = data['consumerKey']
```

- then, you can use the ovh api once your credential validated

```python
api = ov6.OVHApi(app_key, app_secret, consumer_key)

# OVHApi include GET, POST, PUT and DELETE methods
response = api.GET('/ip')

print(json.loads(response.read()))
```

# Reference


## ov6 functions

### ov6.get_ovh_timestamp()

Return the Ovh timestamp


### ov6.request_token(app_key, redirect_url=None, GET=['/\*'], POST=['/\*'], PUT=['/\*'], DELETE=['/\*'])

Return an OVH authentication token (https://api.ovh.com/g934.first_step_with_api#creating_identifiers_requesting_an_authentication_token_from_ovh)


### ov6.sign_request(app_secret, consumer_key, method, query, timestamp, body='')

Return a request signature (https://api.ovh.com/g934.first_step_with_api#using_the_api_for_the_first_time_signing_requests)


## ov6.OVHApi object

### OVHApi(app_key, app_secret, consumer_key)

Constructor

For the following GET, DELETE, POST and PUT methods, if no timestamp specified, the ovh timestamp will be requested

### OVHApi.DELETE(path, timestamp=None)

perform an HTTP DELETE on specified path  
return an httplib.HTTPResponse instance

### OVHApi.GET(path, timestamp=None)

perform an HTTP GET on specified path  
return an httplib.HTTPResponse instance

### OVHApi.POST(path, params, timestamp=None)

perform an HTTP POST on specified path with the specified dict 'params'  
return an httplib.HTTPResponse instance

### OVHApi.PUT(path, params, timestamp=None)

perform an HTTP PUT on specified path with the specified dict 'params'  
return an httplib.HTTPResponse instance
