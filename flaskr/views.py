"""
só de zoas seguindo a live do cara agora falando sobre blueprint
"""

from flask import Blueprint, render_template

from .ga2.analysis.rsi_divergence import find_rsi_divergence, find_oversold
from .ga2.helpers import db
from .ga2.helpers import finance_api as api

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route('/')
def view_index():
    return render_template('index.html')


@bp.route('/stock_values')
def view_stock_values():
    return render_template(
        'stock_values.html',
        stock_values=db.read('hbor3', 180)
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


@bp.route('/update/insert/<stock_symbol>')
def view_update_insert(stock_symbol):
    sv_df = api.stock_values_as_dataframe(
        api.request_stock_values(stock_symbol), 180)
    rsi_df = api.rsi_as_dataframe(
        api.request_rsi(stock_symbol), 180)
    df = api.add_rsi_to_dataframe(sv_df, rsi_df)
    db.bulk_insert(stock_symbol, df)
    return render_template(
        'update.html',
        msg=f"{stock_symbol} adicionado com sucesso.",
        df=df
    )


@bp.route('/rsi_div')
def view_rsi_div():
    df = find_rsi_divergence(find_oversold(db.read('hbor3', 180)))
    return render_template(
        'rsi_div.html',
        df=df
    )


def configure(app):
    app.register_blueprint(bp)
