from sanic_app import app
from sanic_app.views.health import health_bp
from sanic_app.views.info import info_bp


app.register_blueprint(health_bp, url_prefix="/health")
app.register_blueprint(info_bp, url_prefix="/info")

