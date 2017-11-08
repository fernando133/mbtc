# ms-mbtc
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
                "order_id": 44186369, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00819228", 
                "limit_price": "25379.99189", 
                "executed_quantity": "0.00819228", 
                "executed_price_avg": "25379.99189", 
                "fee": "0.00005735", 
                "created_timestamp": "1509970703", 
                "updated_timestamp": "1509970703", 
                "operations": [
                    {
                        "operation_id": 1168036, 
                        "quantity": "0.00819228", 
                        "price": "25379.99000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509970703"
                    }
                ]
            }, 
            {
                "order_id": 44137631, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.01570630", 
                "limit_price": "25467.48757", 
                "executed_quantity": "0.01570630", 
                "executed_price_avg": "25467.48757", 
                "fee": "0.00010994", 
                "created_timestamp": "1509887232", 
                "updated_timestamp": "1509887232", 
                "operations": [
                    {
                        "operation_id": 1164830, 
                        "quantity": "0.00430737", 
                        "price": "25467.47999", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509887232"
                    }, 
                    {
                        "operation_id": 1164831, 
                        "quantity": "0.01139893", 
                        "price": "25467.49000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509887232"
                    }
                ]
            }, 
            {
                "order_id": 44111261, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.02772000", 
                "limit_price": "25075.24675", 
                "executed_quantity": "0.02772000", 
                "executed_price_avg": "25075.24675", 
                "fee": "4.86560088", 
                "created_timestamp": "1509839769", 
                "updated_timestamp": "1509839769", 
                "operations": [
                    {
                        "operation_id": 1163702, 
                        "quantity": "0.02254000", 
                        "price": "25076.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509839769"
                    }, 
                    {
                        "operation_id": 1163703, 
                        "quantity": "0.00204000", 
                        "price": "25075.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509839769"
                    }, 
                    {
                        "operation_id": 1163704, 
                        "quantity": "0.00314000", 
                        "price": "25070.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509839769"
                    }
                ]
            }, 
            {
                "order_id": 44105840, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00458000", 
                "limit_price": "25439.76990", 
                "executed_quantity": "0.00458000", 
                "executed_price_avg": "25439.76990", 
                "fee": "0.81559902", 
                "created_timestamp": "1509830313", 
                "updated_timestamp": "1509830313", 
                "operations": [
                    {
                        "operation_id": 1163157, 
                        "quantity": "0.00458000", 
                        "price": "25439.76990", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509830313"
                    }
                ]
            }, 
            {
                "order_id": 44096887, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00098900", 
                "limit_price": "25449.94944", 
                "executed_quantity": "0.00098900", 
                "executed_price_avg": "25449.94944", 
                "fee": "0.00000692", 
                "created_timestamp": "1509814113", 
                "updated_timestamp": "1509814114", 
                "operations": [
                    {
                        "operation_id": 1162092, 
                        "quantity": "0.00098900", 
                        "price": "25450.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509814114"
                    }
                ]
            }, 
            {
                "order_id": 44049801, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00100000", 
                "limit_price": "25719.00000", 
                "executed_quantity": "0.00100000", 
                "executed_price_avg": "25719.00000", 
                "fee": "0.18003300", 
                "created_timestamp": "1509736843", 
                "updated_timestamp": "1509736843", 
                "operations": [
                    {
                        "operation_id": 1156484, 
                        "quantity": "0.00100000", 
                        "price": "25719.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509736843"
                    }
                ]
            }, 
            {
                "order_id": 44043078, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00204884", 
                "limit_price": "24979.98868", 
                "executed_quantity": "0.00204884", 
                "executed_price_avg": "24979.98868", 
                "fee": "0.00001434", 
                "created_timestamp": "1509728987", 
                "updated_timestamp": "1509728988", 
                "operations": [
                    {
                        "operation_id": 1154705, 
                        "quantity": "0.00204884", 
                        "price": "24980.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509728988"
                    }
                ]
            }, 
            {
                "order_id": 44042561, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00198196", 
                "limit_price": "24950.04945", 
                "executed_quantity": "0.00198196", 
                "executed_price_avg": "24950.04945", 
                "fee": "0.00001387", 
                "created_timestamp": "1509728236", 
                "updated_timestamp": "1509728236", 
                "operations": [
                    {
                        "operation_id": 1154622, 
                        "quantity": "0.00198196", 
                        "price": "24950.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509728236"
                    }
                ]
            }, 
            {
                "order_id": 44039840, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00200000", 
                "limit_price": "24899.99999", 
                "executed_quantity": "0.00200000", 
                "executed_price_avg": "24899.99999", 
                "fee": "0.34860000", 
                "created_timestamp": "1509724862", 
                "updated_timestamp": "1509724862", 
                "operations": [
                    {
                        "operation_id": 1154077, 
                        "quantity": "0.00200000", 
                        "price": "24899.99999", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509724862"
                    }
                ]
            }, 
            {
                "order_id": 44030912, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00572776", 
                "limit_price": "24499.97905", 
                "executed_quantity": "0.00572776", 
                "executed_price_avg": "24499.97905", 
                "fee": "0.00004009", 
                "created_timestamp": "1509713500", 
                "updated_timestamp": "1509713500", 
                "operations": [
                    {
                        "operation_id": 1152416, 
                        "quantity": "0.00572776", 
                        "price": "24500.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509713500"
                    }
                ]
            }, 
            {
                "order_id": 44023378, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00100000", 
                "limit_price": "24560.00000", 
                "executed_quantity": "0.00100000", 
                "executed_price_avg": "24560.00000", 
                "fee": "0.17192000", 
                "created_timestamp": "1509704128", 
                "updated_timestamp": "1509704128", 
                "operations": [
                    {
                        "operation_id": 1151262, 
                        "quantity": "0.00100000", 
                        "price": "24560.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509704128"
                    }
                ]
            }, 
            {
                "order_id": 43971411, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00150000", 
                "limit_price": "23580.00000", 
                "executed_quantity": "0.00150000", 
                "executed_price_avg": "23580.00000", 
                "fee": "0.24759000", 
                "created_timestamp": "1509624934", 
                "updated_timestamp": "1509624934", 
                "operations": [
                    {
                        "operation_id": 1146505, 
                        "quantity": "0.00150000", 
                        "price": "23580.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509624934"
                    }
                ]
            }, 
            {
                "order_id": 43970214, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00563073", 
                "limit_price": "23797.98001", 
                "executed_quantity": "0.00563073", 
                "executed_price_avg": "23797.98001", 
                "fee": "0.00003942", 
                "created_timestamp": "1509623835", 
                "updated_timestamp": "1509623835", 
                "operations": [
                    {
                        "operation_id": 1146358, 
                        "quantity": "0.00563073", 
                        "price": "23797.99994", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509623835"
                    }
                ]
            }, 
            {
                "order_id": 43921394, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00350000", 
                "limit_price": "23160.00000", 
                "executed_quantity": "0.00350000", 
                "executed_price_avg": "23160.00000", 
                "fee": "0.56742000", 
                "created_timestamp": "1509551539", 
                "updated_timestamp": "1509551539", 
                "operations": [
                    {
                        "operation_id": 1139988, 
                        "quantity": "0.00350000", 
                        "price": "23160.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509551539"
                    }
                ]
            }, 
            {
                "order_id": 43915263, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00384573", 
                "limit_price": "23399.97868", 
                "executed_quantity": "0.00384573", 
                "executed_price_avg": "23399.97868", 
                "fee": "0.00002692", 
                "created_timestamp": "1509538804", 
                "updated_timestamp": "1509538804", 
                "operations": [
                    {
                        "operation_id": 1137710, 
                        "quantity": "0.00384573", 
                        "price": "23399.99000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509538804"
                    }
                ]
            }, 
            {
                "order_id": 43909158, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00140000", 
                "limit_price": "23702.00000", 
                "executed_quantity": "0.00140000", 
                "executed_price_avg": "23702.00000", 
                "fee": "0.23227960", 
                "created_timestamp": "1509533680", 
                "updated_timestamp": "1509533680", 
                "operations": [
                    {
                        "operation_id": 1136237, 
                        "quantity": "0.00140000", 
                        "price": "23702.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509533680"
                    }
                ]
            }, 
            {
                "order_id": 43886756, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.02277951", 
                "limit_price": "21949.55028", 
                "executed_quantity": "0.02277951", 
                "executed_price_avg": "21949.55028", 
                "fee": "0.00015946", 
                "created_timestamp": "1509494503", 
                "updated_timestamp": "1509494503", 
                "operations": [
                    {
                        "operation_id": 1133748, 
                        "quantity": "0.01000000", 
                        "price": "21949.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509494503"
                    }, 
                    {
                        "operation_id": 1133749, 
                        "quantity": "0.01277951", 
                        "price": "21949.98884", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509494503"
                    }
                ]
            }, 
            {
                "order_id": 43886736, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.02320000", 
                "limit_price": "21935.00000", 
                "executed_quantity": "0.02320000", 
                "executed_price_avg": "21935.00000", 
                "fee": "3.56224400", 
                "created_timestamp": "1509494469", 
                "updated_timestamp": "1509494469", 
                "operations": [
                    {
                        "operation_id": 1133743, 
                        "quantity": "0.02320000", 
                        "price": "21935.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509494469"
                    }
                ]
            }, 
            {
                "order_id": 43879434, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00240000", 
                "limit_price": "21698.77000", 
                "executed_quantity": "0.00240000", 
                "executed_price_avg": "21698.77000", 
                "fee": "0.36453934", 
                "created_timestamp": "1509479338", 
                "updated_timestamp": "1509479338", 
                "operations": [
                    {
                        "operation_id": 1132537, 
                        "quantity": "0.00240000", 
                        "price": "21698.77000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509479338"
                    }
                ]
            }, 
            {
                "order_id": 43878492, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00238907", 
                "limit_price": "21644.40556", 
                "executed_quantity": "0.00238907", 
                "executed_price_avg": "21644.40556", 
                "fee": "0.00001672", 
                "created_timestamp": "1509477977", 
                "updated_timestamp": "1509477977", 
                "operations": [
                    {
                        "operation_id": 1132352, 
                        "quantity": "0.00238907", 
                        "price": "21644.41858", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509477977"
                    }
                ]
            }, 
            {
                "order_id": 43877154, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00240000", 
                "limit_price": "21700.00000", 
                "executed_quantity": "0.00240000", 
                "executed_price_avg": "21700.00000", 
                "fee": "0.36456000", 
                "created_timestamp": "1509475701", 
                "updated_timestamp": "1509475701", 
                "operations": [
                    {
                        "operation_id": 1132077, 
                        "quantity": "0.00240000", 
                        "price": "21700.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509475701"
                    }
                ]
            }, 
            {
                "order_id": 43877109, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00206811", 
                "limit_price": "21788.00934", 
                "executed_quantity": "0.00206811", 
                "executed_price_avg": "21788.00934", 
                "fee": "0.00001448", 
                "created_timestamp": "1509475611", 
                "updated_timestamp": "1509475611", 
                "operations": [
                    {
                        "operation_id": 1132067, 
                        "quantity": "0.00206811", 
                        "price": "21788.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509475611"
                    }
                ]
            }, 
            {
                "order_id": 43875292, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00212000", 
                "limit_price": "21400.00000", 
                "executed_quantity": "0.00212000", 
                "executed_price_avg": "21400.00000", 
                "fee": "0.31757600", 
                "created_timestamp": "1509472258", 
                "updated_timestamp": "1509472258", 
                "operations": [
                    {
                        "operation_id": 1131584, 
                        "quantity": "0.00212000", 
                        "price": "21400.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509472258"
                    }
                ]
            }, 
            {
                "order_id": 43875198, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00198469", 
                "limit_price": "21418.96216", 
                "executed_quantity": "0.00198469", 
                "executed_price_avg": "21418.96216", 
                "fee": "0.00001389", 
                "created_timestamp": "1509472073", 
                "updated_timestamp": "1509472073", 
                "operations": [
                    {
                        "operation_id": 1131562, 
                        "quantity": "0.00198469", 
                        "price": "21419.00007", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509472073"
                    }
                ]
            }, 
            {
                "order_id": 43872883, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.00201000", 
                "limit_price": "21299.00000", 
                "executed_quantity": "0.00201000", 
                "executed_price_avg": "21299.00000", 
                "fee": "0.29967693", 
                "created_timestamp": "1509469566", 
                "updated_timestamp": "1509469566", 
                "operations": [
                    {
                        "operation_id": 1131162, 
                        "quantity": "0.00201000", 
                        "price": "21299.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1509469566"
                    }
                ]
            }, 
            {
                "order_id": 43334301, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.02591223", 
                "limit_price": "18800.00293", 
                "executed_quantity": "0.02591223", 
                "executed_price_avg": "18800.00293", 
                "fee": "0.00018139", 
                "created_timestamp": "1508595351", 
                "updated_timestamp": "1508595351", 
                "operations": [
                    {
                        "operation_id": 1083337, 
                        "quantity": "0.02591223", 
                        "price": "18800.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1508595351"
                    }
                ]
            }, 
            {
                "order_id": 24565088, 
                "coin_pair": "BRLBTC", 
                "order_type": 2, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.03968000", 
                "limit_price": "2910.00097", 
                "executed_quantity": "0.03968000", 
                "executed_price_avg": "2910.00097", 
                "fee": "0.80828187", 
                "created_timestamp": "1485885594", 
                "updated_timestamp": "1485885594", 
                "operations": [
                    {
                        "operation_id": 399471, 
                        "quantity": "0.03968000", 
                        "price": "2910.00097", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1485885594"
                    }
                ]
            }, 
            {
                "order_id": 23800497, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.02423158", 
                "limit_price": "2953.99640", 
                "executed_quantity": "0.02423158", 
                "executed_price_avg": "2953.99640", 
                "fee": "0.00016962", 
                "created_timestamp": "1484854207", 
                "updated_timestamp": "1484854207", 
                "operations": [
                    {
                        "operation_id": 392384, 
                        "quantity": "0.02423158", 
                        "price": "2953.99698", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1484854207"
                    }
                ]
            }, 
            {
                "order_id": 23598073, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.01572647", 
                "limit_price": "2931.99936", 
                "executed_quantity": "0.01572647", 
                "executed_price_avg": "2931.99936", 
                "fee": "0.00011009", 
                "created_timestamp": "1484586639", 
                "updated_timestamp": "1484586639", 
                "operations": [
                    {
                        "operation_id": 389003, 
                        "quantity": "0.01572647", 
                        "price": "2931.99999", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1484586639"
                    }
                ]
            }, 
            {
                "order_id": 6343808, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.03671508", 
                "limit_price": "1790.00019", 
                "executed_quantity": "0.03671508", 
                "executed_price_avg": "1790.00019", 
                "fee": "0.00025701", 
                "created_timestamp": "1453321009", 
                "updated_timestamp": "1453321009", 
                "operations": [
                    {
                        "operation_id": 199327, 
                        "quantity": "0.03671508", 
                        "price": "1789.99999", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1453321009"
                    }
                ]
            }, 
            {
                "order_id": 6302729, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.03475143", 
                "limit_price": "1784.09924", 
                "executed_quantity": "0.03475143", 
                "executed_price_avg": "1784.09924", 
                "fee": "0.00024326", 
                "created_timestamp": "1453142924", 
                "updated_timestamp": "1453142924", 
                "operations": [
                    {
                        "operation_id": 198285, 
                        "quantity": "0.03475143", 
                        "price": "1784.09900", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1453142924"
                    }
                ]
            }, 
            {
                "order_id": 1348956, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.04555809", 
                "limit_price": "877.99993", 
                "executed_quantity": "0.04555809", 
                "executed_price_avg": "877.99993", 
                "fee": "0.00031891", 
                "created_timestamp": "1427130032", 
                "updated_timestamp": "1427130034", 
                "operations": [
                    {
                        "operation_id": 123056, 
                        "quantity": "0.04555809", 
                        "price": "878.00000", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1427130034"
                    }
                ]
            }, 
            {
                "order_id": 1280637, 
                "coin_pair": "BRLBTC", 
                "order_type": 1, 
                "status": 4, 
                "has_fills": true, 
                "quantity": "0.56590657", 
                "limit_price": "898.99999", 
                "executed_quantity": "0.56590657", 
                "executed_price_avg": "898.99999", 
                "fee": "0.00396135", 
                "created_timestamp": "1426111509", 
                "updated_timestamp": "1426111510", 
                "operations": [
                    {
                        "operation_id": 120766, 
                        "quantity": "0.56590657", 
                        "price": "898.99999", 
                        "fee_rate": "0.70", 
                        "executed_timestamp": "1426111510"
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