from sanic import response, Blueprint

info_bp = Blueprint("info_bp", __name__)


@info_bp.route("/")
async def info(request):
    return response.json(
        {
            "version": "0.0.0",
            "created by": "Darrell",
            "Hello": "Emilio"
        }
    )
