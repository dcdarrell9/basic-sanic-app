import os

from sanic import Sanic, response


app = Sanic()

app_config = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(app_config)

app.strict_slashes = False


@app.route("/")
async def intro(request):
    return response.json({"Hello": "World"})


import sanic_app.views  # NOQA
