# redis_setup.py
from redis import Redis, ConnectionPool

# Set up Redis connection pool
redis_pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = Redis(connection_pool=redis_pool)
