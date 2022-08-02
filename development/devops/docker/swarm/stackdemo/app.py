from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello():
    count = redis.incr("hits")
    return f"Hello World! I have been seen {count} times.\n"


def main():
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    main()
