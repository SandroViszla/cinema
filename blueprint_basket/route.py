from flask import Blueprint, render_template, request, current_app, session, redirect, url_for
from work_with_db import select_dict, insert, call_proc
from sql_provider import SQLProvider
from datetime import datetime
from authentication_blueprint.access import group_required, login_required
from DBcm import DBContextManager

import os

blueprint_basket = Blueprint('bp_basket', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_basket.route('/start')
@group_required
@login_required
def start():
    if 'basket' not in session.keys():
        print('!')
        session['basket'] = {}
    return redirect(url_for('bp_basket.choose'))


@blueprint_basket.route('/', methods=['GET', 'POST'])
@login_required
def choose():
    db_config = current_app.config['dbconfig']
    if request.method == 'GET':
        sql = provider.get('all_items.sql')
        print(sql)
        items = select_dict(db_config, sql)
        print(items)
        return render_template('basket_show.html', item=items, basket=session['basket'],
                               bask_keys=session['basket'].keys())
    else:
        id_product = request.form.get('idtikets')
        sql = provider.get('add_item.sql', id=id_product)
        item = select_dict(db_config, sql)[0]
        add_to_basket(session['basket'], item)
        if not session.modified:
            session.modified = True
        return redirect(url_for('bp_basket.choose'))


def add_to_basket(bask, item):
    if str(item['idtikets']) in bask.keys():
        bask[str(item['idtikets'])]['amount'] = 1
    else:
        bask[str(item['idtikets'])] = {'movie_name': item['movie_name'],
                                       'price': item['price'],
                                       'amount': 1,
                                       'seat': item['seat'],
                                       'row': item['row']}
    session["basket"] = bask


@blueprint_basket.route('/save_order', methods=['GET', 'POST'])
@login_required
def save_order():
    order_id = None
    user_id = session['user_id']
    db_config = current_app.config['dbconfig']
    if 'basket' in session.keys():
        with DBContextManager(db_config) as cursor:
            if cursor:
                sql = provider.get('insert_order.sql', user_id=user_id, user_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                cursor.execute(sql)
                order_id = cursor.lastrowid
                print("1")
                print(order_id)
                if order_id:
                    for key in session['basket'].keys():
                        item = session['basket'][key]
                        sql_insert = provider.get('insert_order_list.sql',
                                              order_id=order_id,
                                              id_product=key,
                                              product_amount=item['amount'],
                                              product_price=float(item['price']),
                                              movie=item['movie_name'],
                                              seat=item['seat'],
                                              row=item['row'])
                        cursor.execute(sql_insert)
                        sql_update = provider.get('sold_update.sql', id_product=key)
                        cursor.execute(sql_update)
                else:
                    return redirect(url_for('bp_basket.choose'))

    else:
        redirect(url_for('bp_basket.choose'))
    if not session['basket']:
        return redirect(url_for('bp_basket.choose'))

    session['basket'] = {}
    return render_template('done.html')


@blueprint_basket.route('/sec')
@login_required
@group_required
def menu():
    session.pop('basket', None)
    return redirect(url_for('index'))


@blueprint_basket.route('/clear')
@login_required
@group_required
def clear_basket():
    session['basket'] = {}
    return redirect(url_for('bp_basket.choose'))
