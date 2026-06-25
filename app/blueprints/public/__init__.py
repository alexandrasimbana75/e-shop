from flask import Blueprint
public_cb =Blueprint(
    'public',
    __name__,
    template_folder='../../templates/public'
)

from . import routes