import os
import json

class Config: 
    def __init__(cls): 
        file = open(os.path.abspath('conf/script_conf.json'), 'r')
        cls.conf = json.loads(file.read())
        cls._conf_key = 'script-conf'

    def get_mbtc_env(cls, key):
        temp = cls.conf[cls._conf_key]
        temp = temp['mbtc'][key]
        return str(temp)
