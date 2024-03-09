import os
from flask import Blueprint, render_template, request, current_app, session, redirect, url_for
from work_with_db import select_dict
from sql_provider import SQLProvider
from authentication_blueprint.access import group_required
from datetime import datetime

blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

#новое
@blueprint_query.route('/query_menu', methods = ['GET', 'POST'])
def start_index():
    return render_template("main_menu.html")



@blueprint_query.route('/session_by_date', methods=['GET', 'POST'])
@group_required
def query_index1():
    if request.method == 'POST':
        date_str = request.form.get('date')
        # Преобразуйте строку даты в формат, ожидаемый в SQL-запросе
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        _sql = provider.get('cinema.sql', formatted_date=formatted_date)
        sessions = select_dict(current_app.config['dbconfig'], _sql)

        if sessions:
            prod_title = 'Результат'
            return render_template('dynamic.html', prod_title=prod_title, sessions=sessions)
        else:
            return render_template('error.html')
    return render_template('input_param.html')


@blueprint_query.route('/query')
def query_index():
    return render_template('queries.html')



@blueprint_query.route('/revenue_by_date', methods=['GET', 'POST'])
@group_required
def query_index2():
    if request.method == 'POST':
        year = request.form.get('year')
        month = request.form.get('month')
        _sql = provider.get('cinema2.sql', year=year, month=month)
        sessions = select_dict(current_app.config['dbconfig'], _sql)
        if sessions:
            prod_title = 'Результат'
            return render_template('dynamic2.html', prod_title=prod_title, sessions=sessions)
        else:
            return render_template('error.html')
    return render_template('input_param2.html')

@blueprint_query.route('/film_without_tickets', methods=['GET', 'POST'])
def query_index3():
    if request.method == 'POST':
        year = request.form.get('year')
        _sql = provider.get('cinema3.sql', year=year)
        sessions = select_dict(current_app.config['dbconfig'], _sql)
        if session:
            prod_title = 'Результат'
            return render_template('dynamic3.html', prod_title=prod_title, sessions=sessions)
        else:
            return render_template('error.html')
    return render_template('input_param3.html')

@blueprint_query.route('/exit', methods = ['GET', 'POST'])
def query_exit_index():
    session.clear()
    #session.pop('user_id') #удаление сессии конкретного пользователя
    return redirect(url_for('auth_bp.auth_index'))

