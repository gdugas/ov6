# Quickstart

- install the module  

```bash
python setup.py install
```

- get your application keys (https://api.ovh.com/g934.first_step_with_api)  

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

- then, you can use the ovh api once your credential validate

```python
api = ov6.OVHApi(app_key, app_secret, consumer_key)

# OVHApi include GET, POST, PUT and DELETE methods
response = api.GET('/ip')

print(json.loads(response.read()))
```

