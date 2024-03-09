from DBcm import DBContextManager
from typing import Tuple, List

def select_dict(db_config: dict, _sql: str):
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        else:
            cursor.execute(_sql)
            products = cursor.fetchall()
            if products:
                products_dict = []
                schema = [item[0] for item in cursor.description]
                for product in products:
                    products_dict.append(dict(zip(schema, product)))
                return products_dict
            else:
                return None

def call_proc(dbconfig: dict, proc_name: str, *args):
    with DBContextManager(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        param_list = []
        for arg in args:
            param_list.append(arg)
        res = cursor.callproc(proc_name, param_list)
        return res

def insert(db_config:dict, _sql: str):
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Cursor not found')
        result = cursor.execute(_sql)
    return result

def update(db_config:dict, _sql:str):
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Update cursor not found')
        result = cursor.execute(_sql)
    return result

def select(db_config: dict, sql: str) -> Tuple[Tuple, List[str]]:
    """
    Выполняет запрос (SELECT) к БД с указанным конфигом и запросом.
    Args:
        db_config: dict - Конфиг для подключения к БД.
        sql: str - SQL-запрос.
    Return:
        Кортеж с результатом запроса и описанеим колонок запроса.
    """
    result = tuple()
    schema = []
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Cursor not found')
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        result = cursor.fetchall()
    return result, schema
