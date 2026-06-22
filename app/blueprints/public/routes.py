from flask import render_template
from . import public_cb

@public_cb.route('/')
def home():
    return render_template('public/home.html')

@public_cb.route('t/ienda')
def tienda():
    return render_template('public/tienda.html')
@public_cb.route('/contacto')
def contacto():
    return render_template('public/contacto.html')
