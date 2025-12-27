from flask import Flask, jsonify
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """Hello World endpoint."""
    logger.info("Hello World endpoint was reached.")
    return jsonify({"message": "Hello World"}), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Kubernetes probes."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # The application port is configured using an environment variable for flexibility.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)