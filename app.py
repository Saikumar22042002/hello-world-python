from flask import Flask, jsonify
import logging
import os

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Main endpoint that returns a friendly greeting."""
    logger.info("Request received for the root endpoint.")
    return jsonify({"message": "Hello World"}), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint for Kubernetes liveness and readiness probes."""
    logger.info("Health check request received.")
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # The application is run via Gunicorn in the Dockerfile, not this block.
    # This block is for local development only.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
