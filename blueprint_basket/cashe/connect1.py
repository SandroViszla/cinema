import json
from redis import Redis, DataError

class RedisCashe:
    def __init__(self, config):
        self.config = config
        self.conn = Redis(**self.config['redis'])

    def set_value(self, name, dict_value, ttl):
        json_value = json.dumps(dict_value)
        try:
            self.conn.set(name, json_value)
            if ttl > 0:
                self.conn.expire(name, ttl)
            return True
        except DataError as err:
            return False

    def get_value(self, name):
        js_value = self.conn.get(name)
        if js_value:
            dict_value = json.loads(js_value)
            return dict_value
        else:
            return None
