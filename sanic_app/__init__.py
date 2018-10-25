import os

from jinja2 import Environment, PackageLoader
from sanic import Sanic, response


env = Environment(loader=PackageLoader('sanic_app', 'templates'))

app = Sanic()

app_config = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(app_config)

app.strict_slashes = False


@app.route("/")
async def intro(request):
    data = {'name': 'name'}
    template = env.get_template('index.html')
    html_content = template.render(name=data["name"])
    return response.html(html_content)


import sanic_app.views  # NOQA
