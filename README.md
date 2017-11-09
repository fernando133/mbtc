# mbtc
Controll Interface for business API from Mercado Bitcoin:
<br/>```https://www.mercadobitcoin.com.br/trade-api/#comunicação-com-a-api```

The project will become a lib to who want`s automate the trading process of BTC and LTC cryptocurrencies in Brazil 

## script_conf.json

Should create the script_conf.json in the ```/conf``` folder with the ```API Key``` and ```ID``` of the account

```
{
    "script-conf":{
        "mbtc":{
            "secret"       : "API_KEY", 
            "id"           : "ID",
            "request_path" : "/tapi/v3/",
            "request_host" : "www.mercadobitcoin.net"
            "ticker_btc"   : "https://www.mercadobitcoin.net/api/BTC/ticker/",
            "ticker_ltc"   : "https://www.mercadobitcoin.net/api/LTC/ticker/"
         }
    }
}
```

## Usage example (main.py):

```
from helpers.operations import Operations
from helpers.ticker import Ticker

op = Operations() 
tc = Ticker() 
```
#### list_orders(coin_pair)
* coin_pair (String): ``` 'BRLBTC' ``` or ``` 'BRLLTC' ```

```
op.list_orders('BRLBTC')
```
##### output:

```
{
    "response_data": {
        "orders": [
            {
                "order_id": 44216530, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00808962", 
                "limit_price": "23945.50053", 
                "executed_quantity": "0.00808962", 
                "executed_price_avg": "23945.50053", 
                "fee": "0.00005663", 
                "created_timestamp": "1510001871", 
                "updated_timestamp": "1510001871", 
                "operations": [
                    {
                        "operation_id": 1174790, 
                        "quantity": "0.00808962", 
                        "price": "23945.48998", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1510001871"
                    }
                ]
            },
            {
                "order_id": 1238997, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.06456583", 
                "limit_price": "713.99996", 
                "executed_quantity": "0.06456583", 
                "executed_price_avg": "713.99996", 
                "fee": "0.00045196", 
                "created_timestamp": "1425000857", 
                "updated_timestamp": "1425000858", 
                "operations": [
                    {
                        "operation_id": 118546, 
                        "quantity": "0.06456583", 
                        "price": "714.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1425000858"
                    }
                ]
            }
        ]
    }, 
    "status_code": 100, 
    "server_unix_timestamp": "1510138289"
}
```

#### get_account_info()
```
op.get_account_info()
```
##### output:

```
{
    "response_data": {
        "balance": {
            "brl": {
                "available": "0.00322", 
                "total": "0.00322"
            }, 
            "btc": {
                "available": "0.01588714", 
                "total": "0.03176714", 
                "amount_open_orders": 1
            }, 
            "ltc": {
                "available": "0.98583252", 
                "total": "0.98583252", 
                "amount_open_orders": 0
            }, 
            "bch": {
                "available": "0.00000282", 
                "total": "0.00000282", 
                "amount_open_orders": 0
            }
        }, 
        "withdrawal_limits": {
            "brl": {
                "available": "20000.00", 
                "total": "20000.00"
            }, 
            "btc": {
                "available": "25.00000000", 
                "total": "25.00000000"
            }, 
            "ltc": {
                "available": "500.00000000", 
                "total": "500.00000000"
            }, 
            "bch": {
                "available": "25.00000000", 
                "total": "25.00000000"
            }
        }
    }, 
    "status_code": 100, 
    "server_unix_timestamp": "1510226543"
}
```

#### get_order(order_id, coin_pair)
* order_id (int)    : ```1167022```
* coin_pair (String): ``` 'BRLBTC' ``` or ``` 'BRLLTC' ```

```
op.get_order(1167022 , 'BRLLTC')
```
##### output:
```
{
    "response_data": {
        "order": {
            "order_id": 1167022, 
            "coin_pair": "BRLLTC", 
            "order_type": 1, 
            "status": 4, 
            "has_fills": true, 
            "quantity": "1.03673760", 
            "limit_price": "192.99001", 
            "executed_quantity": "1.03673760", 
            "executed_price_avg": "192.99001", 
            "fee": "0.00725716", 
            "created_timestamp": "1510067695", 
            "updated_timestamp": "1510067696", 
            "operations": [
                {
                    "operation_id": 361303, 
                    "quantity": "0.51781556", 
                    "price": "192.98000", 
                    "fee_rate": "0.70", 
                    "executed_timestamp": "1510067696"
                }, 
                {
                    "operation_id": 361304, 
                    "quantity": "0.51892204", 
                    "price": "193.00000", 
                    "fee_rate": "0.70", 
                    "executed_timestamp": "1510067696"
                }
            ]
        }
    }, 
    "status_code": 100, 
    "server_unix_timestamp": "1510227061"
}
```
#### place_buy_order(quantity, coin_pair, limit_price)
* quantity (double)    : ```0.01```
* coin_pair (String)   : ``` 'BRLBTC' ``` or ``` 'BRLLTC' ```
* limit_price (double) : ```1200.001```
```
op.place_buy_order(0.01, 'BRLBTC', 1200.001)
```
##### output:
```
{
    "response_data": {
        "order": {
            "order_id": 3,
            "coin_pair": "BRLBTC",
            "order_type": 1,
            "status": 4,
            "has_fills": true,
            "quantity": "1.00000000",
            "limit_price": "900.00000",
            "executed_quantity": "1.00000000",
            "executed_price_avg": "900.00000",
            "fee": "0.00300000",
            "created_timestamp": "1453835329",
            "updated_timestamp": "1453835329",
            "operations": [
                {
                    "operation_id": 1,
                    "quantity": "1.00000000",
                    "price": "900.00000",
                    "fee_rate": "0.30",
                    "executed_timestamp": "1453835329"
                }
            ]
        }
    },
    "status_code": 100,
    "server_unix_timestamp": "1453835329"
}
```
