from conf.config import Config
from message.message_config import MessageConfig
import urllib2
import ast


class Ticker:
    def __init__(self):
        cfg = Config()
        self.ticker_btc = cfg.get_mbtc_env('ticker_btc')
        self.ticker_ltc = cfg.get_mbtc_env('ticker_ltc')
        self.msg_cfg = MessageConfig()

    def get_info(self, coin):
        """
        Get real time info about prices and volume of a informed coin
        the method accept as input 'BTC' or 'LTC'
        For more information see ticker at:
        https://www.mercadobitcoin.com.br/api-doc/#method_trade_api_ticker
        """
        url =''
        if coin == 'BTC':
            url = self.ticker_btc
        elif coin == 'LTC':
            url = self.ticker_ltc
        else:
            return self.msg_cfg.get_msg_env('currency_not_exist')
        content = urllib2.urlopen(url)
        ticker = ast.literal_eval(content.read())
        return ticker
