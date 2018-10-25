import os

from sanic.log import logger

from sanic_app import app
from config import Config


if __name__ == "__main__":
    if not os.getenv("APP_SETTINGS"):
        os.environ["APP_SETTINGS"] = "DevelopmentConfig"

    logger.info("Starting listening on port {}".format(Config.PORT))
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=int(Config.PORT))
