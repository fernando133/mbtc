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
