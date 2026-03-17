from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='portal.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/api/data')
def get_data():
    # Log the access pattern for AI mining
    param = request.args.get('query', 'none')
    app.logger.info(f"Access: param={param}, IP={request.remote_addr}")
    return {"status": "success", "portal": "ParentPortal"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
