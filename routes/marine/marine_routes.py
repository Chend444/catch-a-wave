# marine_routes.py
from flask import Blueprint, jsonify
from api import marine_handler
from redis_config import redis  # Import the 'redis' object
import json

marine_bp = Blueprint('marine', __name__)


@marine_bp.route('/city/waves/range/<cityName>', methods=['GET'])
def get_city_waves_range(cityName):
    city_redis_key = cityName + "-waves-range"
    cached_data = redis.get(city_redis_key)  # Access the 'get' method directly from 'redis'

    if cached_data:
        cached_data_decoded = cached_data.decode('utf-8')  # Decode bytes to a string
        cached_data_json = json.loads(cached_data_decoded)
        return jsonify({'message': cached_data_json})

    response_data = marine_handler.get_waves_peak_range(cityName)
    json_response_data = json.dumps(response_data)
    redis.setex(city_redis_key, 3600, json_response_data)

    return jsonify({'message': response_data})


@marine_bp.route('/city/waves/peak/<cityName>', methods=['GET'])
def get_city_waves_peak(cityName):
    city_redis_key = cityName + "-waves-peak"
    cached_data = redis.get(city_redis_key)  # Access the 'get' method directly from 'redis'

    if cached_data:
        cached_data_decoded = cached_data.decode('utf-8')  # Decode bytes to a string
        cached_data_json = json.loads(cached_data_decoded)
        return jsonify({'message': cached_data_json})


    response_data = marine_handler.get_waves_peak_hours(cityName)
    json_response_data = json.dumps(response_data)
    redis.setex(city_redis_key, 3600, json_response_data)
    return jsonify({'message': response_data})

