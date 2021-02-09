from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

from win32.fishing import Fishing


fish = Blueprint('fishing', url_prefix='/fishing')


@fish.route('/fish_bite', methods=['POST'])
async def fish_bite(request):
    logger.info(request.json)
    if request.json.get('event') != 'FishBite':
        return json({'status': 'error'})
    fishing = Fishing()
    await fishing.fish_bite()
    return json({'status': 'success'})
