###
from flask import Flask
from redis import Redis

redis = Redis(host="redis-server", port=6379)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return 'use one of the following end points /requests /queries'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
