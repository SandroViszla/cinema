import json
from blueprint_report.route import  blueprint_report
from blueprint_query.route import blueprint_query
from blueprint_basket.route import blueprint_basket
from authentication_blueprint.access import authentication_blueprint, login_required
from flask import Flask, redirect, url_for, render_template, session

app = Flask(__name__)
with open('dbconfig.json') as f:
    app.config['dbconfig'] = json.load(f)

with open('authentication_blueprint/access.json') as f:
    app.config['access_config'] = json.load(f)

app.register_blueprint(blueprint_query, url_prefix = '/query')
app.register_blueprint(authentication_blueprint, url_prefix = '/auth')
app.register_blueprint(blueprint_report, url_prefix = '/report')
app.register_blueprint(blueprint_basket, url_prefix='/basket')

app.secret_key = 'you will never guess'
@app.route('/')
@login_required
def main_menu():
    return render_template('main_menu.html', user=session["user_group"])

#новое
@app.route('/exit')
def query_func():
    session.clear()
    #session.pop('user_id') #удаление сессии конкретного пользователя
    return redirect(url_for('auth_bp.auth_index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
