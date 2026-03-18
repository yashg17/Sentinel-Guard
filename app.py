from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter # Ensure this is imported

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# 1. Define the custom metric (Must match your Grafana query name)
FAILED_LOGINS = Counter('security_failed_logins_total', 'Total failed login attempts')

@app.route('/')
def index():
    return "Sentinel Home"

# 2. Add the missing login route
@app.route('/api/login')
def login():
    status = request.args.get('status')
    if status == 'fail':
        FAILED_LOGINS.inc() # This "primes" the metric for Prometheus
        return "Login failure recorded", 401
    return "Login attempt received"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
