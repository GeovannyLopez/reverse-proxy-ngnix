from datetime import datetime
import os
import redis
from flask import Flask

app = Flask(__name__)

# Read Environment Variables
redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')

# Initialize Redis
cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Main route
@app.route('/')
def welcome():
    # Get the item from cache
    last_visit = cache.get('lastVisit')
    if last_visit == None:
        last_visit = "Never"

    # Save the new datetime in cache
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cache.set('lastVisit', now)

    # Return a message
    return f'Previous visit was at {last_visit}!'