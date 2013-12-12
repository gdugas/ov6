HTTPSConnection = None
try:
    import httplib
    HTTPSConnection = httplib.HTTPSConnection
except ImportError:
    import http.client
    HTTPSConnection = http.client.HTTPSConnection

import json


ROOT_API = "eu.api.ovh.com"


def request_token(app_key, url,
                  POST=[],
                  GET=[],
                  PUT=[],
                  DELETE=[]):
    headers = {
        'X-Ovh-Application': app_key,
        'Content-type': 'application/json'
    }
    
    params = {
        'accessRules': [],
        'redirection': url
    }
    
    rules = []
    for path in POST:
        rules.append({'method': 'POST', 'path': path})
    for path in GET:
        rules.append({'method': 'GET', 'path': path})
    for path in PUT:
        rules.append({'method': 'PUT', 'path': path})
    for path in DELETE:
        rules.append({'method': 'DELETE', 'path': path})
    params['accessRules'] = rules
    
    conn = HTTPSConnection(ROOT_API)
    conn.request('POST', '/1.0/auth/credential',
                 headers = headers,
                 body=json.dumps(params))
    
    return conn.getresponse()


def get_ovh_timestamp():
    conn = HTTPSConnection(ROOT_API)
    conn.request('GET', '/1.0/auth/time')
    res = conn.getresponse()
    if res.status == 200:
        return int(res.read())


def sign_request(app_secret, consumer_key, method, query, timestamp,
                 body=''):
    import hashlib
    
    sign = "%s+%s+%s+%s+%s+%d" % (app_secret,
                                  consumer_key,
                                  method,
                                  query,
                                  body,
                                  timestamp)
    return "$1$" + hashlib.sha1(sign.encode('utf-8')).hexdigest()




class OVHApi(object):
    
    def __init__(self, app_key, app_secret, consumer_key):
        self.app_key = app_key
        self.app_secret = app_secret
        self.consumer_key = consumer_key
    
    def GET(self, path, timestamp=None):
        return self.request('GET', path, timestamp=timestamp)
    
    def DELETE(self, path, timestamp=None):
        return self.request('DELETE', path, timestamp=timestamp)
    
    def POST(self, path, params, timestamp=None):
        return self.request('POST', path,
                            params=params,
                            timestamp=timestamp)
    
    def PUT(self, path, params, timestamp=None):
        return self.request('PUT', path,
                            params=params,
                            timestamp=timestamp)
    
    
    def request(self, method, path,
                params=None,
                timestamp=None):
        
        body = ''
        method = method.upper()
        path = '/1.0' + path
        
        if not timestamp:
            timestamp = get_ovh_timestamp()
        
        if params:
            body = json.dumps(params)
        
        signature = sign_request(self.app_secret,
                                 self.consumer_key,
                                 method,
                                 'https://' + ROOT_API + path,
                                 timestamp,
                                 body)
        
        
        headers = {'X-Ovh-Application': self.app_key,
                   'X-Ovh-Signature': signature,
                   'X-Ovh-Consumer': self.consumer_key,
                   'X-Ovh-Timestamp': timestamp}
        
        conn = HTTPSConnection(ROOT_API)
        conn.request(method, path, body, headers)
        return conn.getresponse()
