"""
só de zoas seguindo a live do cara agora falando sobre blueprint
"""

from flask import Blueprint, render_template, request

from .ga2.analysis.rsi_divergence import find_rsi_divergence, find_oversold
from .ga2.helpers import db
from .ga2.helpers import finance_api as api

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route('/')
def view_index():
    return render_template('index.html')


@bp.route('/stock_values', methods=['GET', 'POST'])
def view_stock_values():
    if request.method == "POST":
        stock_symbol = request.form['stock_symbol']
    else:
        stock_symbol = ''
    df = db.read(stock_symbol, 60)
    return render_template(
        'stock_values.html',
        stock_symbol=stock_symbol,
        df=df.to_html()
    )


@bp.route('/update')
def view_update():
    return render_template(
        'update.html',
        stock_symbols=['petr', 'itub', 'bbas']
    )


@bp.route('/update/delete')
def view_delete():
    db.drop_table()
    db.create_table()
    return render_template(
        'update.html',
        msg='dados removidos do bd por completo'
    )


@bp.route('/update/insert', methods=['POST'])
def view_update_insert():
    stock_symbol = request.form['stock_symbol']
    sv_df = api.stock_values_as_dataframe(
        api.request_stock_values(stock_symbol), 60)
    rsi_df = api.rsi_as_dataframe(
        api.request_rsi(stock_symbol), 60)
    df = api.add_rsi_to_dataframe(sv_df, rsi_df)
    db.bulk_insert(stock_symbol, df)
    return render_template(
        'update.html',
        msg=f"{stock_symbol} adicionado com sucesso.",
        df=df.to_html()
    )


@bp.route('/rsi_div', methods=['GET', 'POST'])
def view_rsi_div():
    if request.method == "POST":
        stock_symbol = request.form['stock_symbol']
    else:
        stock_symbol = ''
    df = find_rsi_divergence(find_oversold(db.read(stock_symbol, 60)))
    return render_template(
        'rsi_div.html',
        stock_symbol=stock_symbol,
        df=df.to_html()
    )


def configure(app):
    app.register_blueprint(bp)
