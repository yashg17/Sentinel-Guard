from flask import Flask, request
import logging
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# 1. Setup Logging
logging.basicConfig(
    filename='portal.log', 
    level=logging.INFO, 
    format='%(asctime)s %(message)s'
)

# 2. Add Prometheus Middleware
# This captures all requests to /metrics and handles them automatically
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/')
def hello():
    return "AI Sentinel is running!"

@app.route('/api/data')
def get_data():
    # Log the access pattern for AI mining
    param = request.args.get('query', 'none')
    app.logger.info(f"Access: param={param}, IP={request.remote_addr}")
    return {"status": "success", "portal": "ParentPortal", "message": "AI Sentinel Active"}

if __name__ == "__main__":
    # Ensure it listens on all interfaces so Docker can reach it
    app.run(host='0.0.0.0', port=5000)
