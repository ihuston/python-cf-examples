"""
A simple app to show redis service integration.

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask
import os
import redis
import json

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

# Get Redis credentials
if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    redis_env = services['rediscloud'][0]['credentials']
else:
    redis_env = dict(hostname='localhost', port=6379, password='')
redis_env['host'] = redis_env['hostname']
del redis_env['hostname']
redis_env['port'] = int(redis_env['port'])

# Connect to redis
try:
    r = redis.StrictRedis(**redis_env)
    r.info()
except redis.ConnectionError:
    r = None

@app.route('/')
def keys():
    if r:
        current_hits = r.incr('hits')
        return 'Hits: {}\n'.format(current_hits) + 'Available Keys: ' + str(r.keys())
    else:
        return 'No Redis connection available!'

@app.route('/<key>')
def get_current_values(key):
    if r:
        current_values = r.lrange(key, 0, -1)
        return str(current_values)
    else:
        abort(503)

@app.route('/<key>/<s>')
def add_value(key, s):
    if r:
        r.rpush(key, s)
        return 'Added {} to {}.'.format(s, key)
    else:
        abort(503)


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
