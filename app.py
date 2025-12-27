from flask import Flask, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Main endpoint, returns a hello world message."""
    logger.info("Root endpoint was called")
    return jsonify({"message": "Hello World"}), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    logger.info("Health check was called")
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # This block is for local development only
    app.run(host='0.0.0.0', port=5000, debug=True)
