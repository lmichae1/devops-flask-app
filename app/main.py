from flask import Flask, jsonify
import os
import logging

# Create Flask application instance
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/')
def home():
    """
    Home endpoint that returns API information
    """
    logger.info('Home endpoint was accessed')
    return jsonify({
        'message': 'DevOps Flask API',
        'version': '1.0.0',
        'status': 'running',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })


@app.route('/health')
def health():
    """
    Health check endpoint for monitoring
    """
    logger.info('Health check endpoint accessed')
    return jsonify({
        'status': 'healthy',
        'timestamp': '2024-01-01T00:00:00Z'
    }), 200


@app.route('/api/users')
def get_users():
    """
    Mock users endpoint to demonstrate API functionality
    """
    logger.info('Users endpoint accessed')
    # Mock data for demonstration
    users = [
        {'id': 1, 'name': 'Alice Johnson', 'role': 'developer', 'department': 'engineering'},
        {'id': 2, 'name': 'Bob Smith', 'role': 'devops', 'department': 'infrastructure'},
        {'id': 3, 'name': 'Carol Brown', 'role': 'tester', 'department': 'qa'}
    ]
    return jsonify({
        'users': users,
        'count': len(users)
    })


@app.route('/api/status')
def get_status():
    """
    Detailed status endpoint
    """
    import psutil
    import platform

    try:
        status_info = {
            'api_status': 'operational',
            'system_info': {
                'platform': platform.system(),
                'python_version': platform.python_version(),
                'cpu_count': psutil.cpu_count(),
                'memory_total_gb': round(psutil.virtual_memory().total / (1024 ** 3), 2)
            },
            'environment': os.getenv('ENVIRONMENT', 'development')
        }
        return jsonify(status_info)
    except ImportError:
        # Fallback if psutil is not available
        return jsonify({
            'api_status': 'operational',
            'environment': os.getenv('ENVIRONMENT', 'development'),
            'note': 'Limited system info available'
        })


if __name__ == '__main__':
    # Get port from environment variable, default to 5000
    port = int(os.getenv('PORT', 5000))
    # Get debug mode from environment variable
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    print(f"Starting Flask application on port {port}")
    print(f"Debug mode: {debug_mode}")
    print(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")

    app.run(debug=debug_mode, host='0.0.0.0', port=port)