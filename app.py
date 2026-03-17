from flask import Flask, request
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# 1. Setup Logging
logging.basicConfig(filename='portal.log', level=logging.INFO, format='%(asctime)s %(message)s')

# 2. Setup Automatic Flask Metrics
# this provides the /metrics endpoint AND tracks request durations
metrics = PrometheusMetrics(app)

# Static information for your dashboard
metrics.info('app_info', 'AI Sentinel Application', version='1.0.0')

@app.route('/')
def hello():
    return "AI Sentinel is running!"

@app.route('/api/data')
def get_data():
    param = request.args.get('query', 'none')
    app.logger.info(f"Access: param={param}, IP={request.remote_addr}")
    return {"status": "success", "portal": "ParentPortal"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
