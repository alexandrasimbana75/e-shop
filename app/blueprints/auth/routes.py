from flask import render_template
from . import public_cb

@public_cb.route('/login')
def login():
    return render_template('auth/login.html')

@public_cb.route('/registro')
def registro():
    return render_template('auth/registro.html')