from flask import Flask
from redis import Redis

redis = Redis(host="redis-server", port=6379)

app = Flask(__name__)

@app.route('/requests', methods=["GET"])
def req():
    counter = redis.incr("hits")
    return ('Number of hits: ' + str(counter))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
