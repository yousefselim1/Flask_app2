from flask import Blueprint, jsonify, request

# Create a Blueprint for the API routes
api = Blueprint('api', __name__)

data_store = []

# GET endpoint to fetch the stored data
@api.route('/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Data fetched successfully', 'data': data_store})



# POST endpoint to add data
@api.route('/data', methods=['POST'])
def post_data():
    data = request.json
    data_store.append(data)  # Add the new data to the in-memory list
    return jsonify({'message': 'Data received', 'yourData': data}), 201



# PUT endpoint to update data by index (or identifier)
@api.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.json
    if id < len(data_store):
        data_store[id] = data  # Update the data at the specified index
        return jsonify({'message': 'Data updated', 'id': id, 'newData': data})
    else:
        return jsonify({'message': 'Data not found'}), 404



# DELETE endpoint to delete data by index (or identifier)
@api.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    if id < len(data_store):
        deleted_data = data_store.pop(id)  # Remove the data at the specified index
        return jsonify({'message': f'Data with id {id} deleted', 'deletedData': deleted_data}), 204
    else:
        return jsonify({'message': 'Data not found'}), 404




@api.route('/data/<int:id>', methods=['PATCH'])
def patch_data(id):
    try:
        data = request.json
        data_store[id].update(data)  # Assumes the presence of a dictionary at the specified index
        return jsonify({'message': 'Data partially updated', 'id': id, 'newData': data_store[id]})
    except IndexError:
        return jsonify({'message': 'Data not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Invalid request', 'error': str(e)}), 400
