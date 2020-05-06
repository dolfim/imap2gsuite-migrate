import os
from functools import wraps
from flask import Response, g, request, jsonify
import requests
from cachecontrol import CacheControl

from jose import jwt
from jose.exceptions import JWTError

_GOOGLE_OAUTH2_CERTS_URL = "https://www.googleapis.com/oauth2/v1/certs"
OAUTH2_PROVIDER = {
    'issuer': 'accounts.google.com',
    'audience': os.getenv('OAUTH2_CLIENT_ID'),
    'options': {'verify_at_hash': False}
}

sess = requests.session()
cached_sess = CacheControl(sess)


def current_user():
    return g.get('auth_user_payload')

def gsuite_authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', '')
        token = token.replace('Bearer ', '').replace('bearer ', '')
        if not token:
            return jsonify({
                'message': 'Unauthorized. No Authorization token provided.',
                'code': 401
            }), 401

        r = cached_sess.get(_GOOGLE_OAUTH2_CERTS_URL)
        jws_key = r.json()
        try:
            payload = jwt.decode(token, jws_key, **OAUTH2_PROVIDER)
            print('Previous payload: ', current_user())
            g.auth_user_payload = payload
        except JWTError as err:
            return jsonify({
                'message': 'Unauthorized. ' + str(err),
                'code': 401
            }), 401

        return f(*args, **kwargs)
    return wrapper

