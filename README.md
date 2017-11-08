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
         }
    }
}
```

## Usage example (main.py):

```
from helpers.operations import Operations

op = Operations()
print op.list_orders('BRLBTC')

```

### output

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