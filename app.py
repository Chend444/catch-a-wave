# app.py
from flask import Flask
from routes.marine.marine_routes import marine_bp
from redis_config import redis  # Import the 'redis' object

app = Flask(__name__)
app.register_blueprint(marine_bp, url_prefix='/marine')

# Set Redis configuration in Flask app
app.config['REDIS'] = redis

if __name__ == '__main__':
    app.run(debug=True)
