from helpers.tapi_mac import TApiMac
from helpers.operations import Operations


params = {
    # Do exemplo acima, 'list_orders'
    'tapi_method': 'list_orders',
    # Do exemplo acima, 1
    'tapi_nonce': 1
}

a = TApiMac()
t = a.get_tapi_mac(params)
h = a.get_header(t)



op = Operations()

r = op.list_orders('BRLBTC')

#r = op.get_account_info()

print r