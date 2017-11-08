import os
import json

class MessageConfig: 
    def __init__(cls): 
        file = open(os.path.abspath('message/message_config.json'), 'r')
        cls.conf = json.loads(file.read())
        cls._conf_key = 'message-conf'

    def get_msg_env(cls, key):
        temp = cls.conf[cls._conf_key]
        temp = temp['msg'][key]
        return str(temp)
