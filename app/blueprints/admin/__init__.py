from flask import Blueprint
admin_cb =Blueprint(
    'admin',
    __name__,
    templante_folder='../../templantes/admin'
)

from . import routes