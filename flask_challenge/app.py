from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)

@app.route('/')
def hello_world():
    return 'We are running our first container - from CoderCo'

@app.route('/count')
def count_visits():
    new_count = redis_client.incr("visits")
    return f"This page has been visited {new_count} times"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
