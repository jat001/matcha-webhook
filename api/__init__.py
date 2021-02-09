from sanic import Blueprint

from .fishing import fish


api = Blueprint.group(fish, url_prefix='/api')
