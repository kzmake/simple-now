from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def now(path):
    now = datetime.now().timestamp()
    return jsonify(
        {
            'unixtime': int(now),
            'unixtime_ms': int(now * 1000),
            'unixtime_ns': int(now * 1000 * 1000)
        }
    )

