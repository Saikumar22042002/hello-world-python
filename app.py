import os
import logging
from flask import Flask, jsonify, request

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Get environment variables with defaults
PORT = int(os.environ.get('PORT', 5000))
PYTHON_ENV = os.environ.get('PYTHON_ENV', 'development')

@app.route('/')
def home():
    """Main endpoint to return Hello World."""
    try:
        logging.info(f"Request received for / from {request.remote_addr}")
        return "Hello, World!", 200
    except Exception as e:
        logging.error(f"Error processing request for /: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/health')
def health_check():
    """Health check endpoint."""
    try:
        logging.debug(f"Health check requested from {request.remote_addr}")
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        logging.error(f"Error processing request for /health: {e}")
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500

if __name__ == '__main__':
    # This block is for local development and will not be executed by Gunicorn
    app.run(host='0.0.0.0', port=PORT, debug=(PYTHON_ENV != 'production'))
