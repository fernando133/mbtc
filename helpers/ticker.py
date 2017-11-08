from conf.config import Config
import urllib2
import ast

class Ticker:
    def __init__(self):
        cfg = Config()
        self.url = cfg.get_mbtc_env('ticker_url')

    def get_info(self):
        """
        Get real time info about prices and volume
        For more information see ticker at:
        https://www.mercadobitcoin.com.br/api-doc/#method_trade_api_ticker
        """
        content = urllib2.urlopen(self.url)
        ticker = ast.literal_eval(content.read())
        return ticker
