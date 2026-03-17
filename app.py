from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics # Import the Flask-specific exporter

app = Flask(__name__)

# This single line handles the /metrics endpoint AND 
# automatically tracks request durations/counts for all routes
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "AI Sentinel is running!"

@app.route('/api/data')
def get_data():
    return {"status": "success"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
