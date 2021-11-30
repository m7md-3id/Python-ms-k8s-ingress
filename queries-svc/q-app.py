###
from flask import Flask
from redis import Redis

redis = Redis(host="redis-server", port=6379)

app = Flask(__name__)

@app.route('/queries', methods=["GET"])
def qr():
    counter = redis.get("hits")
    return (counter)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=82)
