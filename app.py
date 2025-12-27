"""
This is the main application file for the Flask Hello World service.
It defines the web server and the API endpoints.
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Handles requests to the root URL."""
    return jsonify({"message": "Hello World"})

@app.route('/health', methods=['GET'])
def health_check():
    """Provides a health check endpoint for monitoring."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # This block is for local development and is not used by Gunicorn in production.
    app.run(host='0.0.0.0', port=5000)
