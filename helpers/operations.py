import httplib
import time
import hashlib
from conf.config import Config
from tapi_mac import TApiMac
import urllib
import json 
from collections import OrderedDict
from helpers.request import Request

class Operations:
    def __init__(self):
        cfg = Config()
        self.REQUEST_HOST = cfg.get_mbtc_env('request_host')
        self.REQUEST_PATH = cfg.get_mbtc_env('request_path')

    @staticmethod
    def get_params_headers(params):
        tapimac = TApiMac()
        mac = tapimac.get_tapi_mac(params)
        headers = tapimac.get_header(mac)
        params = urllib.urlencode(params)
        return params, headers

    def list_orders(self, coin_pair):
        """
        List all orders by the coin_pair informed (Ex: 'BRLBTC')
        """
        tapi_nonce = tapi_nonce = str(int(time.time()))
        params = {
            'tapi_method': 'list_orders',
            'tapi_nonce': tapi_nonce,
            'coin_pair': str(coin_pair)
        }

        params, headers = self.get_params_headers(params)

        try:
            conn = httplib.HTTPSConnection(self.REQUEST_HOST)
            conn.request("POST", self.REQUEST_PATH, params, headers)
            response = conn.getresponse()
            response = response.read()
            response_json = json.loads(response, object_pairs_hook=OrderedDict)
            return json.dumps(response_json, indent=4)
            print "status: %s" % response_json['status_code']
            # print(json.dumps(response_json, indent=4))
        finally:
            if conn:
                conn.close()

    def get_account_info(self):
        """
        Get balance of all cryptocurrency of the account
        """
        tapi_nonce = tapi_nonce = str(int(time.time()))
        params = {
            'tapi_method': 'get_account_info',
            'tapi_nonce': tapi_nonce
        }

        params, headers = self.get_params_headers(params)

        try:
            conn = httplib.HTTPSConnection(self.REQUEST_HOST)
            conn.request("POST", self.REQUEST_PATH, params, headers)
            response = conn.getresponse()
            response = response.read()
            response_json = json.loads(response, object_pairs_hook=OrderedDict)
            return json.dumps(response_json, indent=4), 
            #print "status: %s" % response_json['status_code']
            # print(json.dumps(response_json, indent=4))
        finally:
            if conn:
                conn.close()
