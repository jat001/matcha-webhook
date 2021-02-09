from sanic import Sanic

from api import api


app = Sanic(name='matcha-webhook')
app.blueprint(api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
