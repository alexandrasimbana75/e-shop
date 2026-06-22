from flask import Blueprint
public_cb =Blueprint(
    'public',
    __name__,
    templante_folder='../../templantes/public'
)

from . import routes