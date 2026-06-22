from flask import Blueprint
auth_bp =Blueprint(
    'auth',
    __name__,
    templante_folder='../../templantes/auth'
)

from . import routes