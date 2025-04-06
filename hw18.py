from flask import Flask, jsonify, request
from http import HTTPStatus

import db18

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'message': 'Server is up and running!'}), HTTPStatus.OK


@app.route('/categories', methods=['GET'])
def get_all_categories():
    categories = db18.get_all_categories()
    return jsonify({'categories': categories}), HTTPStatus.OK


@app.route('/categories/<int:categories_id>', methods=['GET'])
def get_categories_by_id(categories_id):
    if categories_id is None or categories_id <= 0:
        return jsonify({'error': 'Invalid categories id'}), HTTPStatus.BAD_REQUEST

    categories = db18.get_categories_by_id(categories_id)
    if categories is None:
        return jsonify({'error': 'Categories not found'}), HTTPStatus.NOT_FOUND

    return jsonify(categories), HTTPStatus.OK


@app.route('/categories', methods=['POST'])
def create_categories():
    try:
        categories = request.get_json()
    except Exception as e:
        return jsonify({'error': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST

    if categories is None:
        return jsonify({'error': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif categories['name'] is None or categories['name'] == '':
        return jsonify({'error': 'name is required'}), HTTPStatus.BAD_REQUEST

    db18.create_categories(categories['name'])

    return jsonify({'message': 'categories created successfully'}), HTTPStatus.CREATED


@app.route('/categories/<int:categories_id>', methods=['PUT'])
def update_categories(categories_id):
    if categories_id is None or categories_id <= 0:
        return jsonify({'error': 'Invalid categories id'}), HTTPStatus.BAD_REQUEST

    try:
        categories = request.get_json()
    except Exception as e:
        return jsonify({'error': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST

    if categories is None:
        return jsonify({'error': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif categories['name'] is None or categories['name'] == '':
        return jsonify({'error': 'name is required'}), HTTPStatus.BAD_REQUEST

    db18.update_categories(categories_id, categories['name'], categories['name'])

    return jsonify({'message': 'categories updated successfully'}), HTTPStatus.OK


@app.route('/categories/<int:categories_id>', methods=['DELETE'])
def delete_categories(categories_id):
    if categories_id is None or categories_id <= 0:
        return jsonify({'error': 'Invalid categories id'}), HTTPStatus.BAD_REQUEST

    db18.delete_categories(categories_id)
    return jsonify({'message': 'categories deleted successfully'}), HTTPStatus.OK


def main():
    try:
        db18.init_db()
        print("DB initialized successfully")
    except Exception as e:
        print(f"Error during DB initialization: {e}")

    try:
        app.run(port=5000)
    except Exception as e:
        print(f"Error during Server initialization: {e}")


main()