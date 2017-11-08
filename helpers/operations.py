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

    def make_request(self, params, headers):
        """
        Make POST request for Mercado Bitcoin API with the params and headers informed
        """
        try:
            conn = httplib.HTTPSConnection(self.REQUEST_HOST)
            conn.request("POST", self.REQUEST_PATH, params, headers)
            response = conn.getresponse()
            response = response.read()
            response_json = json.loads(response, object_pairs_hook=OrderedDict)
            #return response_json
            return json.dumps(response_json, indent=4)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_params_headers(params):
        """
        Return the params and headers encoded within the params informed
        """
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
        return self.make_request(params, headers)

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
        return self.make_request(params, headers)

    def get_order(self, order_id, coin_pair):
        """
        Get order with the informed id
        """
        tapi_nonce = tapi_nonce = str(int(time.time()))
        params = {
            'tapi_method': 'get_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'order_id': order_id
        }
        params, headers = self.get_params_headers(params)
        return self.make_request(params, headers)

    def place_buy_order(self, quantity, coin_pair, limit_price):
        """
        Place a buy order with a quantity, coin_pair and limit price informed
        The limit price is for when the value of coin_pair reach it the order
        is executed
        """
        tapi_nonce = tapi_nonce = str(int(time.time()))
        params = {
            'tapi_method': 'place_buy_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'quantity': quantity,
            'limit_price': limit_price
        }
        params, headers = self.get_params_headers(params)
        return self.make_request(params, headers)

    def place_sell_order(self, quantity, coin_pair, limit_price):
        """
        Place a sell order with a quantity, coin_pair and limit price informed
        The limit price is for when the value of coin_pair reach it the order
        is executed
        """
        tapi_nonce = tapi_nonce = str(int(time.time()))
        params = {
            'tapi_method': 'place_sell_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'quantity': quantity,
            'limit_price': limit_price
        }
        params, headers = self.get_params_headers(params)
        return self.make_request(params, headers)
