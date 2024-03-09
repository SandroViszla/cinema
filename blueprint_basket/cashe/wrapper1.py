from functools import wraps
from blueprint_basket.cashe.connect1 import RedisCashe

def fetch_from_cash(name: str, cash_config: dict):
    cash_conn = RedisCashe(cash_config['redis'])
    #print('cash_conn=', cash_conn)
    ttl = cash_config['ttl']

    def cash_required(func):
        @wraps(func)
        def wrapper(*argc, **kwargs):
            cashed_items = cash_conn.get_value(name)
            if cashed_items:
                print("Достали из кэша")
                return cashed_items
            else:
                response = func(*argc, **kwargs)
                if response:
                    print("Достали из БД")
                    cash_conn.set_value(name, response, ttl)
                return response
        return wrapper
    return cash_required
