from flask import Flask, request
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# 1. Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# 2. Setup Flask Metrics (This replaces the old DispatcherMiddleware)
# This automatically handles the /metrics route and monitors all other routes
metrics = PrometheusMetrics(app)

# Add some static info for your Prometheus dashboard
metrics.info('app_info', 'AI Sentinel', version='1.0.0')

@app.route('/')
def hello():
    return "AI Sentinel is running!"

@app.route('/api/data')
def get_data():
    param = request.args.get('query', 'none')
    return {"status": "success", "portal": "ParentPortal", "query": param}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
