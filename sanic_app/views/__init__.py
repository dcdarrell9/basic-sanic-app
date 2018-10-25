from sanic_app import app
from sanic_app.views.health import health_bp

app.register_blueprint(health_bp, url_prefix="/health")
