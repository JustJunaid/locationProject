import json
from flask import Flask, request, jsonify
import requests
from config import db
from bson.json_util import dumps

app = Flask(__name__)

# db.locations.create_index([("location", '2dsphere')])


@app.route('/get_locations', methods=['POST'])
def location():
    request_data = json.loads(request.data)
    location_type, page_number = request_data.get(
        'location_type'), request_data.get('page_number')
    locationsCursor = db['locations'].find()
    locations = [
        location for location in locationsCursor if location['location'].get('type') == location_type]
    return jsonify({'success': True, 'locations': json.loads(dumps(locations))})


@app.route('/map', methods=['POST'])
def map():
    request_data = json.loads(request.data)
    coordinates, type = request_data.get(
        'coordinates'), request_data.get('location_type')
    locationsCursor = db['locations'].find({'location': {
        '$near': {
            '$geometry': {'type': type, 'coordinates': coordinates},
            '$minDistance': 0,
            '$maxDistance': 10000
        }
    }})
    location_coordinates = []
    for location in locationsCursor:
        location_coordinates.append(location['location']['coordinates'])
    return jsonify({'success': True, 'data': location_coordinates})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
