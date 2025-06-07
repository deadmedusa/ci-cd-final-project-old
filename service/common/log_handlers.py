"""
Error Handlers Module
"""
from flask import jsonify
from service import app
from . import status

@app.errorhandler(status.HTTP_400_BAD_REQUEST)
def bad_request(error):
    """Handles bad requests with 400_BAD_REQUEST"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_400_BAD_REQUEST,
            error="Bad Request",
            message=message
        ),
        status.HTTP_400_BAD_REQUEST,
    )

# [Keep all your other existing error handlers...]
# No changes needed to the rest of the file
