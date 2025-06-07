"""
Service Package
"""
import logging
from flask import Flask

app = Flask(__name__)

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Import after Flask app creation to avoid circular imports
from service import routes  # pylint: disable=wrong-import-position

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
