from flask import Flask, request, jsonify
from api import marine_handler

app = Flask(__name__)

@app.route('/city-check/<cityName>', methods=['GET'])
def get_city_waves(cityName):
    # Use a function from marine_handler to generate the response
    response_data = marine_handler.check_city_waves(cityName)

    # Return the response as JSON
    return jsonify({'message': response_data})

if __name__ == '__main__':
    app.run(debug=True)
