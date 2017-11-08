# -*- coding: utf-8 -*-
import urllib
import hashlib
import hmac
import sys
from os import path
from conf.config import Config

class TApiMac:
    def __init__(self):
        """
        Constructor method of the class
        """
        cfg = Config()
        self.REQUEST_PATH   = cfg.get_mbtc_env('request_path')
        self.MB_TAPI_SECRET = cfg.get_mbtc_env('secret')
        self.MB_TAPI_ID     = cfg.get_mbtc_env('id')


    def get_tapi_mac(self, params):
        """
        Return the tapi_mac to the requests within
        the params informed
        """
        params = urllib.urlencode(params)
        params_string = self.REQUEST_PATH + '?' + params
        H = hmac.new(self.MB_TAPI_SECRET, digestmod=hashlib.sha512)
        H.update(params_string)
        tapi_mac = H.hexdigest()
        return tapi_mac

    def get_header(self, tapi_mac):
        """
        Get header for a request
        """
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'TAPI-ID': self.MB_TAPI_ID,
            'TAPI-MAC': tapi_mac
        }
        return headers
