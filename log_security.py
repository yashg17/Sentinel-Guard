import os, time, anthropic
from prometheus_client import start_http_server, Gauge

RISK_SCORE = Gauge('ai_log_mining_risk', 'Risk level of log patterns (0-10)')
client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))

def analyze():
    with open('portal.log', 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1); continue
            
            # Using prompt designed in Claude UI
            resp = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=10,
                messages=[{"role": "user", "content": f"Score this log risk for vulnerability scanning (0-10). Output ONLY number: {line}"}]
            )
            RISK_SCORE.set(float(resp.content[0].text))

if __name__ == "__main__":
    start_http_server(8000)
    analyze()
