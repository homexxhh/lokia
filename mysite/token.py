#-*— coding:UTF-8 -*-
#/usr/bin/env python
"""
module descript
"""
import json
import requests
import time

from django.conf import settings
from lib.utils import ensure_effective


ACCESS_TOKEN = None
ACCESS_TOKEN_EFFECTIVE_TIME = 0


def get_access_token():
    global ACCESS_TOKEN_EFFECTIVE_TIME
    global ACCESS_TOKEN
    url_params = {"grant_type": "client_credential",
                  "appid": settings.APP_ACCESS['app_id'],
                  "secret": settings.APP_ACCESS['app_secret']}
    token_json = requests.get(settings.COMPANY_URL['token']['ACCESS_TOKEN_URL'],
                              params=url_params).json()
    ACCESS_TOKEN = token_json['access_token']
    ACCESS_TOKEN_EFFECTIVE_TIME = token_json['expires_in'] + time.time()


def ensure_access_token_effective(f):
    global ACCESS_TOKEN_EFFECTIVE_TIME
    return ensure_effective(f, get_access_token, ACCESS_TOKEN_EFFECTIVE_TIME)

