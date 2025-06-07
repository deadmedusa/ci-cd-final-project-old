"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Import after Flask app creation to avoid circular imports
from service import (  # pylint: disable=wrong-import-position,cyclic-import
    routes
)
from service.common import (  # pylint: disable=wrong-import-position
    log_handlers
)

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
