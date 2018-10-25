from sanic import response, Blueprint

health_bp = Blueprint("health_bp", __name__)


@health_bp.route("/")
async def health(request):
    return response.json({"status": "ok"})
